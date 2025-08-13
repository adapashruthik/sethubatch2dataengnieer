#ADAPA SHRUTHIK
#Largest Command line input
import sys
if len(sys.argv) == 1:
    print("Pls send inputs")
else:
    try:
        a = [float(i) for i in sys.argv[1:]]
        print("Largest command line input :", max(a))
    except ValueError:
        # If all inputs are strings (non-numeric)
        if all(i.isalpha() for i in sys.argv[1:]):
            print("Largest command line input :", max(sys.argv[1:]))
        else:
            print("Inputs can not be number and string")

#Even or Odd Command line input
import sys

if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        n = int(sys.argv[1])
        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")

#Average Command line input
import sys

if len(sys.argv) == 1:
    print("Pls send number inputs")
else:
    try:
        a = [float(i) for i in sys.argv[1:]]
        print("Average of command line inputs:", sum(a) / len(a))
    except ValueError:
        print("Pls send number inputs")

#Sort Command line input
import sys

if len(sys.argv) == 1:
    print("Pls send inputs")
else:
    try:
        a = [float(i) for i in sys.argv[1:]]
        print("Ascending order :", sorted(a))
        print("Descending order:", sorted(a, reverse=True))
    except ValueError:
        print("Pls don't send number and string inputs together")

#Swap first ts1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result :", result)

#First two and last two characters
s = input("Enter any string: ")

if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])

#Characters in Forward and Reverse order
s = input("Enter any string: ")

for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")

#Characters at even and odd indexes
s = input("Enter any string: ")

even = ""
odd = ""

for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]

print("String at even indexes :", even)
print("String at odd indexes  :", odd)

#Repeat characters by following digit 

s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("String should have alternate character and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] * int(s[i+1])
    print("Result :", out)

#Merge two strings alternatively 
a = input("Enter first string: ")
b = input("Enter second string: ")

c = ""
i = 0
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1

c += a[i:] + b[i:]
print("Result :", c)

#Remove duplicates in characters without set
s = input("Enter any string: ")

out = ""
for ch in s:
    if ch not in out:
        out += ch

print("String without duplicates :", out)

#Alternate character and digit 

s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("Pls enter string with alternate char and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] + chr(ord(s[i]) + int(s[i+1]))
    print("Result :", out)
print('green' in 'Hyd  is  green  city')  # True
print('day' in 'Sankar  dayal  sarma')    # True
print('Green' in 'Hyd  is  green  city')  # False
print('d  is' in 'Hyd  is  green  city')  # True
print('dis' in 'Hyd  is  green  city')    # False
print('iniv' in 'Srinivas')               # True
print('iniv' not in 'Srinivas')           # False
a = 'Rama Rao'
print(a[:7:2])       # 'RmRo'
print(a[:7])         # 'Rama Ra'
print(a[2:4])        # 'ma'
print(a[2:])         # 'ma Rao'
print(a[:4])         # 'Rama'
print(a[::2])        # 'RmRo'
print(a[-6:-1])      # 'ma Ra'
print(a[-6:])        # 'ma Rao'
print(a[:-4:-1])     # 'oa '
print(a[-3:-1])      # 'ao'
print(a[-3:])        # 'ao'
print(a[::])         # 'Rama Rao'
print(a[:])          # 'Rama Rao'
print(a[::-1])       # 'oaR amaR'
print(a[::-2])       # 'oRaR'
print(a[-2::-2])     # 'a mR'
print(a[2:8])        # 'ma Rao'
print(a[2:8:-1])     # '' (empty string)
print(a[:-6:-1])     # 'oaR'
print(a[2:-3])       # 'ma '
print(a[1:6:2])      # 'aaR'
print(a[:-5:-5])     # 'o'
print(a[2:-5])       # 'm'
print(a[2:-5:2])     # 'm'
print(a[:0:-1])      # 'oaR ama'
print(a[-5:0:-2])    # 'a m'
print(len('Hyd'))       # 3
print(len('Rama Rao'))  # 8
print(len('9247'))      # 4
print(len('+-$',))      # 3
print(len(''))          # 0
print(len(' '))         # 1
print(len('A2#'))       # 3
# print(len(3456))      # TypeError: object of type 'int' has no len()
# print('Sec'. len())   # SyntaxError
print(chr(65))   # 'A'
print(chr(90))   # 'Z'
print(chr(97))   # 'a'
print(chr(122))  # 'z'
print(chr(48))   # '0'
print(chr(57))   # '9'
print(chr(36))   # '$'
print(chr(32))   # ' '

print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32