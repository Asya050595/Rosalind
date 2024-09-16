from itertools import product, permutations

n = int(input())
all_combination = []

for i in permutations(list(range(1, n+1))):
    for j in product([-1, 1], repeat=len(list(range(1, n + 1)))):
        p = [a * sign for a, sign in zip(i, j)]
        all_combination.append(p)


print(len(all_combination))

for item in all_combination:
  print(item[0], ' '.join(map(str, item[1:])))
