"""
Looping Over Data in Python
---------------------------

This script explains in detail how to loop over various data types in Python.
Each section includes example code and explanations.

"""

# 1. Looping Over Lists
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    # 'fruit' takes each element in the list one by one
    print(fruit)

print("-" * 40)  # Separator for output clarity


# Looping Over Lists with Index using enumerate()
# enumerate() allows you to loop over something and get both:

# The index (position)
# The value

for index, fruit in enumerate(fruits):
    # 'index' is the position, 'fruit' is the value
    print(f"Index {index}: {fruit}")

print("-" * 40)


# 2. Looping Over Tuples
coordinates = (10, 20, 30)

for point in coordinates:
    print(point)

print("-" * 40)


# 3. Looping Over Dictionaries

person = {"name": "Alice", "age": 30}

# Looping over keys (default behavior)
for key in person:
    print(key)

print("-" * 40)

# Looping over values
for value in person.values():
    print(value)

print("-" * 40)

# Looping over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

print("-" * 40)


# 4. Looping Over Sets
unique_numbers = {1, 2, 3, 4, 5}

for number in unique_numbers:
    # Sets are unordered; output order may vary
    print(number)

print("-" * 40)


# 5. Looping Over Strings
word = "hello"

for char in word:
    print(char)

print("-" * 40)


# 6. Looping Over Files
# (Make sure "example.txt" exists in the same directory as this script)
try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes trailing newline
except FileNotFoundError:
    print("example.txt file not found. Skipping file loop demonstration.")

print("-" * 40)


# 7. Using break to exit a loop early
for num in range(10):
    if num == 5:
        break  # Stop loop completely when num is 5
    print(num)

print("-" * 40)


# 8. Using continue to skip current iteration
for num in range(5):
    if num == 3:
        continue  # Skip printing when num is 3
    print(num)

print("-" * 40)


# 9. Nested Loops Example
numbers = [1, 2, 3]
letters = ["a", "b"]

for num in numbers:
    for letter in letters:
        print(num, letter)

print("-" * 40)


# 10. Modifying Data While Looping (Creating a new list)
numbers = [1, 2, 3, 4]
squares = []

for num in numbers:
    squares.append(num ** 2)  # Square the number and add to list

print("Squares:", squares)

print("-" * 40)


# 11. List Comprehensions (Pythonic loop to create lists)
squares_comp = [num ** 2 for num in numbers]
print("Squares with list comprehension:", squares_comp)

print("-" * 40)


# 12. Looping Over Multiple Iterables Simultaneously using zip()
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print("-" * 40)


# 13. Practical Tips (Demonstrated as comments)
# - Use meaningful variable names.
# - Avoid modifying a list while looping over it.
# - Use enumerate() when you need indexes.
# - Use dictionary.items() to access keys and values.
# - Use list comprehensions for simple transformations.
# - Remember that sets are unordered.
# - Use 'with open' when working with files for safety.

# End of Looping Over Data examples
