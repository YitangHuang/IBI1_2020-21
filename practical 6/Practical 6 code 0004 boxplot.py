import matplotlib.pyplot as plt   # import the pyplot from matplotlib
gene_lengths = [9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]
# input the data
average_length = []  # just set up a new list which is used for ave_axon length
for i in range(0, 10):
    average_length.append(gene_lengths[i]/exon_counts[i])
    # calculate the average length with for command so we don't ne to do the calculation one by one
average_length.sort()    # just sort the average list
print(average_length)  # out put the result and data
plt.boxplot(average_length, labels=["The Average length"])  # make a boxplot
plt.title("The Average length")  # title the box plot
plt.show()
# show the box plot
