yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to test your fate?\nyes/no\n")
    if response == "yes":
        print("You head into the void. You hear a strange nosie in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
while response not in directions:
    response = input("Which direction do you hear the noise from? Choose wisely.\nleft/right/forward/backward\n")     
    if response == "right":
        print("Instant Death. Start Over.\n")
    if response == "left":
        print("Death Loop. Start Over\n")       
    if response == "forward":
        print("You won one billion in Gold and Thanos Armor.")
        loot = input("Do you want these items?\nyes/no\n")
        if loot == "yes":
            print("You discover a portal home. Congrats")
        else:
            print("You decide to leave the chest untouched.")
    elif response == "backward":
        print("Thank you for playing, " + name + ", have a good night.\n")

