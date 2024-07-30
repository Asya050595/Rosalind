s = input()
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if len(s) <= 200:
    print(s[a:b+1], s[c:d+1], sep=' ')
