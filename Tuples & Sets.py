# Tuples and Sets in Python
# Tuples are ordered, immutable collections of items. They are defined using parentheses ().
# Sets are unordered collections of unique items. They are defined using curly braces {}.
# Tuples are useful when you want to store a collection of items that should not be changed, 
# while sets are useful when you want to store a collection of unique items and perform operations like union, intersection, and difference.
# Nested tuples and sets are also possible, meaning you can have a tuple or set that contains other tuples or sets as elements.


# Sets are unordered collections of unique items. They are defined using curly braces {}. but you can add or remove elements but NO DUPLICATES ALLOWED

fruits = {"apple", "banana", "cherry", "coconut", "orange"}

print(fruits)

# You can use print(dir(fruits)) to see all the methods available for sets
# You can also use help(fruits) to get more information about the set object and its methods

# You can not use indexing or slicing with sets because they are unordered, but you can use the in operator to check if an item is in the set or not. For example:
print("banana" in fruits)  # Output: True
print("grape" in fruits) # Output: False

# you can add an item to a set using the add() method. For example:
fruits.add("grape")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'coconut', 'orange', 'grape'}

# you cam remove an item from a set using the remove() method. For example:
fruits.remove("apple")
print(fruits)  # Output: {'banana', 'cherry', 'coconut', 'orange', 'grape'}

fruits = {"apple", "banana", "cherry", "coconut", "orange"}
# you can also use the discard() method to remove an item from a set. The difference between remove() and discard() is that 
# remove() will raise a KeyError if the item is not found in the set, while discard() will not raise an error and will simply do nothing if the item is not found. For example:
fruits.discard("apple") # This will not raise an error even though "apple" is not in the set, it will simply do nothing
print(fruits)  # Output: {'banana', 'cherry', 'coconut', 'orange', 'grape'}

fruits = {"apple", "banana", "cherry", "coconut", "orange"}
# You can use pop() method to remove and return an arbitrary item from the set. For example:
print(fruits.pop())  # This will remove and return an arbitrary item from the set, since sets are unordered, you cannot predict which item will be removed
print(fruits)  # Output: The set will have one less item, but you cannot

# If you have a duplicate item in a set, it will automatically be removed because sets do not allow duplicate items.




# NESTED SETS
# Regular sets are unordered collections of unique items and mutable. 
# Because sets are mutable, Python does NOT allow a set to contain another set directly.
# This means you cannot have { {1, 2}, {3, 4} } → this will raise an error.

# Workarounds for nested sets:
# Use tuples inside a set (tuples are immutable and hashable)
nested_set = { (1, 2), (3, 4) }
print(nested_set)  # Output: {(1, 2), (3, 4)}

# Use frozensets inside a set (frozensets are immutable sets)
nested_set2 = { frozenset({1, 2}), frozenset({3, 4}) }
print(nested_set2) # Output: {frozenset({1, 2}), frozenset({3, 4})}

# You can perform normal set operations on sets containing tuples or frozensets
a = { (1, 2), (3, 4) }
b = { (3, 4), (5, 6) }

print(a.union(b))        # Output: {(1, 2), (3, 4), (5, 6)}

print(a.intersection(b)) # Output: {(3, 4)}

# The difference() method returns a set that contains the items that are in the first set but not in the second set. For example:
print(a.difference(b))   # Output: {(1, 2)}


# you can also use and, or, and not operators for set operations
print(a | b)  # Union → {(1, 2), (3, 4), (5, 6)}

print(a & b)  # Intersection → {(3, 4)}

print(a - b)  # Difference → {(1, 2)}

print(a and b)  # Intersection → {(3, 4)}

print(a or b)   # Union → {(1, 2), (3, 4), (5, 6)}

print(not a)    # False, because a is not empty



# TUPLES 
# Tuples are ordered, immutable collections of items. They are defined using parentheses ().
# They are similar to lists, but they cannot be changed after they are created. This means that you cannot add, remove, or modify items in a tuple once it is created.
# They are faster than lists because they are immutable, and they can be used as keys in dictionaries, They can also have duplicate items, but they will not be removed because tuples 
# are ordered and allow duplicates, while sets are unordered and do not allow duplicates.
# 
# because they are hashable, while lists cannot be used as keys in dictionaries because they are not hashable.
# You can access items in a tuple by their index, which starts at 0. You can also use negative indexing to access items from the end of the tuple.
# Tuples have many built-in methods that allow you to manipulate the tuple, such as count() and index().
# Nested tuples are also possible, meaning you can have a tuple that contains other tuples as elements, which allows you to create multi-dimensional tuples.


fruits = ("apple", "banana", "cherry", "coconut", "orange", "apple")
# You can use print(dir(fruits)) to see all the methods available for tuples
# You can also use help(fruits) to get more information about the tuple object and its methods

print(fruits[0])  # Output: 'apple'
print(fruits[-1])  # Output: 'orange'
# print(len(fruits))  # Output: 5
# print("banana" in fruits)  # Output: True
# print(fruits.index("cherry"))  # Output: 2
# print(fruits.count("apple"))  # Output: 2


# ==========================================
# NESTED TUPLES
# ==========================================

# NESTED TUPLES
# Nested tuples are tuples that contain other tuples as elements. 
# Tuples are ordered and immutable, which means the inner tuples cannot be modified.
# They are useful for representing structured data such as grids, matrices, or any multi-dimensional data.

# Example: A 2x3 grid (2 rows, 3 columns)
grid = (
    (1, 2, 3),   # Row 0
    (4, 5, 6)    # Row 1
)

print(grid)          # Output: ((1, 2, 3), (4, 5, 6))
print(grid[0])       # Access first row → (1, 2, 3)
print(grid[1][2])    # Access second row, third column → 6

# Loop through nested tuple
for row in grid:
    for value in row:
        print(value)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6

# Nested tuples can also contain tuples of different sizes or even other data types
nested = (("Alice", 25), ("Bob", 30, "Developer"))
print(nested)        # Output: (('Alice', 25), ('Bob', 30, 'Developer'))

# Important notes:
# - Tuples inside sets or frozensets are immutable, so they can be used as elements.
# - Nested sets using frozenset are rare but useful for advanced set operations.
# - Unlike tuples, nested sets do not have indexing or ordering.
# - Tuples are ordered and allow indexing; sets are unordered and cannot be indexed.
