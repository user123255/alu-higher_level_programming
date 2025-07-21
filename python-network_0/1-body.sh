#!/bin/bash
# Script to display body only for 200 OK response
curl -sL -w "%{http_code}" "$1" | { read body; code=${body: -3}; [ "$code" = "200" ] && echo "${body::-3}"; }
