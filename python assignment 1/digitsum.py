def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

num = int(input("Enter a number: "))
print("The sum of the digits of", num, "is:", sum_of_digits(num))