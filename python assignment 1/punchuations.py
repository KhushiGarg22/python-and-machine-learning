import string

def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

s = input("Enter a string: ")
clean_s = remove_punctuation(s)

print("Original string:", s)
print("String without punctuation:", clean_s)