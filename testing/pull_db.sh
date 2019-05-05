#!/usr/bin/env bash
mkdir -p ./db/init/mysql
rm -rf ./db/init/mysql/*
scp mipt@vm221-52.jinr.ru:/home/mipt/mysql/*.sql ./db/init/mysql/
mkdir -p ./db/init/postgres
rm -rf ./db/init/postgres/*
scp mipt@vm221-52.jinr.ru:/home/mipt/postgres/*.sql ./db/init/postgres/