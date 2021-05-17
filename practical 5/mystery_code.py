# What does this piece of code do?
# Answer: Keep selecting a number between 1 and 100 until the number is less than 50 or equals to 50, and then print the number.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False     # define the value of P and prepare for the loop
while p==False:     # start the loop
	p = True                 # stop the loop if the number is not greater than 50
	n = randint(1,100)           # select a number from 1 to 100 randomly
	if n > 50:             # Use a if command to check if the number is greater than 50 or not
		p = False

print(n)                  # output the number
