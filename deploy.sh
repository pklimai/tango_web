#!/bin/bash

if [ "$(git pull)" == "Already up-to-date." ] ; then
  echo "No updates"
else
  docker-compose down
  docker rmi bmn-tango_tango-web
  docker-compose up -d
fi
