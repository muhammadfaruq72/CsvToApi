#!/usr/bin/env bash


sudo systemctl start elasticsearch.service
sudo systemctl start kibana.service

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )

echo $DIR




cd $DIR
sudo lsof -t -i tcp:8000 | xargs kill -9
pip install -r requirements.txt
start http://127.0.0.1:8000/
python FastApi_GET.py > uvicorn.log
$SHELL