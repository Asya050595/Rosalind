a = int(input())
b = int(input())
count = 0

for i in range(a, b + 1):
    if a < b < 10000 and i % 2 == 1:
        count += i

print(count)
