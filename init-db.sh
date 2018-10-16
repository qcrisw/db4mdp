#!/bin/bash
set -e

# config db
bin=/usr/lib/postgresql/9.6/bin
data=/tmp/pgdata
socket=/tmp

# init db
[ -d $data ] && rm -fr $data
mkdir $data
chown postgres $data
su postgres -c "$bin/initdb -D $data -E UTF8"

# start db
su postgres -c "$bin/pg_ctl -D $data -o \"-k $socket -N5 -c listen_addresses='' -p 5555\" -w start"

# client should use the following connection parameters
# options = {
#   adapter: 'postgresql',
#   encoding: 'unicode',
#   username: 'postgres',
#   database: 'postgres',
#   host: '/tmp',
#   port: 5555
# }