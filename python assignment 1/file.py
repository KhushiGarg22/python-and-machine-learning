# Get the user's input
user_input = input("Enter a string: ")

# Open a text file in write mode
with open("user_input.txt", "w") as file:
    # Write the user's input to the file
    file.write(user_input)

print("Your input has been written to user_input.txt")