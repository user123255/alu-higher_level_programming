#!/bin/bash
curl -sL -w "%{http_code}" "$1" -o temp_body && [ "$(tail -c 3 temp_body)" = "200" ] && head -c -3 temp_body
