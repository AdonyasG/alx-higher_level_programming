#!/bin/bash
# displays the status code
curl -o /dev/null -w '%{http_code}' -sLI "$1"
