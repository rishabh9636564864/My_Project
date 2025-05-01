#--This program Find & Calculate Square root--

# Solution 1 (Using Exponentiation)
num = 64
num1 = int(input("Enter a number here: "))
sr = num1**(1/2) # / 0.5 
print("The Square root of the given number is", sr)

# Solution 2 (Using math module)
import math
num = 49
num1 = int(input("Enter a number here: "))
sr = math.sqrt(num1)
print("The Square root of the given number is", sr)