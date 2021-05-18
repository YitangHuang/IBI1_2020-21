#  Let the user intput a DNA sequence
DNA_Seq = ''
reverse_complement = []
def calculator(sequence):
    # define the function

    DNA_seq = input("This is a reverse complement calculator. Please input the DNA sequence:")
    # input the sequence

    DNA_seq = DNA_seq.upper()
    # Capitalize all the letters


    for i in DNA_seq:
        if i == "A":
            reverse_complement.append("T")
        if i == "T":
            reverse_complement.append("A")
        if i == "G":
            reverse_complement.append("C")
        if i == "C":
            reverse_complement.append("G")
    return reverse_complement
# Complementary base pairing

print("".join(calculator(DNA_Seq)))

# Converts the list to string output
# out put the outcome
