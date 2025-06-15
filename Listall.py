#--> Adding Elements <-- #
  # append() method
cars = ["Hyundai", "Suzuki", "Kia"]
cars.append("Honda")
print(cars)                   # Output: ['Hyundai', 'Suzuki', 'Kia', 'Honda']

# insert()
number = [1, 2, 3, 4, 5]
number.insert(2, 10)
print(number)                 # Output: [1, 2, 10, 3, 4, 5]

#--> Removing Element <-- #
   # remove()
bikes = ["Honda", "Bajaj", "TVS", "Hero"]
bikes.remove("Honda")
print(bikes)                  # Output: ['Bajaj', 'TVS', 'Hero']

   # pop()
students = ["Rishabh", "Kinjal", "Shivaksh", "Charit"]
popped = students.pop(1)
print(students)               # Output: ['Rishabh', 'Shivaksh', 'Charit']
print(popped)                 # Output: Kinjal

   # del()
teacher = ["Vimal", "Kavita", "Anshu", "Vipul"]
del teacher[1]
print(teacher)                # Output: ['Vimal', 'Anshu', 'Vipul']

#--> Finding Element <-- #
   # index()
fruits = ["apple", "banana", "mango"]
index = fruits.index("banana")
print(1)                      # Output: 1

    # count()
fruits = ["apple", "banana", "orange", "banana"]
count = fruits.count("banana")
print(count)          # Output: 2

#--> Sorting and reversing <-- #
    # sort()
number = [5, 2, 4, 1, 3]
number.sort()
print(number)        # Output: [1, 2, 3, 4, 5]

    # reverse()
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)        # Output: [5, 4, 3, 2, 1]

#--> List Comprehension <-- #
   # Syntax: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers if num % 2 == 0]
print(squared)        # Output: [4, 16]
 
    # Example: Create a list of even numbers from 1 to 10
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)          # Output: [2, 4, 6, 8, 10]

#--> Built-in Functions and Methods for Lists <-- #
    # len()
fruits = ["apple", "banana", "orange"]
length = len(fruits)
print(length)         # Output: 3

    # min() and max()
numbers = [1, 2, 3, 4, 5]
minimum = min(numbers)
maximum = max(numbers)
print(minimum)        # Output: 1
print(maximum)        # Output: 5

     # sum()
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)          # Output: 15

     # sorted()
numbers = [5, 2, 4, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]

     # clear()
fruits = ["apple", "banana", "orange"]
fruits.clear()
print(fruits)         # Output: []

     # copy()
fruits = ["apple", "banana", "orange"]
fruits_copy = fruits.copy()
print(fruits_copy)    # Output: ['apple', 'banana', 'orange']

#--> Nested List <-- #
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1])            # Output: [4, 5, 6]
print(nested_list[1][2])         # Output: 6

