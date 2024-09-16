from math import log10

s = input()
n = input()
lst = [float(x) for x in n.split(' ')]

def probability_GC(s, n):
    probs_nucleotide = {"G": log10(n / 2), "C": log10(n / 2),
                        "A": log10((1 - n) / 2), "T": log10((1 - n) / 2)}
    prob_log = 0
    for i in s:
        prob_log += probs_nucleotide[i]
    return prob_log

lst2 = []

for j in lst:
    lst2.append(probability_GC(s, j))

print(*lst2)
