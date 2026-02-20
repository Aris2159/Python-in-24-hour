# Error handling in python is an important part and its important so your program doesn't crash pluse it keeps the program running even if something is wrong.
# There are many diffrent types of error gandling function that are build in
# built-in exceptions. Some common ones include:
# SyntaxError – Invalid Python syntax
# NameError – Variable not defined
# TypeError – Wrong data type used
# ValueError – Correct type but invalid value
# IndexError – Index out of range
# KeyError – Key not found in dictionary
# ZeroDivisionError – Division by zero
# FileNotFoundError – File does not exist
# ImportError – Module cannot be imported
# AttributeError – Object has no such attribute

# ----------------------------------------
# Basic try/except
# ----------------------------------------
try:
    # This will raise ZeroDivisionError because division by zero is invalid
    x = 10 / 0
except ZeroDivisionError:
    # This block executes if a ZeroDivisionError occurs
    print("You can't divide by zero!")

# ----------------------------------------
# Multiple except blocks
# ----------------------------------------
try:
    # Trying to convert a non-numeric string to int raises ValueError
    num = int("abc")
except ValueError:
    # Handles invalid value for conversion
    print("Invalid number")
except TypeError:
    # Handles wrong type errors (not triggered here)
    print("Wrong type")

# ----------------------------------------
# Catching multiple exceptions in one block
# ----------------------------------------
try:
    # This also raises ValueError
    value = int("abc")
except (ValueError, TypeError):
    # Handles either ValueError or TypeError in one except block
    print("Conversion error")

# ----------------------------------------
# else block
# ----------------------------------------
try:
    # This conversion is valid
    num = int("10")
except ValueError:
    # This block runs if an exception occurs
    print("Invalid input")
else:
    # This block runs only if no exception occurs
    print("Success:", num)

# ----------------------------------------
# finally block
# ----------------------------------------
try:
    # This may fail if "data.txt" does not exist
    file = open("data.txt")
except FileNotFoundError:
    # Handles missing file gracefully
    print("File not found")
finally:
    # This runs no matter what
    print("Done")

# ----------------------------------------
# Raising exceptions manually
# ----------------------------------------
age = -5
if age < 0:
    # Raises a ValueError because negative age is invalid
    raise ValueError("Age cannot be negative")

# ----------------------------------------
# Custom exception classes
# ----------------------------------------
class CustomError(Exception):
    """Custom exception for demonstration purposes."""
    pass

# Raise the custom exception manually
raise CustomError("Something went wrong")

# ----------------------------------------
# Assertions for debugging
# ----------------------------------------
x = 5
# Will raise AssertionError if condition fails
assert x > 0, "x must be positive"

# ----------------------------------------
# Exception chaining
# ----------------------------------------
try:
    # Raises ValueError because string is not numeric
    int("abc")
except ValueError as e:
    # Raises new TypeError but preserves the original ValueError context
    raise TypeError("Wrong conversion") from e


# This is a General structure

try:
    # Code that might raise an exception goes here
    pass
except Exception:
    # This block runs if an exception occurs in the try block
    # 'Exception' is the base class for most built-in exceptions
    pass
finally:
    # This block always runs, whether an exception occurred or not
    # Useful for cleanup, like closing files or releasing resources
    pass

# raise statement is used to trigger an exception either a built-in one or a custom one.
# it tells Python “something went wrong here” and stops normal execution unless the exception is caught.