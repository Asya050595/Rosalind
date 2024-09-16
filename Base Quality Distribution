from Bio import SeqIO

n = int(input())
counter = 0
phred_lst = []

for record in SeqIO.parse(open('/home/asik/test.fastq'), "fastq"):
    phred_score_results = record.letter_annotations["phred_quality"]
    phred_lst.append(phred_score_results)

for i in range(len(phred_lst[0])):
    if sum(j[i] for j in phred_lst) / len(phred_lst) < n:
        counter += 1


print(counter)
