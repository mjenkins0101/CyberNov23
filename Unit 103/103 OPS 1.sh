#!/bin/bash

# Script: Ops 201 Class 01 Ops Challenge Solution
# Author: 
# Date of latest revision: 
# Purpose: Print a string to the terminal

echo "enter a website"
read website
whois $website >> whois.txt
dig $website >> whois.txt
host $website >> whois.txt
nslookup >> whois.txt