numbers = input()
result = 0

my_dict = {1: 2.0, 2: 2.0, 3: 2.0, 4: 1.5, 5: 2.0, 6: 0, 0: 0}

puf = numbers.split(' ')
puf = [eval(i) for i in puf]

if puf[0] > 0:
    result += 2.0 * puf[0]
elif puf[0] == 0:
    result += 0

if puf[1] > 0:
    result += 2.0 * puf[1]
elif puf[1] == 0:
    result += 0

if puf[2] > 0:
    result += 2.0 * puf[2]
elif puf[2] == 0:
    result += 0

if puf[3] > 0:
    result += 1.5 * puf[3]
elif puf[3] == 0:
    result += 0

if puf[4] > 0:
    result += 1.0 * puf[4]
elif puf[4] == 0:
    result += 0

if puf[5] > 0:
    result += 0
elif puf[5] == 0:
    result += 0

print(result)
