n = int(input())
m = int(input())
a = input().split(' ')
a = [int(i) for i in a]
keys = input().split(' ')
keys = [int(i) for i in keys]
answers = []

for i in keys:
    if i in a:
        answers.append(a.index(i) + 1)
    elif i not in a:
        answers.append(-1)

print(*answers)
