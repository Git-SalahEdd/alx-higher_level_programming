#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sX POST $1 -d email=test@gmail.com -d subject=I%20will%20always%20be%20here%20for%20PLD
