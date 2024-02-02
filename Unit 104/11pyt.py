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
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
response = ""
while response not in directions:
    response = input("Which Direction do you hear the noise from? Choose Wisely?\nleft\nright\nforward\nbackward")     
    if response == "Right":
        print("Instant Death.\n")
    if response == "Left":
        print("Death Loop.\n")       
    if response == "Forward":
        print("You win one billion in Gold and Thanos Armor.\n")
    if response == "Backword":
        print("Thank You for playing, " + name + " , have a goodnight.\n")        