# There are 3 types of loops in Python: for, while, and nested loops.
# A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. It executes a block of code for each item in the sequence.
# A while loop is used to execute a block of code as long as a certain condition is true. It continues to execute until the condition becomes false.
# Nested loops are loops that are inside another loop. The inner loop is executed for each iteration of the outer loop.

# Lets start with for loops. The syntax for a for loop is:
# for variable in sequence:
#     # block of code to be executed


# Before we get into loops lets quickly go over continue and break statements. 
# The continue statement is used to skip the rest of the code inside a loop for the current iteration and move on to the next iteration. 
# The break statement is used to exit a loop prematurely, meaning it will stop the loop from executing any further iterations.
# continue = “skip this round, go to the next one”
# break = “we’re done with this loop”


# for loop = execute a block of code a fixed number of times
# you can iterate over a range, string, list, tuple, dictionary, set, or any other iterable object

#basic syntax of a for loop
# This will print the numbers 1 to 10
# the "x" is just a variable name, you can use any name you want and it works the same way as string slicing
# for printing the range you can also do steps if you like by adding a third valur in the () like this: range(1, 11, 2) which will print the odd numbers from 1 to 10
for x in range(1, 11):
    print(x)
# this comes out of the loop and prints the message because its on the same level of indentation as the for loop, 
# if it was indented it would be part of the loop and would print the message for each iteration of the loop
print("Done with the loop!")

# This is a list for the for loop
nums = [1, 2, 3, 4, 5]
# this will print each number in the list
for num in nums:
    # If the number is 3, it will print "Found 3!" and then skip the rest of the code in the loop and go to the next iteration
    if num == 3:
        print("Found 3!")
        # The continue statement is used to skip the rest of the code inside the loop for the current iteration and move on to the next iteration.
        continue
    print(num)

#while loop = execute a block of code as long as a condition is true
# The syntax for a while loop is:
# while condition: 
#     # block of code to be executed

# While loops will keep going until the condition becomes false. You can use a while loop to create an infinite loop by using a 
# condition that is always true, but you should be careful with this as it can cause your program to crash.

x = 0
# While True means that the loop will run indefinitely until it is broken out of with a break statement or an exception is raised
while True:
    # If x is equal to 5, the break statement will exit the loop
    if x == 5:
        break
    # This will print the value of x and then increment x by 1. The loop will continue until x is equal to 5
    print(x)
    # The += operator is a shorthand for x = x + 1. It increments the value of x by 1 and assigns the new value back to x.
    x += 1


# Nested loops = a loop inside a loop it can be for loop or while loop
# it can be  for loop inside a while loop or a while loop inside a for loop
# The inner loop will be executed for each iteration of the outer loop

# This is a list for the numbers
num = [1, 2, 3, 4, 5]

# This is a nested loop that will print each number in the list and then print each letter in the string "abc" for each number
for num in nums:
    # loop inside of a loop the letter and the num are different variables so they can have the same name without causing any issues
    for letter in "abc":
        # This will print the current number and letter for each iteration of the inner loop. 
        # The inner loop will run 3 times for each number in the outer loop, resulting in a total of 15 iterations (5 numbers * 3 letters).
        print(num, letter)