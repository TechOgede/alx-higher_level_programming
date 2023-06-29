#!/bin/bash
#Sends a custom header variable along with the GET request
curl -sL -H "X-School-User-Id: 98" "$!"
