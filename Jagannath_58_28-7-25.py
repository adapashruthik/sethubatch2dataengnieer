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
'''a=eval(input("Enter  first number:"))
b=eval(input("Enter second number:"))
sum=a+b
difference=a-b
product=a*b
division=a/b
print("Sum:",sum)
print("Difference:",difference)
print("Product:",product)
print("Division:",division)

# Identify  error
else:
		print('else  suite')
print('Outside')

There is no if statement so it is error 
Without if statement else statement could not run

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

: is missing in if statement

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

: is missing in else statement

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

Indentation error

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

Indentation error 
if and else should be in same line

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

{
}  should not be there

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


Indentation error

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a=int(input("Enter a number"))
if a%2==0:
      print("Even number")
else:
      print("Odd number")

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

Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)         
month_number = int(input("Enter month number (1-12): "))
try:                                                                                                                                                                                                                           
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    print("Please enter a number between 1 and 12")                                                                                                             
except:                                                                                                                                                                                 
   print("input should be an integer")

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid                                                                                                                                                                                                                                                                                                                                                                                                                digit = int(input("Enter a digit (0-9): "))

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
