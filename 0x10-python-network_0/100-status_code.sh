#!/bin/bash
#Display Status code alone
curl -sIw "%{http_code}" -o /dev/null "$1"
