from  collections import defaultdict
from itertools import chain

def fastaParser(infile):
    sequences = []
    headers = []
    with open(infile) as f:
        sequence = ""
        header = None
        for line in f:
            if line.startswith('>'):
                headers.append(line[1:-1])
                if header:
                    sequences.append([sequence])
                sequence = ""
                header = line[1:]
            else:
                sequence += line.rstrip()
        sequences.append([sequence])
    return headers, sequences

headers, sequences = fastaParser('/home/asik/Документы/1.fasta')
sequences = list(chain.from_iterable(sequences))
consensus = []

max_len = max(map(len, sequences))
d = defaultdict(lambda: [0]*max_len)
for seq in sequences:
    for i, char in enumerate(seq):
        d[char][i] += 1

A = d['A']
C = d['C']
G = d['G']
T = d['T']

def consensus(a, c, t, g):
    consensus = ''
    for k in range(len(a)):
        if (a[k] > t[k]) and (a[k] > c[k]) and (a[k] > g[k]):
            consensus = consensus + "A"
        elif (t[k] > a[k]) and (t[k] > c[k]) and (t[k] > g[k]):
            consensus = consensus + 'T'
        elif (c[k] > t[k]) and (c[k] > a[k]) and (c[k] > g[k]):
            consensus = consensus + 'C'
        elif (g[k] > t[k]) and (g[k] > c[k]) and (g[k] > a[k]):
            consensus = consensus + 'G'
        else:
            if max(a[k], c[k], t[k], g[k]) in a:
                consensus = consensus + 'A'
            elif max(a[k], c[k], t[k], g[k]) in c:
                consensus = consensus + 'C'
            elif max(a[k], c[k], t[k], g[k]) in t:
                consensus = consensus + 'T'
            elif max(a[k], c[k], t[k], g[k]) in g:
                consensus = consensus + 'G'
    return consensus



print(consensus(A, C, T, G))
print('A:', *d['A'])
print('C:', *d['C'])
print('G:', *d['G'])
print('T:', *d['T'])
