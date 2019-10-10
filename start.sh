#!/bin/bash
cd "$(dirname "$0")" || exit
pipenv install
pipenv run python -m server.main