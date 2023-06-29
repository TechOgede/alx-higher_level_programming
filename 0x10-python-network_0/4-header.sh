#!/bin/bash
#Sends a custom header variable along with the GET request
curl -s -H "X-School-User-Id: 98" "$1"
