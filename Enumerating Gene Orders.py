import itertools

n = int(input())
numbers = []

for i in range(1, n + 1):
    numbers.append(i)

print(len(list(itertools.permutations(numbers))))

for i in list(itertools.permutations(numbers)):
    print(*i, end = '\n')

