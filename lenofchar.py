print(len('Hyd'))        # 3          (number of characters)
print(len('Rama Rao'))   # 8          (including space)
print(len('9247'))       # 4
print(len('+-$'))        # 3
print(len(''))           # 0          (empty string)
print(len(' '))          # 1          (space is a character)
print(len('A2#'))        # 3

# The next line will cause an error because 3456 is an int, not a string
# print(len(3456))       # TypeError: object of type 'int' has no len()

# Correct way would be to convert the integer to string first:
print(len(str(3456)))    # 4

# The syntax below is invalid in Python ('.' is not used like this)
# print('Sec'. len())    # SyntaxError

# Correct way to call len on a string literal:
print(len('Sec'))        # 3
