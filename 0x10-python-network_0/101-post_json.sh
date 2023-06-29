#!/bin/bash
#Sends a POST request to a URL using data stored in a file
curl -s --json @"$2" "$1"
