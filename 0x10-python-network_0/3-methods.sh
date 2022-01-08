#!/bin/bash
# Script to show all options available
curl -isX OPTIONS "$1" | grep "Allow:" | cut -d " "
