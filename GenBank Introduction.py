from Bio import Entrez

genus = input()
date1 = input()
date2 = input()
Entrez.email = "araksya.arutyunova@yandex.ru"
handle = Entrez.esearch(db="nucleotide", term=genus+'[ORGN]', mindate=date1, maxdate=date2, datetype='pdat')
record = Entrez.read(handle)
print(record["Count"])
