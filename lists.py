# Lists in python are used to store multiple items in a single variable. 
# They are ordered, changeable, and allow duplicate values. Lists are defined using square brackets []. Duplicate values are allowed in lists, meaning you can 
# have multiple occurrences of the same value in a list.
# 
# You can access items in a list by their index, which starts at 0. You can also use negative indexing to access items from the end of the list.
# Lists have many built-in methods that allow you to manipulate the list, such as append(), remove(), pop(), sort(), and reverse(). 
# You can also use slicing to access a range of items in the list.
# Nested lists are also possible, meaning you can have a list that contains other lists as elements. 
# This allows you to create multi-dimensional lists, such as matrices or tables.

# List starts with 0 index
fruits = ["apple", "banana", "cherry", "coconut", "orange"]

# to list the diffrent methods of the list you can use the dir() function which will return a list of all the attributes and methods of the list object

#print(dir(fruits))

#use the help() function to get more information about a specific method. For example, to get information about the append() method, you can use help(fruits.append)

#print(help(fruits))

# Print the list of fruits
print(len(fruits))  # Output: 5

# We can use "in" operator to check if the item is in the list or not
print("banana" in fruits)  # Output: True

print("grape" in fruits) # Output: False


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can also use the index() method to find the index of an item in the list. For example:
print(fruits.index("cherry"))  # Output: 1


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can sort the list using the sort() method. For example:
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'coconut', 'orange']


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use the append() method to add an item to the end of the list. For example:
fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'coconut', 'orange', 'grape']


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# you can use the insert() method to add an item at a specific index. For example:
fruits.insert(1, "kiwi") # This will insert "kiwi" at index 1, which will shift the other items to the right
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'coconut', 'orange', 'grape']


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use the remove() method to remove an item from the list. For example:
fruits.remove("apple")
print(fruits)  # Output: ['kiwi', 'banana', 'cherry', 'coconut', 'orange', 'grape']


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use reverse() method to reverse the order of the list. For example:
fruits.reverse()
print(fruits)  # Output: ['grape', 'orange', 'coconut', 'cherry', 'banana', 'kiwi']


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use [] to change the value of an item in the list. For example:
fruits[0] = "grape"
print(fruits)  # Output: ['grape', 'banana', 'cherry', 'coconut', 'orange']


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use the pop() method to remove an item from the list and return it. For example:
popped_fruit = fruits.pop(0) # This will remove the item at index 0 and return it
print(popped_fruit)  # Output: 'grape'

# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# you can use the count() method to count the number of occurrences of an item in the list. For example:
fruits.count("banana")
print(fruits.count("banana"))  # Output: 2


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use the clear() method to remove all items from the list. For example:
fruits.clear()
print(fruits)  # Output: []


# Puitting list so that we can look at the original list before making any changes to it
fruits = ["apple", "banana", "cherry", "coconut", "orange"]
# You can use the copy() method to create a copy of the list. For example:
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: []

# You can use slicing like string slicing to access a range of items in the list. The syntax for slicing is list[start:stop:step].
print(fruits[0:3])  # Output: apple, banana, cherry

# Loop to print each fruit in the list
for fruit in fruits:
    print(fruit)



# ==========================================
# NESTED LISTS IN PYTHON
# ==========================================

# A nested list is a list that contains other lists as its elements.
# Think of it like a table (rows and columns).

# Example: A 3x3 matrix (3 rows, 3 columns)

matrix = [
    [1, 2, 3],     # Row 0
    [4, 5, 6],     # Row 1
    [7, 8, 9]      # Row 2
]

# ------------------------------------------
# Accessing Elements
# ------------------------------------------

# To access an element in a nested list:
# Use two indexes: [row][column]

print(matrix[0])        # Access entire first row → [1, 2, 3]
print(matrix[0][1])     # Row 0, Column 1 → 2
print(matrix[2][2])     # Row 2, Column 2 → 9

# ------------------------------------------
# Modifying Elements
# ------------------------------------------

# Change a value
matrix[1][1] = 50
print(matrix)  
# Output:
# [
#   [1, 2, 3],
#   [4, 50, 6],
#   [7, 8, 9]
# ]

# ------------------------------------------
# Looping Through a Nested List
# ------------------------------------------

# Loop through each row
for row in matrix:
    print(row)

# Loop through each element inside each row
for row in matrix:
    for item in row:
        print(item)

# ------------------------------------------
# Adding a New Row
# ------------------------------------------

matrix.append([10, 11, 12])
print(matrix)

# ------------------------------------------
# Practical Example: Student Grades
# ------------------------------------------

students = [
    ["Alice", 85, 90, 88],
    ["Bob", 78, 81, 85],
    ["Charlie", 92, 89, 95]
]

# Access Bob's second grade
print(students[1][2])   # 81

# Loop and print student names
for student in students:
    print("Name:", student[0])
