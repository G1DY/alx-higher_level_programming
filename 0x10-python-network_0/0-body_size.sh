#!/bin/bash
# send a request and gets bytes size of a response header
curl -s "$1" | wc -c
