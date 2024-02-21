from Bio.SeqUtils import molecular_weight

protein = input()
print(f"Monoisotopic mass: {molecular_weight(protein, 'protein', monoisotopic=True)}")
