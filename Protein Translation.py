from Bio.Seq import translate

dna = input()
protein = input()

def genetic_code(dna, protein):
    result = []
    table_ids = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]
    for i in table_ids:
        if translate(dna, table=i, to_stop=True) == protein:
            result.append(i)
    return result

print(genetic_code(dna, protein))
