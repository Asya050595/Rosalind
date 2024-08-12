import Bio
from Bio.Seq import Seq
text = input()
text = Seq(text)

print(text.reverse_complement())

# !Different approach below!

import Bio
import itertools
from Bio.Seq import Seq
from itertools import chain

fasta = "/home/asik/test.fasta"

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

headers, seqs = fastaParser(fasta)

all_strands = list(chain(*seqs))
reverse_complement_strands = []
counter = 0
for i in all_strands:
    reverse_complement_strands.append(Seq(i).reverse_complement())
    for j in reverse_complement_strands:
        if Seq(i) == Seq(j):
            counter += 1
print(counter)
