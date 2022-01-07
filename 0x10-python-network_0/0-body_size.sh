#!/bin/bash
# script for displaying size in bytes
curl -s "$1" | wc -c
