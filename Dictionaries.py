# Dictionary is a collection of {key: value} pairs
#       # ordered and changeable. No duplicates
# This is also known as hash map in other languages
# They are not allowed to have duplicate keys, they are changable, and ordered

# To create a dictionary you make a variable and then use {} and then key: Value and if you want to add more then you can use a comma and keep adding more
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
}

# To get help use dir but if you want more details you use help
#print(dir(capitals))
#print(help(capitals))

# ----------------------------------------
# Accessing Values
# ----------------------------------------

# You use .get() to prevent errors if the key doesn't exist but if you don't use it then you will crash the program
print(capitals.get("USA"))

# Making variables to use in the if statment for example
country = "USA"
capital = capitals.get(country)

# This is checking if the "USA" key exist in the dictionary if it does then run the first statment or run the statment after else
if capitals.get("USA"):
    print(f"{country}'s capital is {capital}")
else:
    print("Not in the data set")


# ----------------------------------------
# Adding and Updating Items
# ----------------------------------------


# New Items can be added to the dictionary
# Using print statment to show how each one works
capitals.update({"Germany": "Berlin"})
print(capitals)

# You can also update an exesting key to have a new value
capitals.update({"USA": "Cali"}) # (Example of updating value)
print(capitals)

# ----------------------------------------
# Removing Items
# ----------------------------------------

# .pop() remove a specific key you like to remove from the dictionary
capitals.pop("China")
print(capitals)

# Remove the last inserted item from the dictionary by using .popitem()
capitals.popitem()
print(capitals)

# Clear the dictionary deleat everything that exitst in there by using .clear()
print(capitals.clear())
print(capitals)


# ----------------------------------------
# Looping Through a Dictionary
# ----------------------------------------

# Re-create dictionary because of clear function above
capitals = {"USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# These are a little tricky so make sure to read this carefully

# This is OOP so make sure to go over OOP as it is a little tricky

#The .keys() method

# Returns a view object that contains all the keys in the dictionary.
# A "view object" reflects changes made to the dictionary.
# By default, looping directly over a dictionary also loops over its keys,
# but we are explicitly using .keys() here for clarity.

# This is a variable key and is equal to .keys() methodf that allow us to look at dictionary keys and then prind them out
key = capitals.keys()
# This will just print out all the key values of the dictionary
print(key)

# this is just a for loop and will do the same thing as above but in new line just display the countries
for key in capitals.keys():
    # Each iteration assigns one key from the dictionary to the variable "country"
    # On first loop: country = "USA"
    # On second loop: country = "India"
    # and so on...
    print(key)



# The .values() method
# Returns a view object containing all the values in the dictionary.
# This allows us to access only the values without referencing the keys.


values = capitals.values()
# This will just print out all the key values of the dictionary
print(values)

# this is just a for loop and will do the same thing as above but in new line just display the captials of each country
for value in capitals.values():
    # Each iteration assigns one value to the variable "capital"
    # On first loop: capital = "Washington D.C."
    # On second loop: capital = "New Delhi"
    # etc.
    print(value)



#The .items() method

# Returns a view object containing tuples of (key, value) pairs.
# Each element returned is a tuple.
# Example of one item: ("USA", "Washington D.C.")

#We use tuple unpacking in the loop:
#    for country, capital in capitals.items():

#This means:
#    country = key
#    capital = value
#for each iteration.


# This is an advance topic but its good to look at early on to know whats happning
items = capitals.items()
print (items) # Items return a dictionariy object that resembles a 2D list of tuples


# this is just a for loop and will do the same thing as above but in new line just display the countries and captial in a line and for every new country and captial in a new line
for key, value in capitals.items():
    # First loop:
    # key = "USA"
    # value = "Washington D.C."
    print(f"{key}: {value}")