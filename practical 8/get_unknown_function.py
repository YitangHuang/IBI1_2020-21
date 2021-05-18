import re
import os
# import all the packages needed
os.chdir("E:/github repo/IBI1_2020-21/practical 8")   # change the working directory just as what was done in practical 7
f = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
line = f.readlines()            # read how many lines does the file have
sequence = ''
seq_name = []
all_sequence_list = []              # initial some varies
for i in range(len(line)):          # use a for loop and regular expression to find out any lines start with ">"and contains "unknown function"
    if line[i].startswith('>') and line[i].find('unknown function') > 0:
        seq_name.append(line[i].split()[0].split('_')[0])                           # add the name to the list
        for j in range(i+1, len(line)):                                             # use a for loop to get the dna sequence
            if line[j].startswith('>'):
                break                                                               # withdraw the loop if next sequence start, which means that meet anohter ">"
            else:
                sequence += line[j].replace('\n', '').strip()
    all_sequence_list.append(sequence)
                                                                                   # output the file
f2 = open('unknown_function.fa', 'w')
for k in range(len(seq_name)):
    f2.write(seq_name[k]+"     ")
    f2.write(str(len(all_sequence_list[k]))+'\n')
    f2.write(all_sequence_list[k]+'\n')




