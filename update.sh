#!/bin/bash
set -e
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential -y
sudo pip install -r ~/3-tier-HA-Python-Flask-App/requirements.txt
sudo apt-get install unzip -y
