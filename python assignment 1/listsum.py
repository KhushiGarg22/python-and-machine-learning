def sum_numbers(numbers):
    return sum(numbers)

numbers = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in numbers.split()]

result = sum_numbers(numbers)

print("The sum of the numbers is:", result)