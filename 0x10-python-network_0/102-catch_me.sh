#!/bin/bash
# makes a PUT request
curl -s -X PUT -d "You got me!" -o "response.txt" 0.0.0.0:5000/catch_me
