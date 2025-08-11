# Write  a  program  to  determine  largest  command  line  input
import sys
argv = sys.argv
if len(argv) == 1:
    print("Pls send inputs")
else:
    nums = []
    strs = []
    for arg in argv[1:]:
        try:
            val = float(arg)
            nums.append(val)
        except ValueError:
            strs.append(arg)
    if nums and strs:
        print("Inputs can not be number and string")
    elif nums:
        print("argv:", argv)
        print("a:", nums)
        largest = max(nums)
        print("Largest command line input is:", largest)
        print(f"How to determine largest element of list 'a'? ---> max(a) i.e. {largest}")
        print(f"What is the result of max(argv[1:])? ---> {max(argv[1:])}")
        print("What is the issue with max(argv[1:])? ---> Largest string is obtained but not largest number")
    elif strs:
        print("argv:", argv)
        print("a:", strs)
        largest = max(strs)
        print("Largest command line input is:", largest)
        print(f"How to determine largest element of list 'a'? ---> max(a) i.e. {largest}")
        print(f"What is the result of max(argv[1:])? ---> {max(argv[1:])}")
        print("What is the issue with max(argv[1:])? ---> Works fine for strings, but wrong for numbers")

'''output:
python prog2.py 10 20 30.8 7 40 35.6
argv: ['prog2.py', '10', '20', '30.8', '7', '40', '35.6']
a: [10.0, 20.0, 30.8, 7.0, 40.0, 35.6]
Largest command line input is: 40.0
How to determine largest element of list 'a'? ---> max(a) i.e. 40.0
What is the result of max(argv[1:])? ---> 7
What is the issue with max(argv[1:])? ---> Largest string is obtained but not largest number
'''

# Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number
import sys
n = sys.argv[1:]  # Skip the script name

if not n:
    print("Please provide numbers as command-line arguments.")
else:
    for i in n:
        try:
            num = int(i)
            if num % 2 == 0:
                print(f"{num} is Even")
            else:
                print(f"{num} is Odd")
        except ValueError:
            print(f"{i} is not a valid integer.")                                                                                                                 
''' output:
python even_odd.py 12 5 0 -3 abc 8
12 is Even
5 is Odd
0 is Even
-3 is Odd
abc is not a valid integer.
8 is Even'''

# Write  a  program  to  determine  average  of  command  line  inputs
import sys
argv = sys.argv
inputs = argv[1:]
if not inputs:
    print("Pls send number inputs")
else:
    a = []
    for i in inputs:
        if i == "True":
            a.append(True)
        elif i == "False":
            a.append(False)
        else:
            try:
                a.append(float(i))
            except ValueError:
                print("Pls send number inputs")
                break
    else:
        print("argv:", argv)
        print("a:", a)
        print("Average of inputs:", sum(a) / len(a))

'''output: 
python average.py 10.8 25 True 14.6 19 False 7.4
argv: ['average.py', '10.8', '25', 'True', '14.6', '19', 'False', '7.4']
a: [10.8, 25.0, True, 14.6, 19.0, False, 7.4]
Average of inputs: 11.114285714285714
'''

# Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order
import sys
argv = sys.argv
inputs = argv[1:]
a = []
if not inputs:
    print("Pls send some number inputs")
else:
    for arg in inputs:
        try:
            a.append(float(arg))
        except ValueError:
            print("Pls don't send number and string inputs together")
            break
    else:
        print("argv:", argv)
        print("a:", a)
        print("Ascending order:", sorted(a))
        print("Descending order:", sorted(a, reverse=True))
'''output:
python sorting.py 10 20 15.8 5 12.6
argv: ['sorting.py', '10', '20', '15.8', '5', '12.6']
a: [10.0, 20.0, 15.8, 5.0, 12.6]
Ascending order: [5.0, 10.0, 12.6, 15.8, 20.0]
Descending order: [20.0, 15.8, 12.6, 10.0, 5.0]
'''
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False

'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #Rm a
print(a [ : 7]) #Rama Ra
print(a [2 : 4]) # ma
print(a [2 : ]) # ma Ra0
print(a [ : 4 ]) # Rama
print(a [ : : 2]) # Rm a
print(a [-6 : -1]) # ma Ra
print(a [-6 : ]) # ma Rao
print(a [: -4 : -1]) # oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ]) # Rao
print(a [ : : ]) # Rama Rao
print(a [ : ]) # Rama rao
print(a [ : : -1]) # oaR amaR
print(a [ : : -2]) # oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8]) # ma Rao
print(a [2 : 8 : -1]) # Nothing is printed
print(a [ : -6 : -1]) # oaR a
print(a [2 : -3]) # ma
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5])# o
print(a [2 : -5]) # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # oaR ama
print(a [-5 : 0 : -2]) # aa

# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two characters  of  the  two  strings.Assume  that  each  string  has  a   minimum  of  two  characters
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) < 2 or len(str2) < 2:
    print("Input should be a minimum of 2 characters per string")
else:
    result = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    print(result)
'''output:
Enter first string: Java
Enter second string: Python
Pyva Jathon
Enter first string: A
Enter second string: HYD
Input should be a minimum of 2 characters per string
'''
 # Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string.Print  an  empty  string  if  string  has  less  than  four  characters
str1 = input("Enter first string: ")
if len(str1) > 4:
    result = str1[:2]+str1[-2:] 
    print(result)
else:
    print("Nothing")    
'''output:                                                                                                                                     
Enter first string: PYTHON
PYON                                                                                                                                                                 
Enter first string: H
Nothing'''
 # Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse directions  without  slice
str1 = input("Enter first string: ")
for i in range(len(str1)):
    print(f" Character at index {i}: {str1[i]}")
for i in range(len(str1) - 1, -1, -1):
    print(f" Character at index {i-len(str1)}: {str1[i]}")         
'''output:                                                                                                       
Enter first string: VAMSI
 Character at index 0: V
 Character at index 1: A
 Character at index 2: M
 Character at index 3: S
 Character at index 4: I
 Character at index -1: I
 Character at index -2: S
 Character at index -3: M
 Character at index -4: A
 Character at index -5: V'''
 # Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
str = input("Enter any string: ")
odd = ""
even = ""
for i in range(len(str)):
    if i%2==0:
        even += str[i]
    else:
        odd += str[i]
print("String at even indexes: ",odd)
print("String at even indexes: ",even)  
'''output:                                                               
Enter any string: RAMA RAO
String at even indexes:  AARO
String at even indexes:  RM A'''
# Let  input  be    A   4   B   3   C   2   $   5
#                   0   1    2   3   4   5   6   7
# What  is  the  output ?  --->  AAAABBBCC$$$$$
s = input("Enter any string with alternate character and digit: ")
if len(s) % 2 != 0:
    print("String should have alternate character and digit")
else:
    counts = []
    try:
        for i in range(1, len(s), 2):
            counts.append(int(s[i]))
        result = ""
        for i in range(0, len(s), 2):
            result += s[i] * counts[i // 2]
        print("Result:", result)
    except ValueError:
        print("String should have alternate character and digit")   
'''output:           
Enter any string with alternate character and digit: HYD
String should have alternate character and digit
Enter any string with alternate character and digit: A4B3C2$5
Result: AAAABBBCC$$$$$'''
# Write  a  program  to  merge  two  strings  to  form  a  new  string
a = input("Enter first string: ")
b = input("Enter second string: ")
c = ""
i = 0
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print("Result :", c)
'''output:
Enter first string: HYD
Enter second string: VAMSI
Result : HVYADMSI                                                                                               
Enter first string: SAIRAM
Enter second string: HYD
Result : SHAYIDRAM'''
# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
a = input("Enter a string: ")
out = ""
for ch in a:  
    if ch not in out:      
        out += ch         
print("Result:", out)
'''output:
Enter a string: MISSISIPI
Result: MISP'''
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' ')) #1
print(len('A2#')) # 3
print(len(3456)) # ERROR
print('Sec'. len()) # ERROR
# chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  #   Converts  unicode  value  90  to  'Z'
print(chr(97))  #   Converts  unicode  value  97  to  'a'
print(chr(122))  #   Converts  unicode  value  122  to  'z'
print(chr(48))  #   Converts  unicode  value  48  to  0
print(chr(57))  #   Converts  unicode  value  57  to  9
print(chr(36))  #   Converts  unicode  value  36  to  $
print(chr(32))  #   Converts  unicode  value  32  to   nothing is printed
# ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z'))  #  Converts  'Z'  to  unicode  value  90
print(ord('a'))  #  Converts  'a'  to  unicode  value  97
print(ord('z'))  #  Converts  'z'  to  unicode  value  122
print(ord('0'))  #  Converts  '0'  to  unicode  value  48
print(ord('9'))  #  Converts  '9'  to  unicode  value  57
print(ord('$'))  #  Converts  '$'  to  unicode  value  36
print(ord(' '))  #  Converts  ''  to  unicode  value  32
#Let  input  be  A4M3Z5D2
#What  is  the  output ?  --->  AEMPZ_DF
# 0     1     2     3    4    5    6     7
# A      4     M    3    Z    5    D     2
s = input("Enter any string with alternate character and digit: ")
out = ""
if len(s) % 2 != 0:
    print("Pls enter string with alternate char and digit")
else:
    for i in range(0, len(s), 2):
        if not (s[i].isalpha() and s[i+1].isdigit()):
            print("Pls enter string with alternate char and digit")
            break
        char = s[i]
        num = int(s[i+1])
        shifted = chr(ord(char) + num)
        out += char + shifted
    else:
        print("Result :", out)
'''output:
Enter any string with alternate character and digit: A4M3Z5D2
Result : AEMPZ_DF                                                                                            
Enter any string with alternate character and digit: HYD
Pls enter string with alternate char and digit'''