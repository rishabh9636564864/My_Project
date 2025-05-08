#--> Display the Multiplication Table

# Solution: 1  With for loop
n = int(input("enter a number here: "))
for i in range (1, 11):
    print(n, "x", i, "=", n*i)


# Solution: 2 with while loop
n = int(input("enter a number here: "))
i = 1
while i<=10:
    print(n, "x", i, "=", n*i)
    i +=1