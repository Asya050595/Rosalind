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

headers, seqs = fastaParser('/home/asik/sampledata.fasta')

dna = seqs[0]
dna = "".join(dna)
motif = seqs[1]
motif = ''.join(motif)

indexes = []
num = 0

for i in range(len(motif)):
    for j in range(num, len(dna)):
        num += 1
        if len(indexes) < len(motif):
            if motif[i] == dna[j]:
                indexes.append(num)
                break
print(motif)
print(len(motif))
print(*sorted(indexes), sep = ' ')
