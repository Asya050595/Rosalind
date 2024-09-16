n = int(input())
lst = input().split(' ')
lst = [int(i) for i in lst]
counter = 0

def insertionsort(array):
    swapsmade = 0
    checksmade = 0
    for f in range(len(array)):
        value = array[f]
        valueindex = f
        checksmade += 1
        # moving the value
        while valueindex > 0 and value < array[valueindex-1]:
            array[valueindex] = array[valueindex-1]
            valueindex -= 1
            checksmade += 1
            swapsmade += 1 #  Move inside the while loop
        array[valueindex] = value
    print(array)
    swapsnchecks = "{} swaps were made. {} checks were made.".format(swapsmade, checksmade)
    return swapsnchecks

print(insertionsort(lst))
