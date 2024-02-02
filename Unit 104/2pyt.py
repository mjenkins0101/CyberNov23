#1
'''
My name is Marquel
Seafood is my favorite food,
Dream job: Cybersecurity Defense Analyst
'''
#2
integer_var = 34
float_var = 3.14
boolean_var = True
string_var = "Hello, World!"
list_var = [1, 2, 3]

#3
print(len(string_var))

#4 
savvy = "Savvy Coder is Amazing!"
savvy = savvy.replace("Amazing", "great")

#5 
name, age, length = "Marquel", 34, 235

#6 
miniBio = f"Hi, my name is {name}, I am {length} cm tall, and {age} years old today."
print(miniBio)

#7 
mixed_list = [42, "apple", True, 3.14, [1, 2, 3]]

#8 
mixed_list[1] = "banana"

#9 Append or insert several more items to the list
# mixed_list.append("orange")
mixed_list.insert(2, False)

# Find and print the length of the list
print("Length of mixed_list:", len(mixed_list))

# Slice a sub-section of the 1st list and save it to a different 2nd list
second_list = mixed_list[1:4]

# Print the 2nd list
print("Second list:", second_list)

# Extend the original list with the 2nd list
mixed_list.extend(second_list)

# Create a new list called "simList"
simList = [5, 2, 8, 1, 3]

# Sort "simList" and print the list
simList.sort()
print("Sorted simList:", simList)

# Copy the "simList" list to another 3rd list
third_list = simList.copy()

# Add the 2nd and 3rd lists together into a 4th list
fourth_list = second_list + third_list
print("Combined 2nd and 3rd lists:", fourth_list)
