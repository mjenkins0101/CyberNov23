#!/bin/bash

# Read an integer as input
read -p "Enter a number: " userNumber

# Check if the input number is between 2 and 5
if [ $userNumber -ge 2 ] && [ $userNumber -le 5 ]; then
    echo "Valid Number"
    echo "Your number is $userNumber"
else
    echo "Not valid!"
fi
