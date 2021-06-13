# Strings

# You can display a string literal with the print() function:

print("Hello")
print("Hello You")

# Assign string to a variable

# Assigning a string to a variable is done with the variable name
# followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays

# Strings in Python are arrays of bytes representing unicode characters.

a = "Hello, World!"
print(a[1])

# Looping through a String

# Since strings are arrays, we can loop through the characters,
#  in a string with a for loop.

for x in "banana":
    print(x)

#  String length

# To get the length of a string, use the len() function.

a = "Hello David"
print(len(a))

# Check String

# To check if a certain phrase or character is present in a string,
# we can use the keyword in.

txt = "The best thins in life are free!"
print("free" in txt)

txt = "The best thins in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if not

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

# Slicing

# You can return a range of characters by using th slice syntax.
# Specify the start index and the end index, separated by a colon,
# to return a part of the string.

b = "Hello, World!"
print(b[2:5])

# Slice From the Start

# By leaving out the start index, the range will start at the first char

b = "Hello, World!"
print(b[:5])

# Slice To The End

# By leaving out the end index, the range will go to the end:

b = "Hello, World!"
print(b[2:])

# Negative Indexing

# Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])

# Modify Strings

# Upper Case

# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# Lower Case

# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

# Whitespace is the space before and/or after the actual text,
#  and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String

# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String

# The split() method returns a list where the text between
#  the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Strinf Concatenation

# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format

# We can combine strings and numbers
# #  by using the format() method!

# The format() method takes the passed arguments, formats them,
#  and places them in the string where the placeholders {} are:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments,
#  and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments
#  are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# The escape character allows you to use double
#  quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:

# Code	   Result	
# \'	   Single Quote	
# \\	   Backslash	
# \n	   New Line	
# \r       Carriage Return	
# \t	   Tab	
# \b	   Backspace	
# \f	   Form Feed	
# \ooo	   Octal value	
# \xhh	   Hex value


