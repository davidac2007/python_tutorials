# Python numbers

# There are three numeric types in Pythom:

# int
x = 1

# float
y =2.8

# complex
z = 1j 

print(type(x))
print(type(y))
print(type(z))

# Int
#  Int or integer, is a whole number, positive or negative, without decimals,
# of unlimited length.

x = 1
y = 366376429
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
# Float, or "floating point number",positive or negative,
# containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex
# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type conversion
# You can convert from one type to another with the int(), float(), amd complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# You cannot convert complex numbers into another number type.

# Random number 
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used
# to make random numbers:

# Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1,10))

# Python Casting

# Casting in python is therefore done using constructor functions:

'''
 int() - constructs an integer number from an integer literal, a float literal
  (by removing all decimals), or a string literal (providing the string represents
  a whole number)

 float() - constructs a float number from an integer literal, a float literal or a
 string literal (providing the string represents a float or an integer)

  str() - constructs a string from a wide variety of data types, including
  strings, integer literals and float literals
'''

# Integers

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'