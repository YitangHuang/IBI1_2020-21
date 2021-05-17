n = 84             # define n = 84, which means we have 84 students in our class
r = float(input("Please input the r rate:"))           # Let the user input the r value
for i in range(0, 5):  # 5 generation
    n = n + n * r  # calculate the total number of infected individuals
n = int(n)
print("r rate is", r, ",total number of individuals infected after 5 generations is", n)      # Output the result
