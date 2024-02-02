# Function to add two numbers
add() {
  local result=$(( $1 + $2 ))
  echo "Sum: $result"
}
