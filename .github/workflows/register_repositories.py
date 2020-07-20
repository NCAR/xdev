import asyncio
import copy
import json
import logging
import os
from datetime import datetime

import aiohttp
import ruamel.yaml as yaml

logging.basicConfig(level=logging.INFO)

API_BASE_URL = 'https://api.github.com'

XDEVBOT_MAIN_ENDPOINT = 'http://xdevbot.herokuapp.com/gh/testing'


def parse_line(line, original_config, repos={'remove': [], 'add': []}):
    config = copy.deepcopy(original_config)
    valid_line = line.startswith('/add-repo') or line.startswith('/remove-repo')
    if valid_line:
        if line.startswith('/add-repo'):
            split_on = '/add-repo'
        else:
            split_on = '/remove-repo'
        parsed_info = line.split(split_on)[-1].strip().split()
        info = {}
        for item in parsed_info:
            x = item.strip().split(':')
            info[x[0]] = x[1]

        if split_on == '/add-repo':
            if info['repo'] not in set(config[info['campaign']]['repos']):
                config[info['campaign']]['repos'].append(info['repo'])
                repos['add'].append(info['repo'])

        else:
            try:
                config[info['campaign']]['repos'].remove(info['repo'])
            except ValueError:
                pass
            finally:
                repos['remove'].append(info['repo'])

    return config


def configure(config_file='config.yaml'):
    repos = {'remove': [], 'add': []}
    with open(config_file) as resp:
        original_config = yaml.safe_load(resp)

    with open(os.environ['GITHUB_EVENT_PATH'], 'r') as f:
        event_payload = json.load(f)
    comment = event_payload['issue']['body']
    # comment = """
    # Foo\n/add-repo repo:NCAR/integral campaign:analysis\n/add-repo repo:NCAR/test campaign:core\nbar\n/remove-repo repo:NCAR/xdevbot-testing campaign:core\n/add-repo repo:NCAR/xdev-bot-testing campaign:core\n
    # \n/remove-repo repo:NCAR/jupyterlab-pbs campaign:platform
    # """
    comment = comment.splitlines()
    config = copy.deepcopy(original_config)
    for line in comment:
        config = parse_line(line, config, repos)
    return config, original_config, repos


async def delete_repo_webhook(
    repo,
    hooks_info={},
    username=os.environ.get('GH_USERNAME', ''),
    token=os.environ.get('GH_TOKEN', ''),
):

    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}',
        'User-Agent': username,
    }

    url = f'{API_BASE_URL}/repos/{repo}/hooks'

    async with aiohttp.ClientSession(headers=headers) as client:

        logging.info('Retrieving repository webhooks metadata.')
        async with client.get(url) as response:
            hooks = await response.json()
            if response.status == 200:
                potl_hooks = []
                for hook in hooks:
                    if (
                        set(hook['events']) == {'issues', 'pull_request'}
                        and hook['config']['url'] == XDEVBOT_MAIN_ENDPOINT
                        and hook['config']['content_type'] == 'json'
                    ):
                        potl_hooks.append(hook)

                if potl_hooks:
                    for hook in potl_hooks:
                        logging.info('Deleting repository webhook.')
                        url = f"{url}/{hook['id']}"
                        async with client.delete(url) as response:
                            if response.status != 204:
                                logging.error('Failed to delete repository webhook.')
                            else:
                                logging.info('Deleted repository webhook.')
                                hooks_info[repo] = url


async def install_repo_webhook(
    repo,
    hooks_info={},
    username=os.environ.get('GH_USERNAME', ''),
    token=os.environ.get('GH_TOKEN', ''),
):

    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}',
        'User-Agent': username,
    }

    url = f'{API_BASE_URL}/repos/{repo}/hooks'

    async with aiohttp.ClientSession(headers=headers) as client:

        logging.info('Retrieving repository webhooks metadata.')
        async with client.get(url) as response:
            hooks = await response.json()
            if response.status == 200:
                potl_hooks = []
                for hook in hooks:
                    if (
                        set(hook['events']) == {'issues', 'pull_request'}
                        and hook['config']['url'] == XDEVBOT_MAIN_ENDPOINT
                        and hook['config']['content_type'] == 'json'
                        and hook['active']
                    ):
                        potl_hooks.append(hook)

                if len(potl_hooks) == 0:
                    logging.info('Creating repository webhook.')
                    request = dict(
                        name='web',
                        events=['issues', 'pull_request'],
                        config=dict(url=XDEVBOT_MAIN_ENDPOINT, content_type='json'),
                    )
                    async with client.post(url, json=request) as response:
                        main_hook = await response.json()
                        if response.status != 201:
                            logging.error('Failed to create repository webhook.')

                elif len(potl_hooks) == 1:
                    logging.info('Existing repository webhook found.')
                    main_hook = potl_hooks[0]

                else:
                    timestamps = [
                        datetime.strptime(hook['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
                        for hook in potl_hooks
                    ]
                    newest_timestamp, i_hook = max((t, i) for (i, t) in enumerate(timestamps))[1]
                    logging.info(
                        f'Found {len(potl_hooks)} potential webhooks on the repository, '
                        f'choosing most recent webhook at {newest_timestamp}.'
                    )
                    main_hook = potl_hooks[i_hook]

                hooks_info[repo] = main_hook

            else:
                logging.error('Could not retrieve repository metadata.')


if __name__ == '__main__':

    config_file = 'config.yaml'
    new_config, old_config, repos = configure(config_file)
    if new_config != old_config:
        with open(config_file, 'w') as file_obj:
            yaml.round_trip_dump(new_config, file_obj, indent=2, block_seq_indent=2)

    added_hooks = {}
    removed_hooks = {}
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(install_repo_webhook(repo, added_hooks)) for repo in repos['add']] + [
        loop.create_task(delete_repo_webhook(repo, removed_hooks)) for repo in repos['remove']
    ]
    loop.run_until_complete(asyncio.gather(*tasks))

    added_successes = set(added_hooks.keys())
    added_failures = set(repos['add']) - added_successes
    removed_successes = set(removed_hooks.keys())
    removed_failures = set(repos['remove']) - removed_successes

    with open('hooks_log.txt', 'w') as f:
        print('\n#### 1. Additions', file=f)
        if added_successes:
            print('\n**Webhook was successfully installed on:**\n', file=f)
            for repo in added_successes:
                print(f'- {repo}', file=f)

        if added_failures:
            print('\n**Unable to install the webhook on:**\n', file=f)
            for repo in added_failures:
                print(f'- {repo}', file=f)

        print('\n#### 2. Deletions', file=f)
        if removed_successes:
            print('\n**Webhook was successfully removed on:**\n', file=f)
            for repo in removed_successes:
                print(f'- {repo}', file=f)

        if removed_failures:
            print('\n**Unable to uninstall the webhook on:**\n', file=f)
            for repo in removed_failures:
                print(f'- {repo}', file=f)
