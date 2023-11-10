#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables


x=18
y=5
answer=$(echo $(( x * y )))
echo "$x multiplied by $y is : $answer"

answer=$(echo $(( x + y )))
echo "The sum of $x and $y is : $answer"

answer=$(echo $(( x - y )))
echo "$x minus $y is : $answer"

answer=$(echo $(( x / y )))
echo "$x divided by $y is : $answer"

