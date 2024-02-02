for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


inventory = []

# ... (your existing code)

while response not in directions:
    response = input("Which direction do you hear the noise from? Choose wisely.\nleft\nright\nforward\nbackward")

    if response == "right":
        print("Instant Death.\n")
    elif response == "left":
        print("Death Loop.\n")
    elif response == "forward":
        print("You find a treasure chest!")
        loot = input("Do you want to open it?\nyes/no\n")
        if loot == "yes":
            print("You discover a magical amulet.")
            inventory.append("Magical Amulet")
        else:
            print("You decide to leave the chest untouched.")
    elif response == "backward":
        print("Thank you for playing, " + name + ", have a good night.\n")

# ... (continue the game with more features based on player's inventory)
