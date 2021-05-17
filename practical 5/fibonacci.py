x = 1
y = 1  # define the first two numbers of Fibonacci
print(x)
print(y)  # print the first 2 numbers of Fibonacci
for i in range(1, 12):  # repeat the process for 11 times
    z = x + y      # calculate the new number
    print(z)           # print the new number added up by the previous 2
    x = y              # exchange the value of x and y
    y = z               # exchange the value of y and z


