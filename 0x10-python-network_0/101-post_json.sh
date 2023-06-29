#!/bin/bash
#Sends a POST request to a URL using data stored in a file
curl -s -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"

