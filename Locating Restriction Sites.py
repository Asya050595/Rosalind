dna = input()

def complement(seq):
  if seq == 'A': return 'T'
  if seq == 'T': return 'A'
  if seq == 'C': return 'G'
  if seq == 'G': return 'C'
  return seq

reverse_strand = ''.join(map(complement, reversed(dna)))
reverse_strand = reverse_strand[::-1]

for i in range(len(dna)):
    for j in range(i, len(reverse_strand)):
        k = dna[i:j + 1]
        n = reverse_strand[i:j + 1]
        if len(k) >= 4 and len(k) <=12:
            if k == n[::-1]:
                print(i + 1, len(k))
