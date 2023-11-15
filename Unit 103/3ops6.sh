#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.


    echo "googl.com: "
    read domain

    # Run whois
    whois $domain > $domain.txt

    # Run dig
    echo -e "\n### DIG ###" >> $domain.txt
    dig $domain >> $domain.txt

    # Run host
    echo -e "\n### HOST ###" >> $domain.txt
    host $domain >> $domain.txt

    # Run nslookup
    echo -e "\n### NSLOOKUP ###" >> $domain.txt
    nslookup $domain >> $domain.txt

    echo "Results saved to $domain.txt"
    # Open the file with the default text editor
    xdg-open $domain.txt
