# Write  a  program  to  test  year  is  leap  year  or  not                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
try:
    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
        print(year," is a leap year.")
    else:
        print(year," is not a leap year.")
except:
    print("Invalid year")    

'''output:                                                                                                                                                                              
2024
2024  is a leap year.                                                                                                                                                                
1700
1700  is not a leap year.   
23.5                                                                                                                                                                     
Invalid year'''

# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else                                                                
a = int(input("Enter First number:2"))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a > c:
    print(a,"is largest number")
elif b>c:
    print(b,"is largest number")
else:
    print(c,"is largest number")

'''output
Enter First number:20
Enter second number: 30
Enter third number: 15
30 is largest number
'''       
# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
m = int(input("Enter a case: "))
temperature = int(input("Enter temperature: "))
match m:
    case 1:
        fahrenheit = 1.8*temperature+32
        print(fahrenheit)
    case 2:
        celsius = (temperature-32)/1.8
        print(celsius)
    case _:
        print("Enter a valid temperature")      
        
'''Output:
Enter a case: 1
Enter temperature: 30
86.0                                                                                                                                                                                           Enter a case: 2
Enter temperature: 55
12.777777777777777'''

# Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant , 4th  quadrant , x - axis , y - axis   or  origin
x = int(input("Enter x value: "))
y = int(input("Enter the y value: "))
if x > 0 and y > 0:
    print(f'{x} {y} are first Quadrant')
elif x < 0 and y > 0:
    print(f'{x} {y} are second Quadrant')
elif x < 0 and y < 0:
    print(f'{x} {y} are third Quadrant')
elif x > 0 and y < 0:
    print(f'{x} {y} are fourth Quadrant')
elif x != 0 and y == 0:
    print("X-Axis")
elif x == 0 and y != 0:
    print("Y-Axis")
else:
    print("Origin")

'''Output:                                                                                                                                                                                  
Enter x value: 2
Enter the y value: 3
2 3 are first Quadrant                                                                                                                                                      
Enter x value: -5
Enter the y value: 2
-5 2 are second Quadrant                                                                                                                                                       
 Enter x value: -3
Enter the y value: -4
-3 -4 are third Quadrant                                                                                                                                                         
Enter x value: 2
Enter the y value: -5
2 -5 are fourth Quadrant                                                                                                                                                          
Enter x value: 5
Enter the y value: 0
X-Axis                                                                                                                                                                                     
Enter x value: 0
Enter the y value: 5
Y-Axis                                                                                                                                                                                                               
Enter x value: 0
Enter the y value: 0
Origin'''

# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
a = int(input("Enter First input: ")) 
b = int(input("Enter second input: ")) 
c = int(input("Enter third input: "))  
max = a
if b>max :
    max = b
    if c>max:
        max = c
print(max)
min = a
if b<min :
    min = b
    if c<min:
        min = c
print(min)
mid = (a+b+c)-(max+min)
print(mid)                                                                                                                                                                               

'''Output:
Enter First input: 10
Enter second input: 20
Enter third input: 30
30
10
20 '''

# Write  a  program  to  determine  three  sides  form  a  triangle  or  not
import math
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and b + c > a and c + a > b:
    print("The sides form a valid triangle")
    if a == b and b == c:
        print("Equilateral triangle")
        area = (math.sqrt(3) / 4) * a * a
        print("Area =", area)
    if (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
        print("Isosceles triangle")
        perimeter = a + b + c
        print("Perimeter =", perimeter)
    if a != b and b != c and c != a:
        print("Scalene triangle")
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print("Area =", area)
        print("Perimeter =", perimeter)
if not (a + b > c and b + c > a and c + a > b):
    print("The sides do NOT form a valid triangle")

'''Output:Enter side 1: 2
Enter side 2: 2
Enter side 3: 2
The sides form a valid triangle
Equilateral triangle
Area = 1.7320508075688772'''

# Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

import math
a = float(input("Enter a (a ≠ 0): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == 0:
    print("Invalid input: a must not be zero.")
else:
    disc = b ** 2 - 4 * a * c
    print("Discriminant =", disc)
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
        print("Roots are real and distinct.")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif disc == 0:
        root = -b / (2 * a)
        print("Roots are real and same.")
        print("Root =", root)
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-disc) / (2 * a)
        print("Roots are complex (imaginary).")
        print("Root 1 = {:.2f} + {:.2f}j".format(real_part, imag_part))
        print("Root 2 = {:.2f} - {:.2f}j".format(real_part, imag_part))    

'''output:                                                                                         
Enter a (a ≠ 0): 2
Enter b: 3
Enter c: 4
Discriminant = -23.0
Roots are complex (imaginary).
Root 1 = -0.75 + 1.20j
Root 2 = -0.75 - 1.20j'''

# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle. Center  is  origin  and  radius  is  'r'

import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
distance = math.sqrt(x*x+y*y)
print(distance)
r  = float(input("Enter radius: "))
if distance > r:
    print("outside the circle")
elif distance < r:
    print("Inside the circle")
else:
    print("on the circle")                                                                                                                                                           
'''output:                                                                                                                                                                                   
Enter x: 4
Enter y: 3
5.0
Enter radius: 6
Inside the circle'''

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')      

'''Output:                                                                                                                                                                                                 
Bye'''

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: #error because underscore or nameless cannot be in middle it should be at end
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')               

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _: # error because wildcard makes remaining patterns unreachable
		print('Hello')
	case  _:
		print('Bye')
print('End')     

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')     

'''Output:   
Hyd                                                                                                                                                                                           
Bye'''

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
print('Bye')    

'''Output:                                                                                                                                                                        
Book                                                                                                                                                                                 
Bye'''


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
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd Sec Cyb Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One
Two
Three
Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India
China
Usa
Bye

4) What  are  the  outputs  if  input  is  0  ?  --->Hyd
Sec
Cyb
Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One
Two
Three
Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd
Sec
Cyb
Bye
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

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y - axis
8) What  is  the  output  when  input  is  ()  ?  ---> Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not  a  point
'''

'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
'''
units = int(input('Enter units: '))  # Example: 75

match units // 100:
    case 0:
        cost = units * 3.00
        print(cost)
    case 1:
        cost = 100 * 3.00 + (units - 100) * 3.50
        print(cost)
    case 2:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
        print(cost)
    case 3 | 4 | 5 | 6:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
        print(cost)
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00
        print(cost)

'''output:
Enter units: 88
264.0
Enter units: 175
562.0
Enter units: 400
1450.0
Enter units: 666
2647.5
Enter units: 800
3800.0'''

# Write a program to print fibonacci series up to x
a = 0
b = 1 
x = int(input("Enter the value of x: "))
print(a)
print(b)
c = a+b
while(c<=x):
    print(c)
    a=b
    b=c
    c=a+b                                                                                                                                                                                      
'''Output:                                                                                                                                                                          
Enter the value of x: 10
0
1
1
2
3
5
8'''

#  Find  outputs
while  True: 
	print('Hello') # hello prints infinity times
print('Bye')

#  Find  outputs
while  False:
	print('Hello') 
print('Bye') #print Bye

# Find  outputs  (Home  work)
# How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop print()                                                                                                 
a = [10,20,15,18]
for x in a:
    print(x)       # prints whole list line by line                                                                                                                                                                                      How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()                                                                                                      
a = 'Hyd'
for x in a:
    print(x) # prints each character line by line of a string
# How  to  print  each  element  of   range(5)  with  for  loop                   
for x in range(5):
      print(x) # prints 0 1 2 3 4 line by line

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) # prints 10 30 50 line by line
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x) # prints 20 40 60 line by line
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) # prints tuple  (10, 20) (30, 40) (50, 60) line by line
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) # 10 30 50 line by line
      
# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')#10...20  next line 30...40 next line 50...60

for  x ,  y  in   a:
	print(x , y)#cannot unpacked uniterable int
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')#cannot unpack uniterable int object

# Identify  error  (Home  work)
for  x  in   123:
        print(x)#int is not iterable because non sequence

# Find  outputs  (Home  work)
for  x   in   ():
        print(x)#nothing printed
for  x   in  []:
        print(x)#nothing printed
for  x   in   {}:
        print(x)#nothing printed
for  x   in   set():
        print(x)#nothing printed
for  x   in   '':
        print(x)#nothing printed
for  x  in  range(10 , 10):
	print(x)#nothing printed
for  x  in   range():
	print(x)#error
for  x  in   (25):
	print(x)#not iterable
      
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')   

'''output:
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye'''

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
for x in a:
    print(x) #Indexed  based  for loop

'''output:
Indexed  based  for loop
25
10.8
Hyd
True'''

#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for  i  in  range(1 , len(a) + 1):  
	print(a[-i])  #  Prints  a[-i]  where  'i'  varies  from  1  to  len


# Write  a  program  to  add  two  lists  and  store  results  in  3rd  list
a = eval(input('Enter  1st  list  :  '))  #  Reads  1st  list
b = eval(input('Enter  2nd  list  :  '))  #  Reads  2nd  list
c = []  #  3rd  list  is  initially  empty
small = min(len(a) , len(b))  #  Smallest  list  length
for  i  in   range(small):   #  How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
	c . append(a[i] + b[i]) #
print('3rd  list : ' , c)

'''output:
Enter  1st  list  :  [10,20,30]
Enter  2nd  list  :  [20,30,40]
3rd  list :  [30, 50, 70]'''

# How to print list elements from indexes 2 to 4 without slice
a=[25,10.8,'Hyd',True,3+4j,None,'Sec']
print('Indexed for loop')
for i in range(2, 5):
      print(a[i])

'''output:
Indexed for loop
Hyd
True
(3+4j)
'''

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)#a :   [11, 21, 16, 19]

b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)#b :   [10, 20, 15, 18]