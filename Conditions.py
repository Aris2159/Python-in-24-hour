# Conditionds in pythong are used to check if a certain condition is true or false. They are often used in if statements, loops, and other control flow structures.
# The most common conditional statements in Python are:
# 1. if statement: This is used to execute a block of code if a certain condition is true.
# 2. elif statement: This is used to check multiple conditions after an if statement.
# 3. else statement: This is used to execute a block of code if all the previous conditions are false.
# We will be focusing on the if statement in this code snippet.
#The loops will be covered in Loops.py

# if = Do something only if the condition is true
# elif = Do something else if the previous condition is false and this condition is true
# else = Do something if all the previous conditions are false

# You can use comparison operators to compare values in conditions. For example:
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# is (identity operator, checks if two variables point to the same object)


# You can also use logical operators to combine conditions. For example:
# and (both conditions must be true)
# or (at least one condition must be true)
# not (negates the condition)



# Example of if statement Number 1
age = input("Enter your age: ")
age = int(age)
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
elif age < 0:
    print("You are not even living yet.")
else:
    print("You are an unc")


# Example of if statement Number 2
answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("correct")
else:
    print("incorrect")

# Example of if statement Number 3
name = input("What is your name? ")
if name == "":
    print("You did not enter a name.")
else: 
    print(f"Hello, {name}!")

# You can also use Boolean values (True or False) in conditions. For example:
# Example of if statement Number 4
online = True
if online:
    print("The user is online.")
else:
    print("The user is offline.")

# Switch case statments are not available in Python, but you can achieve similar functionality using if-elif-else statements or dictionaries. For example:
# Example of switch case using if-elif-else
day = input("Enter a day of the week: ")
if day.lower() == "monday":
    print("It's the start of the week.")
elif day.lower() == "friday":
    print("It's almost the weekend.")
elif day.lower() == "saturday" or day.lower() == "sunday":
    print("It's the weekend!")
else:
    print("It's a regular weekday.")

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, because the values are the same
print(id(a))  # Memory address of a
print(id(b))  # Memory address of b
# All is operators check for identity, meaning they check if two variables point to the same object in memory. 
# In this case, a and b are different objects in memory, so a is b will return False.

# in other words we can say that the == operator checks for value equality, while the is operator checks for identity.
# Another way to check is
# They this is just is function but insted of using "is" we can use "id" function to check if the memory addresses of a and b are the same or not.
print(id(a) == id(b)) # False, because a and b have different memory addresses

print(a is b)  # False, because a and b are different objects in memory


# False Values in Python include:
# 1. None
# 2. False
# 3. 0 (zero of any numeric type)
# 4. 0.0 (zero float)
# 5. 0j (zero complex)
# 6. Empty sequences and collections (e.g., '', [], (), {})
# All other values are considered True in a Boolean context. For example:
if []:
    print("This will not be printed because an empty list is considered False.")
else:
    print("This will be printed because the condition is False.")
