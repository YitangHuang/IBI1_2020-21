import matplotlib.pyplot as plt
labels = "USA", "India", "Brazil", "Russia", "UK"
size = [29862124, 11285561, 11205972, 4360823, 4234924]
explode = (0.1, 0.1, 0.1, 0.05, 0)
plt.pie(size, explode=explode, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
plt.axis("equal")
plt.show()
exit()
