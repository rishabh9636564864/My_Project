#--> Find Numbers Divisible by Another Number <--#
# Solution 1 to Using for loop
#print("The Numbers divisible by 13 are: ")
#for i in range (1,100):
#   if i % 13 == 0:
#        print(i)

# Solution 2 to using Lambda funtion and filter()
l = [39,48,26,98,33,67,87]
result = list(filter(lambda x : x % 13 == 0,l))

print('the numbers divisible by 13 are', result)