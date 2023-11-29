#!/bin/bash

echo "How is your day today? (Enter 'good' or 'bad'):"
read response

case "$response" in
  "good"|"Good"|"GOOD")
    echo "That's great to hear! Keep it up!"
    ;;
  "bad"|"Bad"|"BAD")
    echo "I'm sorry to hear that. Tomorrow is a new day!"
    ;;
  *)
    echo "Invalid response. Please enter 'good' or 'bad'."
    ;;
esac