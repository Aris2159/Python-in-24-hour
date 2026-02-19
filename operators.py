# Operators can be used with strings in Python for various purposes such as concatenation, repetition, and slicing.
# Here are some examples of how operators work with strings:
# There are arithmetic operators, comparison operators, and logical operators

# Arithmetic Operators
#Addition Operator
#srting
string= "Hello" 
string2 = " World"
print(string + string2) # Concatenation operator for strings\
#number
num1 = 2
num2 = 3

# All the arithmetic operators work with the numbers but not with the strings 
# except for the addition operator which is used for concatenation of strings. 
# The other arithmetic operators will raise an error if attempted to be used with strings.
print(num1 + num2) # Addition operator for numbers
print(num1 - num2) # Subtraction operator for numbers
print(num1 * num2) # Multiplication operator for numbers
print(num1 / num2) # Division operator for numbers
print(num1 ** num2) # Exponentiation operator for numbers
print(num1 // num2) # Floor division operator for numbers
print(num1 % num2) # Modulus operator for numbers

#short hand operators
x = 10
y = 5

x += x # This is equivalent to x = x + 10
print(x) # Output: 20

y -= y # This is equivalent to y = y - 5
print(y) # Output: 0

x //= 2 # This is equivalent to x = x // 2
print(x) # Output: 10

#redeclearing variable so it be used as 10 insted of updating the number to remove the effect of the previous operator
x = 10
x /= 2 # This is equivalent to x = x / 2
print(x) # Output: 5.0

#redeclearing variable so it be used as 10 insted of updating the number to remove the effect of the previous operator
x = 10
x *= 3 # This is equivalent to x = x * 3
print(x) # Output: 30

#redeclearing variable so it be used as 10 insted of updating the number to remove the effect of the previous operator
x = 10
x **= 2 # This is equivalent to x = x ** 2
print(x) # Output: 100

#redeclearing variable so it be used as 10 insted of updating the number to remove the effect of the previous operator
x = 10
x %= 3 # This is equivalent to x = x % 3
print(x) # Output: 1

# Unitary Operators
# The unary operators are used to perform operations on a single operand.
# The unary operators are +, -, and ~.
n = 7
print(-n) # Output: -7 (negation operator)
print(+n) # Output: 7 (positive operator)
# ~ is used for bitwise NOT operation, which inverts the bits of the number. For example, if n is 7 
# (which is 0000 0111 in binary), ~n will be -8 (which is 1111 1000 in binary).
# this is because in Python, integers are represented in a way that allows for negative numbers using two's complement.
print(~n) # Output: -8 (bitwise NOT operator)

# Comparison Operators

a = 5
b = 10
a < b # Output: True (less than operator)
a > b # Output: False (greater than operator)
a <= b # Output: True (less than or equal to operator)
a >= b # Output: False (greater than or equal to operator)
a == b # Output: False (equal to operator)
a != b # Output: True (not equal to operator)

# Logical Operators
# They are used with conditional statements to combine multiple conditions. The logical operators are and, or, and not.
a, b = 5, 4

# Logical operators are used to combine conditional statements. The logical operators are and, or, and not.

# And operator returns True if both conditions are true, otherwise it returns False. Even one condition is false then it will return False
a <8 and b > 3 # Output: True (logical AND operator)

# Or operator returns True if at least one of the conditions is true, otherwise it returns False. Even one condition is true then it will return True
# If both conditions are false then it will return False
a < 8 or b > 5 # Output: True (logical OR operator)

# Not operator is used to reverse the logical state of its operand. If a condition is true, it will return False, and if a condition is false, it will return True.
# In other words it will return the opposite of the condition.
not (a < 8) # Output: False (logical NOT operator)
