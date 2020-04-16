#!/bin/bash
docker build -f ./Dockerfile . -t honeypot-agent:1.0
#docker push honeypot-agent:test