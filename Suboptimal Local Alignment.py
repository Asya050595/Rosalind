#!!! NOT MINE !!!#
!code source -- https://github.com/erexhepa/Rosalind/blob/master/Armory_014_SUBO.py

def hamming_dist(string1, string2):
    ''' Calculate Hamming Distance between strings
    :param string1: string 1 (string)
    :param string2: string 2 (string)
    :return: the hamming distance bw/ string1 and string2 (integer)
    '''
    return sum([x != y for x, y in zip(string1, string2)])


from Bio import SeqIO

# Read the input data.
with open('/home/asik/1.txt') as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# Run LALIGN with +4/-8 Matrix, -8 Gap Open/Extend, and pick the 100% match.
r = 'GAGTTAGCAGGCTCTTCGTGTGAAAAATGTCCGG'

# Count the number of occurences in each sequence.
count = [sum([hamming_dist(dna[seq_num][i:i+len(r)], r) <= 3 for i in range(len(dna[seq_num]) - len(r) + 1)]) for seq_num in range(2)]

# Print and save the answer.
print(' '.join(map(str, count)))
with open('/home/asik/ans.txt', 'w') as output_data:
    output_data.write(' '.join(map(str, count)))
