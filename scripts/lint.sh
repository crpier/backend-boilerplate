#!/usr/bin/env bash

set -x

status=0
mypy app
if [ "$?" == "0" ];then 
  status=1
fi
black app --check
if [ "$?" == "0" ];then 
  status=1
fi
flake8 app
if [ "$?" == "0" ];then 
  status=1
fi
isort --check-only app
if [ "$?" == "0" ];then 
  status=1
fi
exit $status
