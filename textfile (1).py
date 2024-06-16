def copy_file(src_file, dest_file):
    try:
        with open(src_file, 'r') as src:
            with open(dest_file, 'w') as dest:
                dest.write(src.read())
        print(f"Copied contents from {src_file} to {dest_file}")
    except FileNotFoundError:
        print(f"Error: {src_file} not found!")
    except IOError:
        print(f"Error: Unable to read/write file!")

def main():
    src_file = input("Enter the source file name: ")
    dest_file = input("Enter the destination file name: ")
    copy_file(src_file, dest_file)

if __name__ == "__main__":
    main()