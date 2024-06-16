# Get the main string and the substring to search for
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

# Check if the substring is present in the main string
if substring in main_string:
    print("The substring is present in the main string.")
else:
    print("The substring is not present in the main string.")