#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)#25
print(type(y))#<class 'str'>
x = 10.8
y = F'{x}'
print(y)#10.8
print(type(y))#<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)#[10, 20, 30, 40]
print(type(y))#<class 'str'>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
print(F'{x =}  \t   {y =}   \t  {z =}')
"""
25         10.8           Hyd
a = 25            b  =  10.8      c  =  Hyd
a=25       b=10.8         c='Hyd'
25         10.8           Hyd
a  =  {a}         b  =  {b}       c  =   {c}
a  =  a           b  =  b         c  =  c
name 'x' is not defined
"""

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')#{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}
'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''

'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17
What  is  the  difference ?  --->  3
What  is  the  product ?  ---> 70
What  is  the  quotient ?  --->  1.42
What  is  the  remainder ?  --->  3
What  is  the  largest  number ?  ---> 10
What  is  the  smallest  number ?  --->  7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power?  --->  10000000
What  is  the  gcd  of  2  numbers ?  ---> 1
What  is  the  factorial   of  1st  input ?  ---> 10!
'''
import math
a = int(input("Enter 1st integer:"))
b=int(input("Enter 2nd integer:"))
sum = a + b
Difference = a - b
Product= a*b
Quotient= a/b
Remainder= a%b
max = max(a,b)
min = min(a,b)
Square_a = math.sqrt(a)
power = a ** b
gcd = math.gcd(a,b)
Fact = math.factorial(a)
print(f"{a} + {b} = {sum}")
print(f"{a} - {b} = {Difference}")
print(f"{a} * {b} = {Product}")
print(f"{a} / {b} = {Quotient}")
print(f"{a} % {b} = {Remainder}")
print(f"max({a} , {b}) = {max}")
print(f"min({a} , {b}) = {min}")
print(f"{a} ^ {b} = {power}")
print(f"sqrt({a}) = {Square_a}")
print(f"gcd({a} , {b}) = {gcd}")
print(f"fact({a}) = {Fact}")
"""
output:
Enter 1st integer:10
Enter 2nd integer:7
10 + 7 = 17
10 - 7 = 3
10 * 7 = 70
10 / 7 = 1.4285714285714286
10 % 7 = 3
max(10 , 7) = 10
min(10 , 7) = 7
10 ^ 7 = 10000000
sqrt(10) = 3.1622776601683795
gcd(10 , 7) = 1
fact(10) = 3628800

"""
'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''

x = input("Enter first input:")
y = input("Enter second input:")
x, y = y, x
print(f"After swap: x = {x}, y = {y}")
"""
Output:-
Enter first input: 25
Enter second input: Hyd
After swap: x = Hyd, y = 25
"""

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
c = eval(input("Enter 3rd input : "))
largest = a if a > b and a > c else (b if b > c else c)
print(f"Largest Input : {largest}")
"""
Output:-
Enter 1st input : 10
Enter 2nd input : 20
Enter 3rd input : 15
Largest Input : 20

Enter 1st input : 35.8
Enter 2nd input : 42.8
Enter 3rd input : 27.9
Largest Input : 42.8

Enter 1st input : 'RAMA'
Enter 2nd input : 'RAKESH'
Enter 3rd input : 'RAJESH'
Largest Input : RAMA

Enter 1st input : [10, 20, 15, 18]
Enter 2nd input : [10, 20, 32, 19]
Enter 3rd input : [10, 20, 25, 17]
Largest Input : [10, 20, 32, 19]

"""

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
result = '>' if a > b else ('<' if a < b else '=')
print(f"Result :   {result}")
'''Output:-
Enter 1st input : 10
Enter 2nd input : 20
Result :   <
Enter 1st input : 70
Enter 2nd input : 60
Result :   >
 
'''
# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0
'''
1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''
num = int(input("Enter a number: "))
print("Result:", 1 if num > 0 else (-1 if num < 0 else 0))
"""
output:
Enter a number: 2
Result: 1
Enter a number: 0
Result: 0
Enter a number: -34
Result: -1
"""
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''

# Program 
num = int(input("Enter any +ve integer: "))
print("Even number" if num % 2 == 0 else "Odd number")
"""
Output:-
Enter any +ve integer: 45
Odd number
"""
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

# Program 

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
'''
output:
Enter the length of the rectangle: 2
Enter the breadth of the rectangle: 4
Area of the rectangle: 8.0
Perimeter of the rectangle: 12.0
'''
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
radius = float(input("Enter the radius of the sphere: "))
volume = (4 / 3) * math.pi * (radius ** 3)
print("Volume of the sphere:", volume)
'''
output:
Enter the radius of the sphere: 5
Volume of the sphere: 523.5987755982989
'''
# (Home  work)
'''Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
r = float(input("Enter the rate of interest: "))
simple_interest = (p * t * r) / 100
compound_interest = p * ((1 + r / 100) ** t) - p
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)

'''Output 

Enter the principal amount: 1000
Enter the time in years: 2
Enter the rate of interest: 5
Simple Interest: 100.0
Compound Interest: 102.5
'''
'''(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x = 10
y=25
temp = x
x=y
y=temp
print("After swap:")
print("x=",x "y=",y)
'''
output:
After swap:
x=25 y=10

'''
#(Home  work)
#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

# Hint: One  addition  and  two  subtractions

#x = 25
#y =  10

x = 10
y = 25
x = x + y
y = x - y
x = x - y
print("After swapping:")
print("x =", x)
print("y =", y)
'''output:
After swapping:
x = 25
y = 10

(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
x = -200
y = 100
x = x * y
y = x // y
x = x // y
print("After swapping:")
print("x =", x)
print("y =", y)
"""
After swapping:
x = 100
y = -200
"""