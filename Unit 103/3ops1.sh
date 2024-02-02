#!/bin/bash

# Script: Ops 201 Class 01 Ops Challenge Solution
# Author: Marquel Jenkins
# Date of latest revision: 6 Nov 2023 
# Purpose: Print a string to the terminal

echo "enter a website"
read website
whois $website >> whois.txt
dig $website >> whois.txt
host $website >> whois.txt
nslookup >> whois.txt