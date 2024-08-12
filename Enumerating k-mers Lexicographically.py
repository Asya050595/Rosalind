import itertools

pum = input()
pumpum = pum.split(' ')

n = int(input())

print(*[*map("".join, itertools.product(pumpum, repeat=n))], sep='\n')
