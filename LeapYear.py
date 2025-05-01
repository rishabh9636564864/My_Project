#--Check Leap Year--

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):   # this is for Century years like 100 , 2000
    print(year, "is a Leap Year")

elif (year % 4 == 0) and (year % 100 != 0):   # this is for others leap years 
    print(year, "is a Leap Year")

else:
    print(year, "is not a Leap Year")