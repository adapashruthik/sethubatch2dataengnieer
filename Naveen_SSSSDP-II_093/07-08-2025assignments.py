#determine largest command line input
'''
from sys import argv

if len(argv) == 1:
    print('Please send inputs')
else:
    a = []
    num = str_flag = False

    for i in argv[1:]:
        try:
            a.append(float(i))
            num = True
        except:
            a.append(i)
            str_flag = True

    if num and str_flag:
        print('Inputs can not be number and string')
    else:
        print('List:', a)
        print('Largest:', max(a))
'''
#determine command line input is even number or odd number
'''
from sys import argv
print(argv)

try: 
        if int(argv[1])%2==0:
                  print('Even Number')
        else:
                  print('Odd Number')
except:
         print('Please Send an integer input')
'''
#determine average of command line
'''
from sys import argv
print(argv)

if len(argv) == 1:
    print('Pls send number inputs')
else:
    try:
        nums = []
        for x in argv[1:]:
            nums.append(eval(x))  # Caution: eval can be dangerous
        print(f'Average: {sum(nums) // len(nums)}')
    except:
        print('Pls send number inputs')
'''
#sort command line inputs ascending and descending
'''
from sys import argv
print(argv)

try:
    a = []
    for i in argv[1:]:
        a.append(eval(i))  
    print('Ascending order sort:', sorted(a))
    print('Descending order sort:', sorted(a, reverse=True))
except:
    print("Please don't send number and string inputs together")
'''
#assignment1
'''
print( 'green'   in   'Hyd  is  green  city')	#True
print('day'   in   'Sankar  dayal  sarma')	    #True
print('Green'   in   'Hyd  is  green  city')	#False
print('d  is'   in   'Hyd  is  green  city')	#True
print('dis'   in   'Hyd  is  green  city')	    #False
print('iniv'   in   'Srinivas')		            #True
print('iniv'   not   in   'Srinivas')	     	#False
'''
#assignment2
'''  (Home  work)
Slice  demo  program
0      1      2       3        4       5       6       7
R      a      m       a                R       a       o
-8    -7     -6      -5       -4      -3      -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])	#  a[ 0 :  7 : 2]   --->  string  from  indexes   0  to   6  in  steps  of  2  	i.e.  Rm<space>a
print(a [ : 7])	#  a[ 0 :  7 : 1]   --->  string  from  indexes   0  to   6  in  steps  of  1  	i.e.  Rama<space>Ra
print(a [2 : 4])	#  a[ 2 :  4 : 1]   --->  string  from  indexes   2  to   3  in  steps  of  1  	i.e.  ma
print(a [2 : ])	#  a[ 2 :  8 : 1]   --->  string  from  indexes   2  to   7  in  steps  of  1  	i.e.  ma<space>Rao
print(a [ : 4 ])	#  a[ 0 :  4 : 1]   --->  string  from  indexes   0  to   3  in  steps  of  1  	i.e.  Rama
print(a [ : : 2])	#  a[ 0 :  8 : 2]   --->  string  from  indexes   0  to   7  in  steps  of  2  	i.e.  Rm<space>a
print(a [-6 : -1])	#  a[-6 : -1 : -1] --->  string  from  indexes  -6  to  -2  in  steps  of -1  i.e.  ma<space>Ra
print(a [-6 : ])	#  a[-6 :  8 : 1]   --->  string  from  indexes  -6  to   7  in  steps  of  1  	i.e.  ma<space>Rao
print(a [: -4 : -1])	#  a[-1 : -4 : -1] --->  string  from  indexes  -1  to  -3  in  steps  of -1  i.e.  oaR
print(a [-3 : -1])	#  a[-3 : -1 :  1] --->  string  from  indexes  -3  to  -2  in  steps  of -1  i.e.  Ra
print(a [-3 : ])	#  a[-3 :  8 : 1]   --->  string  from  indexes  -3  to   7  in  steps  of  1  	i.e.  Rao
print(a [ : : ])	#  a[ 0 :  8 : 1]   --->  string  from  indexes   0  to   7  in  steps  of  1  	i.e.  Rama<space>Rao
print(a [ : ])	#  a[ 0 :  8 : 1]   --->  string  from  indexes   0  to   7  in  steps  of  1  	i.e.  Rama<space>Rao
print(a [ : : -1])	#  a[-1 : -9 : -1] --->  string  from  indexes  -1  to  -8  in  steps  of -1  i.e.  oaR<space>amaR
print(a [ : : -2])	#  a[-1 : -9 : -2] --->  string  from  indexes  -1  to  -8  in  steps  of -2  i.e.  oRaa
print(a [ -2 : : -2])	#  a[-2 : -9 : -2] --->  string  from  indexes  -2  to  -8  in  steps  of -2  i.e.  a<space>mR
print(a [2 : 8])	#  a[ 2 :  8 : 1]   --->  string  from  indexes   2  to   7  in  steps  of  1  	i.e.  ma<space>Rao
print(a [2 : 8 : -1])	#  a[ 2 :  8 :-1]   --->  string  from  indexes   2  to   7  in  steps  of -1  	i.e.  (empty)  as step is negative
print(a [ : -6 : -1])	#  a[-1 : -6 :-1]  --->  string  from  indexes  -1  to  -5  in  steps  of -1 	i.e.  oaR<space>a
print(a [2 : -3])	#  a[ 2 : -3 : 1]   --->  string  from  indexes   2  to  -4  in  steps  of  1  	i.e.  ma
print(a [1 : 6 : 2])	#  a[ 1 :  6 : 1]   --->  string  from  indexes   1  to   5  in  steps  of  2  	i.e.  aaR
print(a [ : -5 : -5])	#  a[-1 : -5 : -5] --->  string  from  indexes  -1  to  -4  in  steps  of -5 	i.e.  o
print(a [2 : -5])	#  a[ 2 : -5 : 1]   --->  string  from  indexes   2  to  -6  in  steps  of  1  	i.e.  m
print(a [2 : -5 : 2])	#  a[ 2 : -5 : 2]   --->  string  from  indexes   2  to  -6  in  steps  of  2  	i.e.  m
print(a [ : 0 : -1])	#  a[-1 :  0 : -1] --->  string  from  indexes  -1  to   1  in  steps  of -1  	i.e.  oaR<space>ama
print(a [-5 : 0 : -2])#  a[-5 :  0 : -2] --->  string  from  indexes  -5  to   1  in  steps  of -2  i.e.  aa
'''
#concatenate two strings seperated by space but swap first two
'''
s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

if len(s1) < 2 or len(s2) < 2:
    print('Input should be a min of 2-char string')
else:
    out = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result:", out)
'''
#print first two and last two characters of the string
'''
a = input('Enter any string: ')

if len(a) < 4:
	print("")
else:
   	print(a[:2] + a[-2:])
'''
#print characters of the string in forward and reverse without slice
'''
a = input("Enter any string: ")

print("Forward direction:")
for i in range(len(a)):
    print(f"Character at index {i} : {a[i]}")

print("\nReverse direction:")
for i in range(-1, -len(a)-1, -1):
    print(f"Character at index {i} : {a[i]}")
'''
#print characters at even and odd indexes without slice
'''
a = input("Enter any string: ")

even = ""
odd = ""

for i in range(len(a)):
 	if i % 2 == 0:
        		even += a[i]
else:
        		odd += a[i]

print("String at even indexes:", even)
print("String at odd indexes:", odd)
'''
#assignment3
'''
a = input("Enter any string with alternate character and digit: ")

if len(a) % 2 != 0:
    print("String should have alternate character and digit")
else:
    out = ""
    for i in range(0, len(a), 2):
        out += a[i] * int(a[i+1])
    print("Result:", out)
'''
#merge two stringd to form a new string
'''
a = input("Enter first string: ")
b = input("Enter second string: ")

i = 0
c = ""
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1

c += a[i:] + b[i:]
print("Result:", c)
'''
#remove duplicate characters of the string
'''
s = input("Enter any string: ")
out = ""

for ch in s:
    if ch not in out:
        out += ch

print("String without duplicates:", out)
'''
#len function demo program
'''
print(len('Hyd'))	    #3
print(len('Rama Rao'))	#8
print(len('9247'))	    #4
print(len('+-$'))	    #3
print(len(''))		    #0
print(len(' '))		    #1
print(len('A2#'))	    #3
print(len(3456))		# error as we can't use len for int
print('Sec'. len('12'))	# error as syntax for str len is not valid
'''
#ch() function demo 
'''
print(chr(65))	#   Converts  unicode  value  65  to  'A'
print(chr(90))	#   Converts  unicode  value  90  to  'Z'
print(chr(97))	#   Converts  unicode  value  97  to  'a'
print(chr(122))	#   Converts  unicode  value  122 to  'z'
print(chr(48))	#   Converts  unicode  value  48  to  '0'
print(chr(57))	#   Converts  unicode  value  57  to  '9'
print(chr(36))	#   Converts  unicode  value  36  to  '$'
print(chr(32))	#   Converts  unicode  value  32  to  'space'
'''
#ord() function demo
'''
print(ord('A'))	#  Converts  'A'  to  unicode  value  65
print(ord('Z'))	#  Converts  'Z'  to  unicode  value  90
print(ord('a'))	#  Converts  'a'  to  unicode  value  97
print(ord('z'))	#  Converts  'z'  to  unicode  value  122
print(ord('0'))	#  Converts  '0'  to  unicode  value  48
print(ord('9'))	#  Converts  '9'  to  unicode  value  57
print(ord('$'))	#  Converts  '$'  to  unicode  value  36
print(ord(' '))	#  Converts  ' '  to  unicode  value  32
'''
#assignment4
s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0:
    print("Pls enter string with alternate char and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] + chr(ord(s[i]) + int(s[i+1]))
    print("Result:", out)

