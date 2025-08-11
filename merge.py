# Input two strings from the user
a = input("Enter first string : ")
b = input("Enter second string : ")

c = ""  # Result string
i = 0   # Index for iteration

# Loop until the end of the shorter string
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1

# Append remaining characters of the longer string
if i < len(a):
    c += a[i:]
elif i < len(b):
    c += b[i:]

print("Result  :  ", c)
