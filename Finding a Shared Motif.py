from suffix_trees import STree
import functools

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

headers, seqs = fastaParser('/home/asik/rosalind_lcsm.fasta')

sequences = functools.reduce(lambda x, y: x + y, seqs, [])
shared_motif = STree.STree(sequences)
print(shared_motif.lcs())


