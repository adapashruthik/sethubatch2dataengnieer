'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  single  if  with  3  conditions  and  else
'''                                                                                                                                                                                                                              
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''                                                                                                                                                                                                
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))                                                                                                                                    
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3                                                                                                                                                                    
print("The largest number is:", largest)

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''                                                                                                                                                                                                    
def celsius_to_fahrenheit(celsius):
    return 1.8 * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''                                                                                                                                                                                                           
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))                                                                                                                                               
if x > 0 and y > 0:
    print("The point lies in the 1st quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the 2nd quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the 3rd quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the 4th quadrant.")
elif x != 0 and y == 0:
    print("The point lies on the x-axis.")
elif x == 0 and y != 0:
    print("The point lies on the y-axis.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
else:
    print("Invalid input.")

'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max =  20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program
'''                                                                                                                                                                                                            
a = 10
b = 20
c = 7                                                                                                                                                                                                           
max = a
min = a                                                                                                                                                                                                          
if b > max:
    max = b
if c > max:
    max = c                                                                                                                                                                                                     
if b < min:
    min = b
if c < min:
    min = c                                                                                                                                                                                                       
mid = (a + b + c) - (max + min)                                                                                                                                                                  
print("Max =", max)
print("Min =", min)
print("Mid =", mid)


'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''                                                                                                                                                                                                             
import math                                                                                                                                                                                                         
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))                                                                                                                                                                              
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The given sides form a triangle.")                                                                                                                                                            
if a == b == c:
        print("It is an Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print(f"Area of Equilateral Triangle = {area:.2f}")                                                                                                                                        
elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle.")
        perimeter = a + b + c
        print(f"Perimeter of Isosceles Triangle = {perimeter:.2f}")                                                                                                                           
else:
        print("It is a Scalene Triangle.")
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Perimeter of Scalene Triangle = {perimeter:.2f}")
        print(f"Area of Scalene Triangle = {area:.2f}")
else:
    print("The given sides do NOT form a triangle.")

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

Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')

case_: should not be in middle 
It should be in end of match

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _:
		print('Bye')
print('End')

End

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

Hyd
Bye

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

Book 
Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->

Hyd
Sec
Cyb

2) What  are  the  outputs  if  input  is  15  ?  --->

One 
Two 
Three 

3) What  are  the  outputs  if  input  is  10.8  ?  --->

India 
China
Usa

4) What  are  the  outputs  if  input  is  0  ?  --->

India 
China
Usa

5) What  are  the  outputs  if  input  is  -10  ?  --->

One
Two 
Three 

6) What  are  the  outputs  if  input  is  7  ?  --->

Hyd
Sec
Cyb

'''
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->

Quadrant 

2) What  is  the  output  when  input  is  (10 , 0) ?  --->

x-axis 

3) What  is  the  output  when  input  is  (0 , -20) ?  --->

y-axis 

4) What  is  the  output  when  input  is  (0 , 0) ?  --->

Origin

5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->

Error 
It should be two inputs

6) What  is  the  output  when  input  is  [10 , 20]  ?  --->

Error 
It should be tuple 

7) What  is  the  output  when  input  is  [0 , -25]  ?  --->

Error 

8) What  is  the  output  when  input  is  ()  ?  --->

Error 

9) What  is  the  output  when  input  is  {10 , 20} ?  --->

Error 

10) What  is  the  output  when  input  is  (25,) ?  --->

Error 

11) What  is  the  output  when  input  is  {10 : 20} ?  --->

Error 

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
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))  #  75
match  units // 100:
	case  0:
	 cost = units * 3.00                                                                                                                                                                                                                                      -     
      case 1:
        cost = 100 * 3.00 + (units - 100) * 3.50
       case 2 | 3:
        cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
       case 4 | 5 | 6:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (units - 400) * 4.50
    case _:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (units - 700) * 5.00

print(f"Bill amount for {units} units is Rs. {cost:.2f}")

'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  --->   0 , 1 ,  1 , 2 ,  3 ,5 , 8


1) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for   3rd  term ?  ---> 	2nd  term + 1st  term
    What  is  the  formual  for  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1  (No  formula)

3) Hint:  Use  while  loop
'''

x=10
a,b=0,1
while a<=x:
  print(a)
  a=b
  b=a+b
#  Find  outputs
while  True:
	print('Hello')
print('Bye')

Hello 
Bye

#  Find  outputs
while  False:
	print('Hello')
print('Bye')

Bye

# Find  outputs  (Home  work)
How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
print()

for num in [10 , 20 , 15 , 18]:
  print(num)

How  to  print  each  character  of   string  'Hyd'  with  for  loop
print()

for char in 'Hyd':
   print(char)

How  to  print  each  element  of   range(5)  with  for  loop

for i in range(5):
print(i)

# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)

10
30
50

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)

20
40
60

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)

(10,20)
(30,40)
(50,60)

print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)

10
30
50

# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')

10...20
30...40
50...60

for  x ,  y  in   a:
	print(x , y

Error 

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')

Error

# Identify  error  (Home  work)
for  x  in   123:
        print(x)


Value should be in sequence 
123 is error

# Find  outputs  (Home  work)
for  x   in   ():
        print(x)

empty tuple 

for  x   in  []:
        print(x)

empty list 

for  x   in   {}:
        print(x)

empty dictionary 

for  x   in   set():
        print(x)

empty set

for  x   in   '':
        print(x)

empty string 

for  x  in  range(10 , 10):
	print(x)

No values

for  x  in   range():
	print(x)

empty range 

for  x  in   (25):
	print(x)

Error 
, is missing

#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #
	print('Hello')
print('Bye')

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
Bye

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')a = [25, 10.8, 'Hyd', True]
print('Indexed based for loop')

for i in range(len(a)):
    print(f'Index {i} -> {a[i]}')

How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)              
print('For each loop')

for item in a:
    index = a.index(item)
    print(f'Index {index} -> {item}')

# How  to  print  each  element  and  the  corresponding  index
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed  based  for loop')
How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop
print('For each loop')
How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)                                                        
a = [25, 10.8, 'Hyd', True]                                                                                                                                                                  
print("Indexed for loop")
for i in range(len(a) - 1, -1, -1):
    print(a[i])
print("For-each loop")
a.reverse()        
for item in a:      
    print(item)
a.reverse()

'''
Write  a  program  to  add  two  lists  and  store  results  in  3rd  list

1st  list  --->  [10 , 20 , 15 , 18]

2nd  list  --->  [30 , 40 , 35 , 12 , 100 , 200 , 300]

3rd  list ?  ---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12]  =  [40 , 60 , 50 , 30]

Hint:  Use  append()  method
'''
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
c = []
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  indexed  based   for  loop
print('3rd  list : ' , c)                                                                                                                                                                                         
for i in range(len(a)):
    c.append(a[i] + b[i])

print('3rd list:', c)
How  to  add  lists  'a'  and  'b'  and  store  results  in  list  'c'  with  for  each  loop (Do  not  use  2nd  variable)                                              
i = 0
for x in a:
    c.append(x + b[i])
    i += 1

print('3rd list:', c)

#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  indexed  based  for  loop                                                                        
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
print('Indexed for loop')
for i in range(2, 5):
    print(a[i])

How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice          
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
print('For-each loop without second variable and slice')
count = 0
for item in a:
    if 2 <= count <= 4:
        print(item)
    count += 1

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)                                                                                                                                                                                                                       
a :   [11, 21, 16, 19]
b :   [10, 20, 15, 18]
