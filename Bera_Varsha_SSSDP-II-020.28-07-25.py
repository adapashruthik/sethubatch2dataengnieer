'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
																		 = 39 / 61 + 2j / 61											   
'''
# n1 = complex(input("Enter the first number"))
# n2=complex(input("Enter the second number"))
# sum = n1+ n2
# diff = n1-n2
# pro = n1*n2
# div = n1/n2

# print(f"{n1}+{n2}={sum}")
# print(f"{n1}+{n2}={diff}")u
# print(f"{n1}+{n2}={pro}")
# print(f"{n1}+{n2}={div}")
"""
Enter the first number 3+4j
Enter the second number 5+2j
(3+4j)+(5+2j)=(8+6j)
(3+4j)+(5+2j)=(-2+2j)
(3+4j)+(5+2j)=(7+26j)
(3+4j)+(5+2j)=(0.793103448275862+0.48275862068965514j)
"""
# Identify  error
else:
		print('else  suite')
print('Outside')
#error there is no if
# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
# no : in  after if condition

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
#
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
output:indentation error
# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
output:# unexpected indent
# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')
output:
expected am indent block after if

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
output:
Expected an indentation after else
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
if num % 2 != 0:
    print("Odd number")
Output
Enter a number: 8
Even
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
output:
One
Two 
Three
Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
output:
Hyd
Sec
Cyb
Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
output:
Bye
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
Program 
try:
    month = int(input("Enter month number (1 - 12): "))

    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
    else:
        print("Input should be between 1 and 12")

except ValueError:
    print("Input should be an integer")

'''
output:
Enter month number (1 - 12): 7
July
Enter month number (1 - 12): 13
Input should be between 1 and 12
Enter month number (1 - 12): 5.5
Input should be an integer
'''
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
digit = int(input("Enter a digit (0-9): "))

if digit == 0:
    print("Zero")
else:
    if digit == 1:
        print("One")
    else:
        if digit == 2:
            print("Two")
        else:
            if digit == 3:
                print("Three")
            else:
                if digit == 4:
                    print("Four")
                else:
                    if digit == 5:
                        print("Five")
                    else:
                        if digit == 6:
                            print("Six")
                        else:
                            if digit == 7:
                                print("Seven")
                            else:
                                if digit == 8:
                                    print("Eight")
                                else:
                                    if digit == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")

'''
Output 
Enter a digit(0-9):4
Four
Enter a digit(0-9):10
Invalid
'''