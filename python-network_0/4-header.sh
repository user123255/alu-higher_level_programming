#!/bin/bash
# Sends a GET request with a custom header X-School-User-Id: 98
curl -s -H "X-School-User-Id: 98" "$1"
