#!/bin/bash
# Display all HTTP methods that the server will accept of the given URL                                                                                                                   
curl -i -s -L -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2- 
