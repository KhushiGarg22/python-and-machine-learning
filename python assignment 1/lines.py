lines = []

while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)