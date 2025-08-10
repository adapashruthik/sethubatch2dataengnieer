import sys

argv = sys.argv

if len(argv) == 1:  # No inputs given
    print("Pls send inputs")
else:
    inputs = argv[1:]  # Exclude program name
    
    # Try to convert all to float
    try:
        a = [float(x) for x in inputs]  # Convert all to numbers
        print("Largest command line input:", max(a))
    except ValueError:
        # If not all numbers, check if all are strings
        all_strings = all(x.isalpha() for x in inputs)
        if all_strings:
            print("Largest command line input:", max(inputs))
        else:
            print("Inputs can not be number and string")


import sys

argv = sys.argv

# Case 3: No input given
if len(argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(argv[1])  # Will fail for floats and strings
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        # Case 4 & 5: Not an integer
        print("Pls send an integer input")

True
True
False
True
False
True
False

print(len('Hyd'))       # 3 characters → 3
print(len('Rama Rao'))  # 8 characters (space counted) → 8
print(len('9247'))      # 4 characters → 4
print(len('+-\$'))       # 3 characters → 3
print(len(''))          # Empty string → 0
print(len(' '))         # One space → 1
print(len('A2#'))       # 3 characters → 3
print(len(3456))        # ❌ ERROR — int is not iterable
print('Sec'. len())     # ❌ ERROR — invalid syntax

print(chr(65))   # Unicode 65 → 'A'
print(chr(90))   # Unicode 90 → 'Z'
print(chr(97))   # Unicode 97 → 'a'
print(chr(122))  # Unicode 122 → 'z'
print(chr(48))   # Unicode 48 → '0'
print(chr(57))   # Unicode 57 → '9'
print(chr(36))   # Unicode 36 → '$'
print(chr(32))   # Unicode 32 → ' ' (space)



