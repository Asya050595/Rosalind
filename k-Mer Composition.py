import itertools
from itertools import chain

def fastaParser(infile):
    seqs = []
    headers = []
    with open(infile) as f:
        sequence = ""
        header = None
        for line in f:
            if line.startswith('>'):
                headers.append(line[1:-1])
                if header:
                    seqs.append([sequence])
                sequence = ""
                header = line[1:]
            else:
                sequence += line.rstrip()
        seqs.append([sequence])
    return headers, seqs

headers, seqs = fastaParser('/home/asik/1.fasta')
sequence = list(chain.from_iterable(seqs))

nucleotides = ['A', 'T', 'G', 'C']
kmers = list(itertools.product(nucleotides, repeat=4))

newkmers = sorted(list((''.join(w) for w in kmers)))
freqs = []

def function(string, str_to_search_for):
    count = 0
    for x in range(len(string) - len(str_to_search_for) + 1):
        if string[x:x + len(str_to_search_for)] == str_to_search_for:
            count += 1
    return count

for i in newkmers:
    freqs.append(function(sequence[0], i))

print(*freqs)
