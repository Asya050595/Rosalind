from itertools import chain

with open('/home/asik/Загрузки/rosalind_ps.txt', 'r') as input_data:
    data = [line.strip().split() for line in input_data]
    data =[[int(x) for x in l] for l in data]
    k = data[-1]
    k = ', '.join(map(str, k)) # count of numbers that should be in the output
    data = data[1:-1]
    data = list(chain(*data))
    input_data.seek(0)
    lst1 = input_data.readline().split(' ')
    n = lst1[0] #size of array

sorted_lst = []
sorted_lst.extend(sorted(data))


print(*sorted_lst[:int(k)])
