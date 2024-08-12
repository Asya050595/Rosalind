s = input()

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

pum = word_count(s)

for key, value in pum.items():
    print(key, value)
