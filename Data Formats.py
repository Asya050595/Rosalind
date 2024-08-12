from Bio import Entrez
from Bio import SeqIO

Entrez.email = "araksya.arutyunova@yandex.ru"
handle = Entrez.efetch(db="nucleotide", id=["JX393321 BT149867 NM_001133698 NM_001270868 FJ817486 JX569368 NM_001159758 BT149866 NM_204821 NM_001251956"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

shortest_string = min(records, key=len)

print(shortest_string)
print(shortest_string.seq)

