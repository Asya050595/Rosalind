from itertools import chain

with open('/home/asik/Загрузки/rosalind_hs.txt', 'r') as input_data:
    data = [line.strip().split() for line in input_data]
    data =[[int(x) for x in l] for l in data]
    data = list(chain(*data))
    data = data[1:]
    input_data.seek(0)
    lst = input_data.readline().split(' ')
    n = lst[0] #size of array

def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < N and arr[l] > arr[largest]:
        largest = l
    if r < N and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)

def buildHeap(arr, N):
    startIdx = N // 2 - 1
    for i in range(startIdx, -1, -1):
        heapify(arr, N, i)


buildHeap(data, int(n))
print(*sorted(data))

