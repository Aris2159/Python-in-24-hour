print("hello world")
print("this is a print and i can use '' or \" \" ")
print("just print simple text, variables, numbers etc.")
print(123456)
print("it can also be very good to tell what the output is going to be like:")


#I ma learning python in 24 hours what should i start with and go hour by hour


#string indexing and slicing
word = "Python"
print(word[0]) #first character

print(word[2:5]) #characters from position 2 to 4

print(word[1] ) #second character
print(word[-1]) #last character


print(len(word)) #length of the string on how many characters are there in that string
#string methods
text = "Hello, World!"
result = text.upper()  # Convert to uppercase
print(result)  # Output: "HELLO, WORLD!"

result = text.lower() # Convert to lowercase
print(result)  # Output: "hello, world!"

result = text.strip(", ! ") # Remove leading and trailing whitespace
print(result)  # Output: "Hello, World!"

result = text.find("W")
print(result)  # Output: 7 (index of 'W')


result = text.count("H") # Count occurrences of 'H'
print(result)  # Output: 1

result = text.replace("World", "Python") # Replace World with Python it will replace the first occurence with the second one
print(result)  # Output: "Hello, Python!"

# Repeating strings
word = "H"
print(word * 5) # output should be H in 5 times together HHHHH or multiply strings

# print(help(str))  # Get help on string methods

#Checking Content
user_input = input("Enter your name: ")

whitespace = input("Enter something with spaces any kind: ")
print(user_input.isalpha())  # Check if all characters are alphabetic 
print(user_input.isdigit())  # Check if all characters are digits
print(user_input.isalnum())  # Check if all characters are alphanumeric they contain both letters and numbers
print(whitespace.isspace())  # Check if all characters are whitespace aka spaces, tabs, newlines 

#f-strings
name = str(input("Tell me yo name: "))
age = int(input("How old are you my guy?: "))
money = float(input("How much money you got bruh?: "))
print(f"Hello {name}, you are {age} years old and have ${money}.")

#Splitting & Joining
sentence = "I love women and they love me trust me all huzz want me"


#Joining and splitting strings

Vegies = "carrot, potato, cucumber, tomato, onion"
vegies_list = Vegies.split(", ") # Split the characterters that are in the .split() and make them into a substring

#this line is not needed just to show that you can remove characters from a strings too
#vegies_list = Vegies.replace(",", "" ) #Remove the characterters that are in the () from the string

# If the line above is commended then it will be a list of strings with commas
print(vegies_list)  # Output: ['carrot,', 'potato,', 'cucumber,', 'tomato,', 'onion']


#Now joining the list back into a single string
Vegies_joined = "-".join(vegies_list) # Join the list into a single string with - in between each item
print(Vegies_joined)  # Output: "carrot-potato-cucumber-tomato-onion"



# This is 3 exercises to practice string methods
# Exercise 1: Easy – Split a sentence into words
# Take a sentence from the user, split it into words, and print the list of words.
userSentence = input("put a sentence here bruh: ") # Get a sentence from the user
word_list = userSentence.split(" ") # Split the sentence into words based on spaces
print (word_list)


# Exercise 2: Medium – Join words into a sentence
# Take a list of words, join them into a single string with hyphens between words, and print it.
list_of_words = input("put some words anything you like separated by spaces: ").split() # Split input into a list of words
joinem = "-".join(list_of_words) # Join the words with hyphens
print(joinem) # Output the joined string


# Exercise 3: Hard – Reverse words in a sentence
# Take a sentence from the user, reverse the order of the words, and print the new sentence.
text = input("Enter a sentence with extra spaces: ")
words = text.split() # Split the sentence into words (automatically removes extra spaces)
reversed_word = words[::-1] # Reverse the list of words
reversedSentence = " ".join(reversed_word) # Join the reversed words back into a sentence
print(reversedSentence)  # Output the reversed sentence


#Looping through a string
simple_string = "Hello"
for char in simple_string:
    print(char)

#Escape characters

print("He said, \"Hello!\"")  # Using double quotes inside a double-quoted string
print('It\'s a beautiful day!')  # Using single quote inside a single
print("Line1\nLine2")  # New line
print("Column1\tColumn2")  # Tab space
print("This is a backslash: \\")  # inputs a literal backslash
print("Hey\b!")  # Backspace removes the character before it
print("I am lowkey fine\rNot fine")  # Carriage return replaces the beginning of the string with the new text
