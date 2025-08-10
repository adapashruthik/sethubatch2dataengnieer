'''#program to test year is leap year or not
x=int(input('Enter a year: '))
if ((x%4==0 and x%100 !=0) or x%400==0):
    print(F'{x} is a leap year')
else:
    print(F'{x} is not a leap year')

print()
#program to determine largest of three numbers with if and else
x=int(input('Enter 1st number: '))
y=int(input('Enter 2nd number: '))
z=int(input('Enter 3rd number: '))
if(x>y and y>z):
    print('x is largest')
if(y>z and y>x):
        print('y is largest')    
else:
        print('z is largest')

print()
#program to convert celsius to farenheit and vice versa
x=int(input('enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius '))
if (x==1):
    y=float(input('enter fahrenheit temperature :'))
    celsius=(y-32)/1.8
    print('celsius equivalent :',celsius)
elif(x==2):
    z=float(input('enter celsius temperature: '))
    fahreheit=1.8*z+32
    print('fahrenheit eqivalent :',fahreheit)
else:
    print('Invalid input')

#program to test a point (x,y) lies in 1st, 2nd, 3rd, 4th quadrant, or origin
x=float(input('enter x-axis: '))
y=float(input('Enter y-axis: '))
if (x>0 and y>0):
    print(F'({x},{y}) lies in 1st quadrant')
elif (x<0 and y>0):
    print(F'({x},{y}) lies in 2nd quadrant')
elif (x<0 and y<0):
    print(F'({x},{y}) lies in 3rd quadrant')
elif (x>0 and y<0):
    print(F'({x},{y}) lies in 4th quadrant')
else:
    print(F'({x},{y}) lies at origin')
    
print()

#program to determine largest, smallest and middle of three numbers
x=float(input('enter 1st input: '))
y=float(input('enter 2nd input: '))
z=float(input('enter 3rd input: '))
max=x
min=y
if(y>max):
    max=y
if(z>max):
    max=z
if(x<min):
    min=x
if(z<min):
    min=z
print('largest number: ',max)
print('smallest number: ',min)
mid=(x+y+z)-(max+min)
print('middle number ',mid)

#program to determine three sides form a triangle or not
import math
a=float(input('enter 1st side of triangle: '))
b=float(input('enter 2nd side of triangle: '))
c=float(input('enter 3rd side of triangle: '))
if((a+b)>c or(b+c)>a or (c+a)>b):
    if (a==b==c):
        print('area of equilateral triangle: ',math.sqrt(3)/4*a**2)
    if(((a==b) and b!=c) or (b==c and c!=a) or (c==a and a!=b)):
        print('perimeter of isoscles triangle: ',a+b+c)
    if((a!=b and b!=c and c!=a)):
        s=(a+b+c)/2
        print('area of scalene trinagle: ',math.sqrt(s*(s-a)*(s-b)*(s-c)))
        print('perimeter of the scalene triangle: ',(a+b+c))
#program to determine roots of quadratic equation
import math
a=float(input('Enter the value of a(X^2 coefficient) in aX^2+bX+c(a!=0): '))
b=float(input('Enter the value of b(X coefficient) in aX^2+bX+c(a!=0): '))
c=float(input('Enter the value of c(constant) in aX^2+bX+c(a!=0): '))
discriminant=(b**2)-4*a*c
if(discriminant>0):
    print('Roots are Real and Distinct')
    print('Root1 :',(-b+math.sqrt(discriminant))/(2*a))
    print('Root1 :',(-b-math.sqrt(discriminant))/(2*a))
if(discriminant==0):
    print('Roots are Real and same')
    print('Root is :',-(b/(2*a)))
if(discriminant<0):
    print('Roots are complex or imaginary')
    real_root=-b/(2*a)
    imag_root=(math.sqrt(-discriminant/(2*a)))
    print(F'Root1 is : {real_root}+{imag_root}j')
    print(F'Root1 is : {real_root}-{imag_root}j')


#program to determine a point(x,y) lies inside, outside or on the circle
import math
x=float(input('enter x-axis: '))
y=float(input('Enter y-axis: '))
r=float(input('Enter radius :'))
distance=math.sqrt(x**2+y**2)
if(distance>r):
        print(F'({x},{y}) lie outside the circle)')
if(distance<r):
        print(F'({x},{y}) lie inside the circle)')
if(distance==r):
        print(F'({x},{y}) lie on the circle)')


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  #  Bye: there is no m=4 in match

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')  #  Anonymous value should be written at end. The remaining cases won't be executed

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End') # error : there is no case 2
'''
#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')   #  Hyd <next line> Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') #  Book <next line> Bye


'''
1) What  are  the  outputs  if  input  is  -6 ? --->  
   Hyd
   Sec
   Cyb
   Bye
2) What  are  the  outputs  if  input  is  15  ?  --->
   One
   Two
   Three
   Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->
   India
   China
   Usa
   Bye
4) What  are  the  outputs  if  input  is  0  ?  --->
   Hyd
   Sec
   Cyb
   Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->
   One
   Two
   Three
   Bye
6) What  are  the  outputs  if  input  is  7  ?  --->
   Hyd
   Sec
   Cyb
   Bye

x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')
'''

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->
   Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->
   x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->
    y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->
    origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->
    Not a point : three elements are given
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->
    Not a point :Should insert in tuple not list
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->
    Not a point :should insert in tuple not list
8) What  is  the  output  when  input  is  ()  ?  --->
    Not a point: empty tuple
9) What  is  the  output  when  input  is  {10 , 20} ?  --->
    Not a point: should insert in tuple not set
10) What  is  the  output  when  input  is  (25,) ?  --->
    Not a point: only single element is inserted
11) What  is  the  output  when  input  is  {10 : 20} ?  --->
    Not a point : should insert in tuple not dictionary
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')















