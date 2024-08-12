def transitions_transversions_ratio(text1, text2):
    transition = 0
    transvertion = 0
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == 'A' and text2[j] == 'G'  and i == j:
                transition += 1
            elif text1[i] == 'G' and text2[j] == 'A'  and i == j:
                transition += 1
            elif text1[i] == 'C' and text2[j] == 'T'  and i == j:
                transition += 1
            elif text1[i] == 'T' and text2[j] == 'C' and i == j:
                transition += 1
            elif text1[i] == 'A' and text2[j] == 'C'  and i == j:
                transvertion += 1
            elif text1[i] == 'C' and text2[j] == 'A' and i == j:
                transvertion += 1
            elif text1[i] == 'G' and text2[j] == 'T' and i == j:
                transvertion += 1
            elif text1[i] == 'T' and text2[j] == 'G' and i == j:
                transvertion += 1
            elif text1[i] == 'G' and text2[j] == 'C' and i == j:
                transvertion += 1
            elif text1[i] == 'C' and text2[j] == 'G' and i == j:
                transvertion += 1
            elif text1[i] == 'A' and text2[j] == 'T' and i == j:
                transvertion += 1
            elif text1[i] == 'T' and text2[j] == 'A' and i == j:
                transvertion += 1
    return transition / transvertion

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

sequences = fastaParser('/home/asik/rosalind_tran.fasta')
text1 = ''.join(str(element) for element in sequences[1][0])
text2 = ''.join(str(element) for element in sequences[1][1])
print(transitions_transversions_ratio(text1, text2))
