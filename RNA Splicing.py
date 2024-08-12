from itertools import chain
from Bio.Seq import Seq

dna = "/home/asik/rosalind_splc.fasta"

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

info = fastaParser(dna)
dna = "".join(str(element) for element in info[1][0])
introns = list(chain(*info[1][1:]))

for intron in introns:
    dna = dna.replace(intron, '')

def transcribe_DNA_to_RNA(text):
    for i in text:
        if i == 'T':
            text = text.replace('T', 'U')
    return text

rna = transcribe_DNA_to_RNA(dna)

rna_seq = Seq(str(rna))
print(rna_seq.translate())
