#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)

25

print(type(y))

<class 'str'>

x = 10.8
y = F'{x}'
print(y)

10.8

print(type(y))

<class 'str'>

x = [10,20,30,40]
y = F'{x}'
print(y)

[10,20,30,40]

print(type(y))

<class 'str'>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')

25      10.8      Hyd 

print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')

a=25          b=10.8         c=Hyd 
 
print(F'{a=}  \t   {b=}   \t  {c=}')

a=25          b=10.8         c='Hyd'

print(F'{a:}  \t   {b:}   \t  {c:}')

25      10.8      Hyd

print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')

Error 

print(F'a  =  a  \t  b  =  b  \t  c  =  c')

a=a        b=b      c=c

print(F'{x =}  \t   {y =}   \t  {z =}')

Error

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')

{{x}}

print(F'{{{{{x}}}}}')

{{25}}

print(F'{{{{{{x}}}}}}')

{{{x}}}

print(F'{{{{{{{x}}}}}}}')

{{{25}}}

print(F'{{{{{{{{x}}}}}}}}')

{{{{x}}}}

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
a=10
b=7
sum=a+b
difference=a-b
product=a*b
quotient=round(a/b,2)
remainder=a%b
largest=max(a,b)
smallest=min(a,b)
sqrt_first=round(math.sqrt(a),2)
power=a**b
gcd=math.gcd(a,b)
factorial_first=math.factorial(a)
print (f"{sum}")
print (f"{difference}")
print (f"{product}")
print (f"{quotient}")
print (f"{remainder}")
print (f"{largest}")
print (f"{smallest}")
print (f"{sqrt_first}")
print (f"{power}")
print (f"{gcd}")
print (f"{factorial_first}")

'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x,y=25, Hyd 
x,y=y,x
print ("x=",x)
print ("y=",y)

'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

def largest(a,b,c):
return a if a>b and a>c else (b if b>c else c)
print (largest(10,20,15))
print(largest(35.8,42.8,27.9))
print(largest('RAMA','RAKESH','RAJESH'))
 print(largest([10 , 20 , 15 , 18]  , [10 , 20 , 32, 19],[10 , 20 , 25, 17]))

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   --->  42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  ---> [10 , 20 , 32 , 19]

5) Inputs  can  be  integers , floats , strings  and  so  on

6) Use  nested  ternary  operator
'''

'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same


a=input("Enter first value:")
b=input("Enter second value:")
print('>' if a>b else '<' if a<b else '=')



1) What  is  the  result  if  inputs  are  10  and  20 ?  ---> <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''

'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

num=int(input("Enter a number"))
result=1 if num>0 else (-1 if num<0 else 0)
print(result)


1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  --->  0

4) Use  nested  ternary  operator
'''

'''
Write  a  program  to  test  input  is  even  number  or  odd  number

num=int(input("Enter a number"))
result="Even number" if num%2==0 else "odd number"
print(result)


1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle


length=float(input("Enter the length of the rectangle"))
breadth=float(input("Enter the breadth of the rectangle"))
area=length*breadth 
perimeter=2*(length+breadth)
print("Area is:",area)
print("Perimeter is:", Perimeter)


1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere


import math
radius=float(input("Enter the radius of the sphere"))
volume=(4/3)*math.pi*(radius**3)
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")


1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest
    
def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    return compound_interest
    
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))
print(f"\nSimple Interest = {si:.2f}")
print(f"Compound Interest = {ci:.2f}")
1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object
x = 10
y = 25
print("Before swapping:")
print("x =", x)
print("y =", y)
temp = x
x = y
y = temp
print("\nAfter swapping:")
print("x =", x)
print("y =", y)
Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = 25
y = 10
x = x + y      
y = x - y      
x = x - y 
print("After swapping:")
print("x =", x)
print("y =", y)
Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = -200
y = 100
x = x * y       
y = x // y       
x = x // y       
print("After swapping:")
print("x =", x)
print("y =", y)

Hint: One  multiplication  and  two  divisions

x =  -200
y =  100
'''
