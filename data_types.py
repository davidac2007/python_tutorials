# Built- in data types

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''
# Getting data types by using th type() function

x = 5
print(type(x))

# Setting the Data Type

# str
x = "Hello World"

# int
x = 20

# float
x = 20.5

# complex
x = 1j

# list
x = ["apple", "banana", "cherry"]

# tuple
x = ("apple", "banana", "cherry")

# range
range(6)

# dict
x = {"name": "John", "age": 36}

# set
x = {"apple", "banana", "cherry"}

# frozenset
x = frozenset({"apple", "banana", "cherry"})

# bool
x = True

# bytes
x = b"Hello"

# bytearray
x = bytearray(5)

# memoryview
x = memoryview(bytes(5))
