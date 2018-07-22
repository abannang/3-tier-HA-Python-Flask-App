#!/bin/bash

set -e

sudo apt-get install firewalld -y
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload