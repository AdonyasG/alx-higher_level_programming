#!/bin/bash
# displays the status code
curl -o -sLI /dev/null -w '%{http_code}' "$1"
