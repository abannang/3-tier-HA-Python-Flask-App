#!/bin/bash

set -e

sudo mkdir /opt/oracle
sudo unzip instantclient-basic-linux.x64-12.2.0.1.0.zip -d /opt/oracle/
sudo ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1 libclntsh.so
sudo ln -s /opt/oracle/instantclient_12_2/libocci.so.12.1 libocci.so
sudo apt-get install libaio1
sudo sh -c "echo /opt/oracle/instantclient_12_2 > \
      /etc/ld.so.conf.d/oracle-instantclient.conf"
sudo ldconfig
