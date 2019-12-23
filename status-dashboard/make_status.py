#!/usr/bin/env python

import os
import sys

from jinja2 import Template
from yaml import safe_load as load

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'dashboard.yml')) as f:
    config = load(f)

existing = {
    project['repo'].split('/')[1].lower(): project
    for section in config
    for project in section['projects']
}

# Also get affiliated projects
registry = []
# for section in config:
#     if section['name'] == 'Affiliated projects':
#         affiliated = section
#         break
# else:
#     print("Could not find affiliated project section in dashboard.yml")
#     sys.exit(1)

for project in registry:
    # FIXME: Not all repo name is actual project name.
    pkg_name = project['name'].lower()

    if pkg_name in existing:
        entry = existing[pkg_name]
    else:
        entry = {}
    if 'repo' not in entry:
        if 'github.com' in project['repo_url']:
            entry['repo'] = project['repo_url'].split('github.com/')[1]
        else:
            print('Skipping project {0} which is not on GitHub'.format(project['name']))
    if 'pypi_name' not in entry:
        entry['pypi_name'] = project['pypi_name']
    if 'badges' not in entry:
        entry['badges'] = 'travis, coveralls, rtd, pypi, conda'
    # if pkg_name not in existing:
    #     affiliated['projects'].append(entry)

for section in config:
    for project in section['projects']:
        project['user'], project['name'] = project['repo'].split('/')
        project['badges'] = [x.strip() for x in project['badges'].split(',')]
        project['conda_project'] = project.get('conda_project', project['name'])
        if 'rtd' in project['badges'] and 'rtd_name' not in project:
            project['rtd_name'] = project['name']
        if 'pypi' in project['badges'] and 'pypi_name' not in project:
            project['pypi_name'] = project['name']
        if 'appveyor' in project['badges'] and 'appveyor_project' not in project:
            project['appveyor_project'] = project['repo']
        if 'circleci' in project['badges'] and 'circleci_project' not in project:
            project['circleci_project'] = project['repo']
        if 'travis' in project['badges']:
            if 'travis_project' not in project:
                project['travis_project'] = project['repo']
            project['travis_dot'] = project.get('travis_dot', 'org')
        if 'conda' in project['badges']:
            project['conda_channel'] = project.get('conda_channel', 'conda-forge')

        if 'githubci' in project['badges']:
            project['githubci'] = project['repo']
            project['gh_workflow_name'] = project.get('gh_workflow_name', 'CI')

# affiliated['projects'] = sorted(affiliated['projects'], key=lambda x: x['name'].lower())

template = Template(open(os.path.join(here, 'template.html'), 'r').read())


with open(os.path.join(here, '../site/pages/status.html'), 'w') as f:
    f.write(template.render(config=config))
