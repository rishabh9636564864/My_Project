#--> Find the Sum of Natural Numbers <--
num = int(input("Enter a number here: "))

if num < 0:
    print('Please enter Positive Number')
else:
    sum = 0
    while num>0:
        sum += num
        num -= 1

    print(sum)