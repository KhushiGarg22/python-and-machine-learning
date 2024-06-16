def find_min_max(numbers):
    return min(numbers), max(numbers)

numbers = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in numbers.split()]

min_val, max_val = find_min_max(numbers)

print(f"The minimum value is: {min_val}")
print(f"The maximum value is: {max_val}")