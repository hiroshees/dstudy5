#!/bin/sh
# ファイルを1行ずつ読み込んで表示

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE:-$0}")"; pwd)"
ENVFILE=$SCRIPT_DIR/../.env_heroku
while read line; do
    if [[ $line != \#* ]] && [ -n "$line" ]; then
        heroku config:set $line
    fi
done < $ENVFILE

