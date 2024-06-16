def string_to_list(s):
    return list(s)

def main():
    s = input("Enter a string: ")
    char_list = string_to_list(s)
    print(f"The list of characters is: {char_list}")

if __name__ == "__main__":
    main()