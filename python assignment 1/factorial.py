print("to check the factorial of an number")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("enter a number to check its factorial"))
result = factorial(number)
print(f"The factorial of {number} is {result}.")