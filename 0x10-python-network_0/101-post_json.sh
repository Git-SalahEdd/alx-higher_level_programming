#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
cat $2 | curl -sX POST -H "Content-Type: application/json" -d @- $1
