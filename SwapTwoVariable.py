#--Swap Two Variable--

#Solution 1 (Using third Variable)
x = 16
y = 18

temp = x   # temp is a Temporary  x value assign in temp
print("The value of temp variable is", temp)

X = y
print("The value of x is", x)

y = temp
print("The value of Y is", y)

#Solution 2 (Without Using third Variable)
x = 12
y = 13
x,y = y,x

print("The value of x is", x)
print("The value of Y is", y)