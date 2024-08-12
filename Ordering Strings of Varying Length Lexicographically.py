import itertools

pum = input()
pumpum = pum.split(' ')

n = int(input())
my_lst = []

for i in range(1, n+1):
    my_lst.append(list(map("".join, itertools.product(pumpum, repeat=i))))

all_in_one_lst = list(itertools.chain(*my_lst))

print(*sorted(all_in_one_lst, key=lambda s:[pum.index(c) for c in s]), sep='\n')
