#!/bin/bash
# Script that sends a GET request with a custom header
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
