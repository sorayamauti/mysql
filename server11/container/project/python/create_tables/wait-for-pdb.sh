#!/bin/bash
# wait-for-postgres.sh
set -e
host="$1"
shift
cmd="$@"
#MySQLコンテナに接続できるまで繰り返す
until CMD_MYSQL="mysql -u user -h mysql -ppass db"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"
exec $cmd