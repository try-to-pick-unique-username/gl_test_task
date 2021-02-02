#!/usr/bin/env bash

BASEDIR=$(pwd)
ALLUREDIR=$BASEDIR/reports

pytest -v --alluredir=$ALLUREDIR
allure serve $ALLUREDIR