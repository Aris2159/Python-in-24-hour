#data types in python
a = 1
b = 1
#print(1)
print(a + b)
print(type(a)) #checking data type: integer


c= "1"
d= "1"
print(c + d)
print(type(c)) #checking data type: string

#basic data types in python:
#1. Numeric data types: int, float, complex
a1 = 1 #integer

a2 = 1.5 #float
print(type(a2)) #checking data type to prove its a float

a3 = complex(3,5) #complex number
#3+5i
print (type(a3))


#2. Sequence data types: srtring, list, tuple, range
b1 = "Sehaj" #string
b11 = "23" #string
print(type(b1))


b2 = [12, 23, 43, "uwu", 32] #list
print (type(b2))

b3 = (12, 23, 43, "uwu", 32) #tuple
print (type(b3))

#3. Dictionary
#(key:value)

my_dictionary = {'name': 'Sehaj', 'age': 20, 'city': 'Kingston'} #dictionary
print(type(my_dictionary))

#4. Set data type
my_set = {12, 23, 43, "uwu", 32} #set
print(type(my_set))

#5. Boolean data type

bool1 = True
bool2 = False
print(type(bool1))

#6. Binary data types: bytes, bytearray, memoryview

byte1 = b"Sehaj" #bytes
print(type(byte1))



name = input('Whats yo name gang? ')
age = int(input('How old you unc? '))
waifu = input('Who is your waifu bro? ')
money = float(input('How much money you got fam? '))

#this is not a proficinal way because its hard to read and not using f strings
print("yo name is ", name, " you are ", age, " years old", " your waifu is ", waifu, " and you got ", money, " dolla dolla bills yall")

#this is a proficinal way using f strings and easy to read
print(f"yo name is {name}, you are {age} years old, your waifu is {waifu} and you got {money} dolla dolla bills yall")