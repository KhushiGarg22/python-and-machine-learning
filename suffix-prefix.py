def check_string_prefix_suffix(string, prefix, suffix):
    if string.startswith(prefix):
        print(f"'{string}' starts with '{prefix}'")
    else:
        print(f"'{string}' does not start with '{prefix}'")

    if string.endswith(suffix):
        print(f"'{string}' ends with '{suffix}'")
    else:
        print(f"'{string}' does not end with '{suffix}'")

def main():
    string = input("Enter a string: ")
    prefix = input("Enter a prefix: ")
    suffix = input("Enter a suffix: ")
    check_string_prefix_suffix(string, prefix, suffix)

if __name__ == "__main__":
    main()