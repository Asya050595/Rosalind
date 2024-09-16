with open('/home/asik/Загрузки/1.txt', 'r') as input_data:
    data = [line.strip().split() for line in input_data]
    data = [[int(x) for x in l] for l in data]
    data = data[1:]
    input_data.seek(0)
    lst = input_data.readline().split(' ')
    k = lst[0] #number of arrays
    n = lst[1] #size of an array

for i in range(int(k)):
    counter = [data[i].count(data[i][j]) > int(n) / 2 for j in range(int(n))]
    if any(counter):
        print(data[i][counter.index(True)], end=" ")
    else:
        print("-1", end=" ")
