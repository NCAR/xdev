#!/usr/bin/env bash

if [ "${CIRCLE_BRANCH}" == "master" ]; then
    git config --global user.name 'CircleCI'
    git config --global user.email 'circleci@invalid'
    git pull --all
    git remote add deploy https://${GITHUB_TOKEN}@github.com/NCAR/xdev.git
    nikola github_deploy -m 'Nikola auto deploy [ci skip]'
    exitcode=$?
else
    exitcode=0
fi

exit $exitcode
