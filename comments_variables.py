print("Hello world! \n")

if 5 > 2:
    print("Five is greater than two")

x = 5
y = "Hello"

print(x, y)

z = float(3)

w = """
This
is
a
multiline
text
"""
# This is a comment
print(w)

# age = int(input("Tu edad: "))

print(type(w))

# Multi Words Variable Names

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Values to multiple variables
a, b, c = "Orange", "Banana", "Strawberry"

print(a, b, c)

# One Value to Multiple Variables
e = f = g = "Orange"
print(e, f, g)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
h, i, j = fruits
print(h)
print(i)
print(j)

# Output Variables
x = "awesome"
print("Python is " + x)

x = "I am "
y = 19
print(x + str(y))

a = "My name is "
b = "David"

print(a + b)

x = 5
y = 10
print(x + y)

# Global variables

'''
Variables that are created outside of a function
(as in all of the examples above) are known as global variables.
Global variables can be used by everyone,
both inside of functions and outside.
'''

# Create a variable outside of a function, and use it inside de function

x = "awesome"


def myfunc():
    print("Pyton is " + x)


myfunc()

'''
If you create a variable with the same name inside a function,
this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was,
global and with the original value.
'''


x = "awesome"


def myfunc2():
    x = "fantastic"
    print("Python is " + x)


myfunc2()

print("Python is " + x)

# You can create a global variable inside a function using the global keyword.

# You can also use the global keyboard if you want to change a global variable inside a function


def myfunc3():
    global x
    x = "wonderful"
    print("Python is " + x)


myfunc3()

print("Python is " + x)
