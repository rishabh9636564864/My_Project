#--Find Largest number--

num1 = int(input("Enter 1st number here: "))
num2 = int(input("Enter 2st number here: "))
num3 = int(input("Enter 3st number here: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is the largest")

elif (num2 > num1) and (num2 > num3):
    print(num2, "is the largest")

else:
    print(num3, "is the largest")