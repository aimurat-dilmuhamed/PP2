# This is a comment.
# Python uses indentation to indicate a block of code.

if 5 > 2:
    print("Five is greater than two!")

# If you skip the indentation, Python will give you a syntax error.
x = 5           # x is of type int
y = "John"      # y is of type str
z = 4.0         # z is of type float

print(x)
print(y)
print(z)

# Get the data type of a variable
print(type(x))
print(type(y))
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10
scientific_num = 35e3
print(scientific_num)
# Integers: constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats: constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
a = float(1)     # a will be 1.0
b = float("4.2") # b will be 4.2

# Strings: constructs a string from a wide variety of data types, including strings, integer literals and float literals
c = str("s1") # c will be 's1'
d = str(2)    # d will be '2'

print(x, y, z)
print(a, b)
print(c, d)
# Simple string assignment
greeting = "Hello"
print(greeting)

# Multiline Strings using three quotes
multiline_text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_text)

# Strings are Arrays: Get the character at position 1
a = "Hello, World!"
print(a[1])

# Check String Length
print(len(a))

# Check if a phrase is present in a string
txt = "The best things in life are free!"
print("free" in txt)
