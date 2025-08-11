s = input("Enter any string with alternate character and digit : ")

# Validate that input length is even (pairs of char and digit)
if len(s) % 2 != 0:
    print("Pls enter string with alternate char and digit")
else:
    result = ""
    valid = True  # Flag to check validity

    for i in range(0, len(s), 2):
        char = s[i]
        digit = s[i+1]

        # Validate char is a letter or allowed symbol (not digit)
        if not char.isalpha():
            valid = False
            break

        # Validate digit is numeric
        if not digit.isdigit():
            valid = False
            break

        # Calculate shifted character code
        # ord(char) + int(digit)
        shifted_code = ord(char) + int(digit)

        # If shifted_code goes beyond 'Z' (assuming uppercase letters),
        # you may want to wrap or just keep as is - your example leaves 'Z' + 5 as '_'
        # chr(90 + 5) = chr(95) = '_', so this fits the example.

        result += char + chr(shifted_code)

    if valid:
        print("Result  :  ", result)
    else:
        print("Pls enter string with alternate char and digit")



s = input("Enter any string with alternate character and digit : ")

# Check length of input is even (pairs of char & digit)
if len(s) % 2 != 0:
    print("String should have alternate character and digit")
else:
    result = ""
    valid = True
    for i in range(0, len(s), 2):
        char = s[i]
        digit = s[i+1]

        # Check char is alphabetic or symbol (not digit), and digit is numeric
        if not char.isalpha() and not (33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126):
            # char is neither alphabet nor common symbols (just a generic check for symbol range)
            valid = False
            break
        if not digit.isdigit():
            valid = False
            break

        result += char * int(digit)
    
    if valid:
        print("Result :  ", result)
    else:
        print("String should have alternate character and digit")




print(chr(65))   # A  (Unicode for uppercase 'A')
print(chr(90))   # Z  (Unicode for uppercase 'Z')
print(chr(97))   # a  (Unicode for lowercase 'a')
print(chr(122))  # z  (Unicode for lowercase 'z')
print(chr(48))   # 0  (Unicode for digit '0')
print(chr(57))   # 9  (Unicode for digit '9')
print(chr(36))   # $  (Unicode for dollar sign)
print(chr(32))   #   (Unicode for space character)





import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send number inputs")
else:
    inputs = argv[1:]
    a = []
    try:
        for item in inputs:
            if item == 'True':
                a.append(True)
            elif item == 'False':
                a.append(False)
            else:
                a.append(float(item))
        print("argv =", argv)
        print("List 'a' =", a)
        average = sum(a) / len(a)
        print("Average is:", round(average, 2))
    except ValueError:
        print("Pls send number inputs")






from sys import argv
print(argv)
for i in range(len(argv)):
    print(F'argv{i}={argv[i]}')




# Command line arguments demo program
from sys import argv
print(argv) # ['progla.py', '25', 'Rama Rao', '10000.0', 'm', 'True']
print(type(argv)) # <class 'list'>
for i in range(len(argv)): # Each element of argv list along with index
    print(f'argv[ {i} ] : {argv[i]}')
print('argv list without filename : ', argv[1:]) # ['25', 'Rama Rao', '10000.0', 'm', 'True']
print('Number of inputs : ', len(argv) - 1) # 5



import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send number inputs")
else:
    inputs = argv[1:]
    a = []
    all_numbers = True
    for item in inputs:
        try:
            num = float(item)
            a.append(num)
        except ValueError:
            all_numbers = False
            break
    if not all_numbers:
        print("Pls don't send number and string inputs together")
    else:
        print("argv =", argv)
        print("List 'a' =", a)
        print("Sorted list (ascending):", sorted(a))
        print("Sorted list (descending):", sorted(a, reverse=True))



a = 'Rama Rao'

print(a[:7:2])      # Rm a
print(a[:7])        # Rama Ra
print(a[2:4])       # ma
print(a[2:])        # ma Rao
print(a[:4])        # Rama
print(a[::2])       # Rm a
print(a[-6:-1])     # ma Ra
print(a[-6:])       # ma Rao
print(a[:-4:-1])    # oaR
print(a[-3:-1])     # Ra
print(a[-3:])       # Rao
print(a[:])         # Rama Rao
print(a[::])        # Rama Rao
print(a[::-1])      # oaR am aR
print(a[::-2])      # oRaa
print(a[-2::-2])    # a mR
print(a[2:8])       # ma Rao
print(a[2:8:-1])    # 
print(a[:-6:-1])    # oaR a
print(a[2:-3])      # ma 
print(a[1:6:2])     # aaR
print(a[:-5:-5])    # o
print(a[2:-5])      # m
print(a[2:-5:2])    # 
print(a[:0:-1])     # oaR am
print(a[-5:0:-2])   # aa




def compare_two_inputs():
    try:
        input1_str = input("Enter the first input for comparison: ")
        input2_str = input("Enter the second input for comparison: ")

        val1 = eval(input1_str)
        val2 = eval(input2_str)

        # Use a ternary operator to determine the comparison result
        result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')

        print(f"Comparing {val1} and {val2}: {result}")

    except SyntaxError:
        print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
    except NameError as e:
        print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
    except TypeError as e:
        print(f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Program to determine the sign of a number (+1, -1, or 0).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")






try:
    a=int(input("Enter a number[1-7]: "))
    if a==1:
        print("Sunday")
    elif a==2:
        print("Monday")
    elif a==3:
        print("Tuesday")
    elif a==4:
        print("Wednesday")
    elif a==5:
        print("Thursday")
    elif a==6:
        print("Friday")
    elif a==7:
        print("Saturday")
    else:
        print("Invalid day")
except:
    print("Enter only number from 1-7")  





x=10
y=20
z=x
if (1):
    del x
    print("successfully deleted")
print(z)




x=[10,20,30,40,50]
print(x)
del x[0]
print(x)
del x[1:3]
print(x)




class Geek:
    domain="www.amazon.com"

geeks= Geek()
print(geeks.domain)
del Geek.domain
print("geeks.domain")




try:
    num=int(input('Enter a number from[0-9]: '))
    if num==0:
        print('zero')
    elif num==1:
        print('one')
    elif num==2:
        print('two')
    elif num==3:
        print('three')  
    elif num==4:
        print('four')
    elif num==5:
        print('five')
    elif num==6:
        print('six')    
    elif num==7:
        print('seven')
    elif num==8:
        print('eight')
    elif num==9:
        print('nine')
    else:
        print('Invalid input, please enter a number between 0 and 9.')
except:
    print('An error occurred. Please enter a valid number.')




# Input string
s = input("Enter a string: ")

# Print characters in forward direction with positive indices
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

print()  # Blank line

# Print characters in reverse direction with negative indices
for i in range(1, len(s) + 1):
    print(f"Character at index {-i} : {s[-i]}")





# Input string from user
s = input("Enter any string : ")

out = ""  # To store characters without duplicates

for char in s:
    if char not in out:
        out += char  # Concatenate if char not already in out

print("String without duplicates : ", out)





import sys

argv = sys.argv

if len(argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(argv[1])
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")





# Input string from user
s = input("Enter any string : ")

even_chars = ""  # to hold chars at even indexes
odd_chars = ""   # to hold chars at odd indexes

# Loop over all indexes and characters
for i in range(len(s)):
    if i % 2 == 0:
        even_chars += s[i]
    else:
        odd_chars += s[i]

print("String at even indexes : " + even_chars)
print("String at odd indexes : " + odd_chars)





import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send inputs")
else:
    inputs = argv[1:]
    # Try to convert all inputs to float
    all_numbers = True
    all_strings = True
    a = []
    for item in inputs:
        try:
            num = float(item)
            a.append(num)
            all_strings = False
        except ValueError:
            a.append(item)
            all_numbers = False

    if all_numbers:
        print(f"argv = {argv}")
        print(f"List 'a' = {a}")
        print(f"Largest command line input is: {max(a)}")
        print(f"max(argv[1:]) = {max(argv[1:])}")  # Shows string comparison
        print("Issue with max(argv[1:])? ---> Largest string is obtained but not largest number")
    elif all_strings:
        print(f"Largest command line input is: '{max(a)}'")
    else:
        print("Inputs can not be number and string mixed")





# Program to determine the largest of three inputs without using the max() function.
# This program uses a nested ternary operator for finding the largest value.
print("--- Determine the Largest of Three Inputs ---")

# Function to get input and determine the largest using a nested ternary operator
def find_largest_of_three():
    try:
    # Get three inputs from the user
    # Using eval() for flexibility as inputs can be numbers, strings, lists, etc.
    # NOTE: eval() carries security risks if used with untrusted input.
    # For this homework, it's used to match the varied input types.
    input1_str = input("Enter the first input for largest of three: ")
    input2_str = input("Enter the second input for largest of three: ")
    input3_str = input("Enter the third input for largest of three: ")

    val1 = eval(input1_str)
    val2 = eval(input2_str)
    val3 = eval(input3_str)

    # Determine the largest using a nested ternary operator
    # Logic:
    # If val1 is greater than val2:
    #   Then compare val1 with val3. If val1 > val3, val1 is largest, else val3 is largest.
    # Else (val2 is greater than or equal to val1):
    #   Then compare val2 with val3. If val2 > val3, val2 is largest, else val3 is largest.
    largest = val1 if val1 > val2 else val2
    largest = largest if largest > val3 else val3

    # Alternatively, a single nested ternary (more compact but harder to read for complex logic):
    # largest = val1 if val1 > val2 and val1 > val3 \
    #           else (val2 if val2 > val1 and val2 > val3 else val3)
    # A simpler single line for three distinct values:
    # largest = val1 if val1 > val2 and val1 > val3 else \
    #           (val2 if val2 > val3 else val3)


    print(f"The inputs are: {val1}, {val2}, {val3}")
    print(f"The largest value is: {largest}")
except SyntaxError:
    print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
    print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
    print(f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to print '>', '<', or '=' based on the comparison of two inputs.
# This program uses a ternary operator.
print("\n--- Compare Two Inputs ---")

def compare_two_inputs():
try:
    input1_str = input("Enter the first input for comparison: ")
    input2_str = input("Enter the second input for comparison: ")

    val1 = eval(input1_str)
    val2 = eval(input2_str)

    # Use a ternary operator to determine the comparison result
    result = '>' if val1 > val2 else ('<' if val1 < val2 else '=')

    print(f"Comparing {val1} and {val2}: {result}")

except SyntaxError:
    print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
    print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except TypeError as e:
    print(f"Comparison Error: {e}. Ensure inputs are comparable types (e.g., all numbers, all strings, or all lists).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine the sign of a number (+1, -1, or 0).
# This program uses a nested ternary operator.
print("\n--- Determine Number Sign ---")

def determine_sign():
try:
    num_str = input("Enter a number to determine its sign: ")
    num = float(num_str) # Convert to float to handle decimals and integers

    # Use a nested ternary operator to determine the sign
    # Logic:
    # If num > 0, result is 1
    # Else (num <= 0):
    #   If num < 0, result is -1
    #   Else (num == 0), result is 0
    sign = 1 if num > 0 else (-1 if num < 0 else 0)

    print(f"The sign of {num} is: {sign}")

except ValueError:
    print("Invalid input: Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to test if an input number is even or odd.
# This program uses a ternary operator.
print("\n--- Check Even or Odd Number ---")

def check_even_odd():
try:
    num_str = input("Enter an integer to check if it's even or odd: ")
    num = int(num_str) # Convert to integer

    # Use a ternary operator to determine if the number is even or odd
    # An even number is divisible by 2 (remainder is 0).
    # An odd number is not divisible by 2 (remainder is not 0).
    result = "Even" if num % 2 == 0 else "Odd"

    print(f"The number {num} is: {result}")

except ValueError:
    print("Invalid input: Please enter a valid integer number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine area and perimeter of a rectangle.
print("\n--- Calculate Rectangle Area and Perimeter ---")

def calculate_rectangle_properties():
try:
    length_str = input("Enter the length of the rectangle: ")
    breadth_str = input("Enter the breadth of the rectangle: ")

    length = float(length_str)
    breadth = float(breadth_str)

    if length < 0 or breadth < 0:
        print("Length and breadth cannot be negative.")
        return

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f"For a rectangle with length {length} and breadth {breadth}:")
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

except ValueError:
    print("Invalid input: Please enter valid numbers for length and breadth.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine the volume of a sphere.
import math # Import math module for pi and power

print("\n--- Calculate Sphere Volume ---")

def calculate_sphere_volume():
try:
    radius_str = input("Enter the radius of the sphere: ")
    radius = float(radius_str)

    if radius < 0:
        print("Radius cannot be negative.")
        return

    # Volume of sphere formula: (4/3) * pi * r^3
    volume = (4/3) * math.pi * (radius ** 3)

    print(f"For a sphere with radius {radius}:")
    print(f"Volume = {volume}")

except ValueError:
    print("Invalid input: Please enter a valid number for the radius.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to determine simple interest and compound interest.
print("\n--- Calculate Simple and Compound Interest ---")

def calculate_interest():
try:
    principal_str = input("Enter the principal amount (P): ")
    time_str = input("Enter the time in years (T): ")
    rate_str = input("Enter the annual rate of interest (R, as a percentage): ")

    principal = float(principal_str)
    time = float(time_str)
    rate = float(rate_str)

    if principal < 0 or time < 0 or rate < 0:
        print("Principal, time, and rate cannot be negative.")
        return

    # Simple Interest Formula: (P * T * R) / 100
    simple_interest = (principal * time * rate) / 100

    # Compound Interest Formula: P * (1 + R / 100)^T - P
    # Note: (1 + R/100) is the growth factor per period
    compound_interest = principal * ((1 + rate / 100) ** time) - principal

    print(f"For Principal = {principal}, Time = {time} years, Rate = {rate}%:")
    print(f"Simple Interest = {simple_interest:.2f}") # Format to 2 decimal places
    print(f"Compound Interest = {compound_interest:.2f}") # Format to 2 decimal places

except ValueError:
    print("Invalid input: Please enter valid numbers for principal, time, and rate.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Program to swap values of two objects using a third object.
print("\n--- Swap Two Objects (using a third object) ---")

def swap_with_third_object():
try:
    # Get two inputs from the user
    # Using eval() for flexibility as inputs can be numbers, strings, lists, etc.
    # NOTE: eval() carries security risks if used with untrusted input.
    input_x_str = input("Enter the value for x: ")
    input_y_str = input("Enter the value for y: ")

    x = eval(input_x_str)
    y = eval(input_y_str)

    print(f"Before swap: x = {x}, y = {y}")

    # Perform the swap using a third temporary variable
    temp = x
    x = y
    y = temp

    print(f"After swap: x = {x}, y = {y}")

except SyntaxError:
    print("Invalid input: Please ensure inputs are valid Python literals (e.g., 10, 3.5, 'text', [1,2]).")
except NameError as e:
    print(f"Invalid input: {e}. If entering strings, enclose them in quotes (e.g., 'RAMA').")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# --- Call the functions to run the programs ---

# Call the function to run the largest of three program with user input
find_largest_of_three()

# Call the function to run the two input comparison program with user input
compare_two_inputs()

# Call the function to run the number sign determination program with user input
determine_sign()

# Call the function to run the even/odd check program with user input
check_even_odd()

# Call the function to run the rectangle properties calculation program with user input
calculate_rectangle_properties()

# Call the function to run the sphere volume calculation program with user input
calculate_sphere_volume()

# Call the function to run the interest calculation program with user input
calculate_interest()

# Call the function to run the swap with third object program with user input
swap_with_third_object()




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





try:
    a=int(input("Enter a month[1-12]: "))
    if a==1:
        print("January")
    elif a==2:
        print("February")
    elif a==3:
        print("March")
    elif a==4:
        print("April")
    elif a==5:
        print("May")
    elif a==6:
        print("June")
    elif a==7:
        print("July")
    elif a==8:
        print("August")
    elif a==9:
        print("September")
    elif a==10:
        print("October")
    elif a==11:
        print("November")
    elif a==12:
        print("December")
    else:
        print("Invalid month")
except:
    print("Invalid input")





print(ord('A'))  # 65   (Unicode/ASCII for uppercase 'A')
print(ord('Z'))  # 90   (Unicode/ASCII for uppercase 'Z')
print(ord('a'))  # 97   (Unicode/ASCII for lowercase 'a')
print(ord('z'))  # 122  (Unicode/ASCII for lowercase 'z')
print(ord('0'))  # 48   (Unicode/ASCII for digit '0')
print(ord('9'))  # 57   (Unicode/ASCII for digit '9')
print(ord('$'))  # 36   (Unicode/ASCII for dollar sign)
print(ord(' '))  # 32   (Unicode/ASCII for space character)





def print_full_pyramid(num_lines):
    """
    Prints a full pyramid pattern of asterisks.

    Args:
        num_lines (int): The number of lines (rows) for the pyramid.
    """
    if num_lines <= 0:
        print("Please enter a positive number of lines.")
        return

    # Outer loop for the number of rows
    for i in range(1, num_lines + 1):
        # Print leading spaces
        # The number of spaces decreases with each row
        # For n lines, the first row has (n-1) spaces, second (n-2), etc.
        # This can be calculated as num_lines - i
        print(" " * (num_lines - i), end="")

        # Print asterisks
        # The number of asterisks increases by 2 with each row
        # For row i, the number of asterisks is (2 * i - 1)
        print("*" * (2 * i - 1))

# Get input from the user
try:
    lines = int(input("Enter the number of lines for the pyramid: "))
    print_full_pyramid(lines)
except ValueError:
    print("Invalid input. Please enter an integer.")




s = input("Enter a string: ")

if len(s) < 4:
    print("")  # empty string
else:
    result = s[:2] + s[-2:]
    print(result)




# Program to concatenate two strings swapping their first two characters

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) < 2 or len(str2) < 2:
    print("Input should be a min of 2-char string")
else:
    # Swap first two characters
    # New first string = first two chars of str2 + rest of str1 from index 2
    new_str1 = str2[:2] + str1[2:]
    # New second string = first two chars of str1 + rest of str2 from index 2
    new_str2 = str1[:2] + str2[2:]
    
    # Concatenate with a space
    result = new_str1 + " " + new_str2
    
    print("Result  :  ", result)






x=int(input("enter the x value:"))
y=int(input("enter the y value:"))
print('values before swap:',x ,y )
x,y=y,x
print('values after swap:',x ,y )





try:
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    print(f'Before swap: {a} \t {b}')
    a=a+b
    b=a-b   
    a=a-b
    print(f'After swap: {a} \t {b}')
except ValueError:
    print('Invalid input, please enter valid integers.')






try:
    x=int(input("Enter the x value: "))
    y=int(input("Enter the y value: "))
    print(f'Before swap: {x} \t {y}')
    x=x*y
    y=x//y
    x=x//y          
    print(f'After swap: {x} \t {y}')
except ValueError:
    print('Invalid input, please enter valid integers.')    




try:
    x=int(input("Enter the x value: "))
    y=int(input("Enter the y value: "))         
    print('values before swap:', x, y)
    temp=x
    x=y
    y=temp
    print('values after swap:', x, y)
except ValueError:
    print('Invalid input, please enter valid integers.')





print(a:= 25)
a=36
while(a<10):
    print(a)
    print(25)
    print(a)




try:
    sum = ctr = 0
    while True:
        if (x := eval(input('Enter input (ctrl + z to stop): '))):
            sum += x
            ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input cannot be string')






