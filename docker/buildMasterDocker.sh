#!/bin/bash
docker build -f ./Dockerfile-master . -t registry.cmic.site:5000/sg/honeypot-master:latest
docker push registry.cmic.site:5000/sg/honeypot-master:latest
