#!/bin/bash

# Read three integers as input
read -p "Enter the length of side 1: " side1
read -p "Enter the length of side 2: " side2
read -p "Enter the length of side 3: " side3

# Check if the triangle is equilateral
if [ $side1 -eq $side2 ] && [ $side2 -eq $side3 ]; then
    echo "EQUILATERAL"
elif [ $side1 -eq $side2 ] || [ $side1 -eq $side3 ] || [ $side2 -eq $side3 ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
 