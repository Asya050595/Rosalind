from Bio.Seq import Seq

rna = input()
rna_seq = Seq(str(rna))
print(rna_seq.translate())

