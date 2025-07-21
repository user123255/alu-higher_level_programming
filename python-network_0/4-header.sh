#!/bin/bash
# Sends a GET request to the URL with a header X-School-User-Id: 98
curl -sH "X-School-User-Id: 98" "$1"
