a = 210202
b = 190784
c = 170521
d = abs(a-c)
e = abs(a-b)

if d > e:
    print("d is greater than e.")
elif d < e:
    print("e is greater than d.")
else:
    print("e equals d.")
# Compare  d and e
##################################################################################################################
print("Z = (X and not Y) or (Y and not X)")
X = True
Y = False
Z = (X and not Y) or (Y and not X)
print("X=True and Y=False, Z is", Z)

X = False
Y = True
Z = (X and not Y) or (Y and not X)
print("X=False and Y=True, Z is", Z)
if Z is True:
    print("No matter X = True, Y = false or X = False, Y = True, Z is True")
else:
    print("Z is not always true.")
# Verify Z
#################################################################################################################
W = X != Y

if W == Z:
    print(W == Z, type(W))
# Verify W
