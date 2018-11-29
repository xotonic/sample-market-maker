#!/bin/bash

rm -rd sandbox

sudo pip3 install -e . && \
  mkdir sandbox && cd sandbox && \
  marketmaker setup && marketmaker

