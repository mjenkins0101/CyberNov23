secret_number = 105
user_guess = int(input("Guess the secret number: "))
while user_guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_guess = int(input("Try again: "))
print("Well done, muggle! You are free now.")
