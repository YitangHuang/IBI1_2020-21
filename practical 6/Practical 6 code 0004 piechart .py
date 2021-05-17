import matplotlib.pyplot as plt          # import matplotlib to make a pie chart
labels = "USA", "India", "Brazil", "Russia", "UK"           # label the pie of the pie chart
size = [29862124, 11285561, 11205972, 4360823, 4234924]           # input the data of each pie of the pie chart
explode = (0.1, 0, 0, 0, 0)       # define the position of each pie of the pie chart
plt.pie(size, explode=explode, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
plt.axis("equal")    # make a the pie chart is a circle
plt.title("The Condition of Covid-19 Of 5 Countries")
plt.show()        # show the pie chart
exit()         # end the program
