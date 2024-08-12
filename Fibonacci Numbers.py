a, b = 1, 1

n = int(input())

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
