'''
#program to determine command line input is even number or odd number
from sys import argv
print(argv)
try:
    x=int(argv[1])
    if x%2==0:
        print("Even number")
    else:
        print("odd number")
except:
    print("pls send an integer input")
print()

#program to determine average of command line inputs
from sys import argv
print(argv)
a = []
if len(argv)==1:
    print("pls send number inputs")
else:
    try:
        for i in range(1,len(argv)):
            x=argv[i]
            if '.' in argv[i]:
                x=float(argv[i])
                a.append(x)
            elif x.lower()=='true':  
                a.append(True)
            elif x.lower()=='false':
                a.append(False)
            else:   
                x=int(argv[i])
                a.append(x)    
        print('sum of list elements:' ,sum(a))
        print("number of list elements:",len(a))
        print("average of command line inputs: ",sum(a)/len(a))

    except:
        print("pls send number inputs")

print()
#program to sort command line  inputs in ascending order and descending order
from sys import argv
print(argv)
a=[]
try:
    for i in range(1,len(argv)):
        if '.' in argv[i]:
            x=float(argv[i])
            a.append(x)
        else:
            x=int(argv[i])
            a.append(x)
    print("Ascending order of a :",sorted(a))
    print("descending order of a :",sorted(a,reverse=True))
except:
    print("pls don't send number and string inputs together")
print()

# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')  # True  : 'green' is a substring of 'Hyd is green city'
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city')  # True
print('dis'   in   'Hyd  is  green  city')  #  False
print('iniv'   in   'Srinivas')  # True
print('iniv'   not   in   'Srinivas')  # False  :  'iniv' is a substring of 'Srinivas'

print()
(Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1

a = 'Rama Rao'
print(a [ : 7 : 2])  # a[0:7:2] : string from indexes o to 6 in steps of 2 i.e., Rm a
print(a [ : 7])  #  a[0:7:1] : string from indexes o to 6 in steps of 1 i.e., Rama Ra
print(a [2 : 4])  #  a[2:4:1]  : string from indexes 2 to 3 in steps of 1 i.e., ma
print(a [2 : ])  #  a[2:8:1]   : string from indexes 2 to 7 in steps of 1 i.e., ma Rao
print(a [ : 4 ])  #  a[0:4:1]  :  string from indexes 0 to 3 in steps of 1 i.e., Rama
print(a [ : : 2])   #  a[0:8:2]  : string from indexes 0 to 7 in steps of 2 i.e., Rm a
print(a [-6 : -1])   #  a[-6:-1:1]  : string from indexes -6 to -2 in steps of 1 i.e., ma Ra
print(a [-6 : ])  #   a[-6:0:1]  :  string from indexes  -6 to -1 in steps of 1 i.e., ma Rao
print(a [: -4 : -1])  #  a[-1:-4:-1]  :  string from indexes -1 to -3 in steps of i.e., oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])  #  a[-3: :1]  :  string from indexes   -3 to -1  in steps of 1 i.e., Rao
print(a [ : : ])   #  a[0:8:1]  :  string from indexes   o to 7  in steps of 1 i.e., Rama Rao
print(a [ : ])  #  a[0:8:1]  :  string from indexes    o to 7  in steps of i.e., Rama Rao
print(a [ : : -1])   #   a[-1:-9:1]  :  string from indexes -1 to -8 in steps of i.e., oaR amaR
print(a [ : : -2])   #   a[-1:-9:-2]  :  string from indexes   -1 to -8 in steps of i.e., oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])  #  a[2:8:1]  :  string from indexes  2 to 7 in steps of 1 i.e., ma Rao
print(a [2 : 8 : -1])    #   empty string
print(a [ : -6 : -1])     #   a[-1:-6:-1]  :  string from indexes  -1 to -5 in steps of -1 i.e., oaR a
print(a [2 : -3])  #  a[2:-3:1]  : string from indexes 2 to -3 in steps of 1 i.e., ma<>space
print(a [1 : 6 : 2])  #  a[1:6:2]  :  string from indexes   1 to 7  in steps of 2 i.e., aaR
print(a [ : -5 : -5])   #  a[-1:-5:-5]  :  string from indexes   -1 to -4  in steps of -5 i.e.,  o
print(a [2 : -5])   #   a[2:-5:1]  :  string from indexes   2 to  -6 in steps of 1 i.e., m
print(a [2 : -5 : 2])   #  a[2:-5:2]  :  string from indexes  2 to -6 in steps of 2i.e., m
print(a [ : 0 : -1])  #  a[7:0:-1]  :  string from indexes  7 to 1 in steps of-1 i.e., oaR ama
print(a [-5 : 0 : -2])   #  a[-5:9:-2]  :  string from indexes  -5 to 1 in steps of -2 i.e., aa

#program to concatenate two strings separated by space but swap first two char of the two strings
x=input("Enter First string : ")
y=input("Enter second string : ")
if len(x)>=2 and len(y)>=2:
    print(x[0:2]+y[2:len(y)+1] +" "+ y[0:2]+x[2:len(x)+1])
else:
    print("Input should be a min of 2-character string")
    
#program to print first two and last two characters of the string print an empty string if string has less than four characters
x=input("Enter a string : ")
if len(x)<4:
    print()
else:
    print(x[0:2] + x[-2:len(x):1])

print()
#program to print characters of the string in forward and reverse directions without slice
x=input("Enter a string : ")
for i in range(0,len(x),1):
    print(F"character at index {i} :",x[i])
for i in range(-1,-len(x)-1,-1):
    print(F"character at index {i} :",x[i])

#program to print chracters at even and odd indexes without slice
x=input("Enter a string : ")
even=''
odd=''
for i in range(0,len(x),1):
    if i%2==0:
        even+=x[i]
    else:
        odd+=x[i]
print("string at even indexes :",even)
print("string at odd indexes :",odd)

print()
#program to print characters at even and odd indexes without slice 
x=input("enter any string with alternative character and digit :")
result=''
try:
    for i in range(0,len(x),1):
        if i%2==0:
            y=x[i]*int(x[i+1])
            result+=y
    print(result)
except:
    print("string should have alternative character and digit")

#program to merge two strings to form a new string
x=input("Enter first string :")
y=input("Enter second string :")
result=''
i=0
while i<len(x) and i<len(y):
    result+=x[i]+y[i]
    i+=1
result+=x[i:]+y[i:]
print(result)


#program to remove duplicate characters from a string without using set
x=input("Enter a string : ")
result=''
for i in range(0,len(x),1):
    if x[i] not in result:
        result+=x[i]
print("String without duplicate  : ",result)

# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao')) # 8
print(len('9247'))  #  4
print(len('+-$'))  #  3
print(len(''))  #  0
print(len(' '))  #  1
print(len('A2#'))  #  3
#print(len(3456)) #  error
print('Sec'. len())  #  error : string has no attribute length

# chr()  function  demo  program
print(chr(65))  #   Converts  unicode  value  65  to  'A'
print(chr(90))  #   Converts  unicode  value  90  to  'Z'
print(chr(97))  #   Converts  unicode  value  97  to  'a'
print(chr(122))  #   Converts  unicode  value  122  to  'z'
print(chr(48))  #   Converts  unicode  value  48  to  '0'
print(chr(57))  #   Converts  unicode  value  57  to  '9'
print(chr(36))  #   Converts  unicode  value  36  to  '$'
print(chr(32))  #   Converts  unicode  value  32  to  ' '

# ord()  function  demo  program
print(ord('A'))  #  Converts  'A'  to  unicode  value  65
print(ord('Z'))  #  Converts  'Z'  to  unicode  value  90
print(ord('a'))  #  Converts  'a'  to  unicode  value  97
print(ord('z'))  #  Converts  'z'  to  unicode  value  122
print(ord('0'))  #  Converts  '0'  to  unicode  value  48
print(ord('9'))  #  Converts  '9'  to  unicode  value  57
print(ord('$'))  #  Converts  '$'  to  unicode  value  36
print(ord(' '))  #  Converts  ' '  to  unicode  value  32

x=input("Enter any string with alternative character and digit : ")
result=''
try:
    for i in range(0,len(x)):
        if i%2==0:
            result+=x[i]+chr(ord(x[i]) + int(x[i+1]))
    print(result)
except:
    print("pls enter string with alternate char and digit")
'''
#program to find largest command line input
from sys import argv
print(argv)
if len(argv) == 1:
    print("Please send inputs")
else:
    all_numbers = True
    all_strings = True
    a = []
    for arg in argv[1:]:
        try:
            x = float(arg)
            a.append(x)
            all_strings = False  
        except ValueError:
            a.append(arg)
            all_numbers = False  
    if all_numbers:
        print("Largest command input:", max(a))
    elif all_strings:
        print("Largest command input:", max(a))
    else:
        print("Inputs cannot be  numbers and strings")