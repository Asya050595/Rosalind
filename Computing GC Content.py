from Bio import SeqIO

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def GC_counter(seq): #doesn't work for some reason =(
    gc_total = 0
    total = len(seq)
    for i in seq:
        if i == 'G' or i == 'C':
            gc_total += 1
    gc_content = gc_total / float(total) * 100
    return gc_content

with open('/home/asik/gc.txt') as f:
    for seq in SeqIO.parse(f, "fasta"):
        gc_total = 0
        total = len(seq)
        for i in seq:
            if i == 'G' or i == 'C':
                gc_total += 1
        gc_content = gc_total / float(total) * 100
        spisok = f"{seq.id}: {gc_content:}"
        
for gc_content in spisok:
    print(max(gc_content), end = "")
