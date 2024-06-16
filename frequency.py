def count_char_frequency(s):
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

s = input("Enter a string: ")
char_frequency = count_char_frequency(s)

print("Character Frequency:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")