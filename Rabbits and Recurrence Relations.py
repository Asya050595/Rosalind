def fibonacci(n, k):
    a = 1
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n-1):
            c = a*k + b
            a = b
            b = c
        return c

print(fibonacci(5, 3))

