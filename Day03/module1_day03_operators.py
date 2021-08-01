"""
    Author:         Daniel-TheProgrammer
    Description:    Learn about the basics around operators in python.
"""

# Numeric Functionality:
# Use the `+` for addition.
print(10 + 6)
# Use the `-` for subtraction.
print(10 - 6)
# Use the `*` for multiplication.
print(10 * 6)
# Use the `/` for division. The results are always a floating point number.
print(10 / 6)
# Use the `//` for integer division results (rounded down).
print(10 // 6)
# Use the `**` for exponents.
print(10 ** 6)
# 7. Use the `%` for the remainder of the division.
print(10 % 6)
# Python uses PEMDAS to complete numerical calculations.
print(8 * (2 + 2) + 3 ** 2 + 1)
# If a floating point number is generated by the equation or is used as an input, the result will be a floating point
# number.
print(10 // 6.0)

# String Functionality:
# Use the `+` to concatenate strings.
print("Python" + ": It's a fun language to learn")
# Use the `\` to escape special character.
print("\"This is a quote.\"")
print("C:\\newFolder")
# Use the `"` or `'` to quote strings. Single and double quotes work in the same fashion, but the start and end quotes
# must match. If double quotes are used, single quotes within the string do not need to be escaped.
print("That's right. Python is cool.")
# Use the `"""` or `'''` to block quote strings. Triple quotes are used as a block quote. The newline will be applied
# automatically. Additionally, triple quotes can be used at the beginning of the python code as a block comment. This is
# an excellent way to document the script with the purpose.
print("""This is a
block quote""")
# Use multiplication (`*`) to repeat a string.
print("Rudy " * 5)

# Newlines and Tabs:
# Add `\n` for a newline in a string.
print("This doesn't have to stay\non one line")
# Add `\t` for a tab in a string.
print("\tThe text can also be indented")
# Use the `r` before the quote to print the raw string.
print("C:\newFolder")
print(r"C:\newFolder")

# Relational Operators:
# Use the `==` operator to return True if the two expressions are equal and False if they are different.
print(1 == 1)
print(1 == 2)
# Use the `!=` operator to return True if the two expressions are not equal and False if they are the same.
print(1 != 1)
print(1 != 2)
# Use the `>` operator to return True if the left operand is greater than the right operand and False otherwise.
print(1 > 1)
print(1 > 2)
# Use the `>=` operator to return True if the left operand is greater than or equal to the right operand and False
# otherwise.
print(1 >= 1)
print(1 >= 2)
# Use the `<` operator to return True if the left operand is less than the right operand and False otherwise.
print(1 < 1)
print(1 < 2)
# Use the `<=` operator to return True if the left operand is less than or equal to the right operand and False
# otherwise.
print(1 <= 1)
print(1 <= 2)

# Boolean Operators:
# The `and` operator returns False unless all conditions are True.
print(True and False)
# The `or` operator returns True unless all of the conditions are False.
print(True or False)
# The `not` operator returns the inverse of the boolean expression.
print(not True)
