#!/bin/bash
#Sends a POST request to the URL and displays the response body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
