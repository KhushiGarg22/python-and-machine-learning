# Open the text file in read mode
with open("user_input.txt", "r") as file:
    # Read the entire file content
    content = file.read()

# Print the file content to the console
print(content)