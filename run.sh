#! /bin/bash

cd /opt/twitter_project 

source twitter/bin/activate

python3 crawl/musical.py

deactivate 
