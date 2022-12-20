#!/bin/bash
# HTTP methods the server will accept.
curl -Is "$1" | grep "Allow:" | cut -f2 -d' '
