#!/bin/bash
# GETs request and displays response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
