#!/bin/bash

# Function to add two numbers
add() {
  local result=$(( $1 + $2 ))
  echo "Sum: $result"
}

# Function to subtract two numbers
subtract() {
  local result=$(( $1 - $2 ))
  echo "Difference: $result"
}

# Function to multiply two numbers
multiply() {
  local result=$(( $1 * $2 ))
  echo "Product: $result"
}

# Function to divide two numbers
divide() {
  if [ $2 -eq 0 ]; then
    echo "Error: Cannot divide by zero."
  else
    local result=$(awk "BEGIN {printf \"%.2f\", $1 / $2}")
    echo "Quotient: $result"
  fi
}

# Get user input
read -p "Enter the first number: " num1
read -p "Enter the second number: " num2

# Choose operation
echo "Select operation:"
echo "1. Add"
echo "2. Subtract"
echo "3. Multiply"
echo "4. Divide"
read -p "Enter choice (1/2/3/4): " choice

# Perform the chosen operation
case $choice in
  1) add $num1 $num2 ;;
  2) subtract $num1 $num2 ;;
  3) multiply $num1 $num2 ;;
  4) divide $num1 $num2 ;;
  *) echo "Invalid choice";;
esac
