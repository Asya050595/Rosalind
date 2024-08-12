from Bio import SeqIO

for record in SeqIO.parse(open('/home/asik/test.fastq', "rU"), "fastq"):
    print('>', record.id, sep='')
    print(record.seq)
