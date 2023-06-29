#!/bin/bash
#Sends a POST request to a URL using data stored in a file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
