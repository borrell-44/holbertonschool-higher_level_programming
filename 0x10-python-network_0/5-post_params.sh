#!/bin/bash                                                                                                                                                                               
# Sends a POST request to the given URL and display body of the response                                                                                                                  
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -L -X POST "$1" 
