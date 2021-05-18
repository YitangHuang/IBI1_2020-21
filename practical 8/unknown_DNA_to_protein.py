


 # This task is every similar to the get_unknown_function.py, the only thing is to replace the dna sequence with protein sequence.

import os
os.chdir("E:/github repo/IBI1_2020-21/practical 8")
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


protein = ''
seq_name = []
DNA_sequence = ''
protein_sequence = ''
all_DNA_list = []
all_protein_list = []     #  very similar steps to the previous task

filename = input("Please input the file name: ")      # let the user input a file name, and the name is unknown_function.fa
f1 = open(filename)  # the file name is unknown_function.fa
line = f1.readlines()         # use the same idea to get the dna sequence
for i in range(len(line)):
    if line[i].startswith('>'):
        seq_name.append(line[i].split(' ')[0])
        for j in range(i + 1, len(line)):
            if line[j].startswith('>'):
                break
            else:
                DNA_sequence += line[j].replace('\n', '')
    all_DNA_list.append(DNA_sequence)

#      translate the dna sequence into protein sequence.
for l in range(0,len(seq_name)):
    for k in range(0, len(all_DNA_list[l]), 3):  # step is 3, because a codon is made up of three base pairs.
        codon = all_DNA_list[l][k:k + 3:1]  # When we read it, we should go through 3 base pairs at one go.Step is 1 so we can go through all the base pairs
        protein += genetic_code[codon]  # translate
    all_protein_list.append(protein)           # add all the protein seq to a list

f2 = open("The protein sequence.fa", 'w')        # output the file
for j in range(len(seq_name)):
    f2.write(seq_name[j] + "     ")
    f2.write(str(len(all_protein_list[j]))+'\n')
    f2.write(all_protein_list[j]+'\n')

