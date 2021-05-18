# input the DNA sequence
seq='ATGCGACTACGATCGAGGGCC'
# import the genetic_code
genetic_code = {
    'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
    'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
    'TTA': 'L', 'TCA': 'S', 'TAA': 'O', 'TGA': 'X',
    'TTG': 'L', 'TCG': 'S', 'TAG': 'U', 'TGG': 'W',
    'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
    'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
    'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
    'CTG': 'L', 'CCG': 'P', 'CAG': 'Z', 'CGG': 'R',
    'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
    'ATC': 'I', 'ACC': 'T', 'AAC': 'B', 'AGC': 'S',
    'ATA': 'J', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
    'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
    'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
    'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
    'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'A',
    'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}

protein = []
for i in range(0, len(seq), 3):      # step is 3, because a codon is made up of three base pairs.
    codon = seq[i:i+3:1]          # When we read it, we should go through 3 base pairs at one go.Step is 1 so we can go through all the base pairs
    protein.append(genetic_code[codon])    # translate
print(protein)     # output the protein

