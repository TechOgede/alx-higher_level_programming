#!/bin/bash
#Display Status code alone
curl -sIw "%{http_code}\n" -o /dev/null "$1"
