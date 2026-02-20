# Functions in Python are defined using the 'def' keyword, followed by the function name and parentheses. They can take parameters and return values.
# A function is a reusable block of code that performs a specific task. Functions help to break down complex problems into smaller, more manageable pieces, 
# and they promote code reusability and modularity.
# The syntax for defining a function is:
# def function_name(parameters):
#     # block of code to be executed
# return is a statment that is used to end a function and send a result back to the caller. 
# It can be used to return a value from a function, or it can be used to simply exit a function without returning anything.

# Define a function and in parameters we can put the name of the person we want to wish happy birthday to
# This function takes a name as an argument and prints a birthday message using an f-string to format the output.
def happy_birthday(name):
    print(f"Happy birthday, {name}!")

# The "Alice" is the argument that we are passing to the function, which will be used as the value for the "name" parameter in the function definition.
happy_birthday("Alice")

# You can also return values from a function using the return statement. 
# For example, you can create a function that adds two numbers and returns the result:
def add_numbers(a, b):
    # The return statement is used to send the result of the addition back to the caller. 
    # When you call the function with specific values (e.g., 5 and 3), it will compute the sum and return it, which is then stored in the variable 'result'.
    return a + b
# When you call the function with specific values (e.g., 5 and 3), it will compute the sum and return it, which is then stored in the variable 'result'.
result = add_numbers(5, 3)
print(result)  # Output: 8

# Functions can also be recursive, meaning they can call themselves. This is useful for solving problems that can be broken down into smaller, similar subproblems.
# You can also declear variables in the function and they will be local to the function, meaning they cannot be accessed outside of the function.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Bob")  # Output: Hello, Bob!
greet("Bob", "Hi")  # Output: Hi, Bob!

# You can also use opprators in the function to perform calculations or manipulate data. 
# For example, you can create a function that multiplies two numbers and returns the result:
def multiply(x, y):
    # The return statement is used to send the result of the multiplication back to the caller.
    return x * y
# This will give values to x and y in the function and then return the result of the multiplication, which is stored in the variable 'result'.
result = multiply(4, 5)
print(result)  # Output: 20

# You can also use conditional statements (if, elif, else) in a function to perform different actions based on certain conditions.
def factorial(n):
    #  The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. 
    #  The factorial of 0 is defined to be 1. The factorial function can be defined recursively as follows:
    if n == 0:
        # if the n is 0 the function will return 1 because the factorial of 0 is defined to be 1
        return 1
    # if n is not 0, the function will call itself with n-1 and multiply the result by n, which will give us the factorial of n.
    else:
        return n * factorial(n-1)
# This will give the n the value of 5 then use the function to calculate the factorial of 5, which is 5 * 4 * 3 * 2 * 1 = 120, and then print the result.
print(factorial(5))  # Output: 120

# You can also use string manipulation in a function to perform operations on strings. For example, 
# you can create a function that generates a full name from a first name and last name:
def name_generator(first, last):
    # The capitalize() method is used to convert the first character of a string to uppercase and the rest of the characters to lowercase.
    # you can use the variables created in the function to manipulate the data and then return the result. 
    # In this case, we are capitalizing the first and last names and then returning the full name as a formatted string.
    first = first.capitalize()
    last = last.capitalize()
    # The return statement is used to send the full name back to the caller. 
    # When you call the function with specific values (e.g., "john" and "doe"), it will capitalize the names and return the full name, which is then printed.
    return f"{first} {last}"

# This will ask the user to input the first and last name, split the input into a list of two elements 
# (first name and last name), and then pass those elements as arguments to the name_generator function. The function will return the full name, which is then printed.
full_name = input("Enter your first and last name: ").split()
print(name_generator(full_name[0], full_name[1]))