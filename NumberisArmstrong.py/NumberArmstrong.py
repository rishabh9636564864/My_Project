num = int(input("enter a number here: "))
order = len(str(num))

sum = 0 
temp = num

while temp > 0:
    digit = temp%10
    sum += digit ** order
    temp  //=10

if sum == num :
    print ('It is an armstrong number')
else:
    print ('It is not an armstrong number')