from Bio import SeqIO

n = int(input())
counter = 0

for record in SeqIO.parse(open('/home/asik/test.fastq'), "fastq"):
    phred_score_results = record.letter_annotations["phred_quality"]
    average_quality = sum(phred_score_results) / len(phred_score_results)
    if average_quality < n:
        counter += 1


print(counter)
