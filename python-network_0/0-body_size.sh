#!/bin/bash
# Script to display body size of response
curl -s "$1" | wc -c
