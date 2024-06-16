def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print("The first", n, "Fibonacci numbers are:", fibonacci(n))