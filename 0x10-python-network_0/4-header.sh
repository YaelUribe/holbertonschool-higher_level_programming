#!/bin/bash
# Script to send GET request and display the body of response
curl -sX GET -H "X-School-User-Id: 98" "$1"
