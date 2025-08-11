#  Find  outputs  (Home  work) 
x = 25 
y = F'{x}' 
print(y) #25 
print(type(y)) #<class str> 
x = 10.8 
y = F'{x}' 
print(y) #10.8 
print(type(y)) #<class str> 
x = [10,20,30,40] 
y = F'{x}' 
print(y) #[10,20,30,40] 
print(type(y)) #<class str> 
#Find  outputs  (Home  work) 
a ,  b , c = 25 , 10.8 , 'Hyd' 
print(F'{a}  \t   {b}   \t  {c}') # 25 10.8 Hyd 
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a=25  b=10.8   c=Hyd 
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25  b=10.8   c=Hyd 
print(F'{a:}  \t   {b:}   \t  {c:}') # 25  10.8  Hyd 
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}    b  =  {b}    c  =   {c} 
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a    b  =  b    c  =  c 
print(F'{x =}  \t   {y =}   \t  {z =}') #Error:x,y,z are not defined. 
#  Find  outputs  (Home  work) 
x = 25 
print(F'{x}')  #  25 
print(F'{{x}}')   #  {x} 
print(F'{{{x}}}')  #   {25} 
print(F'{{{{x}}}}') # {{x}} 
print(F'{{{{{x}}}}}') #{{25}} 
print(F'{{{{{{x}}}}}}') #{{{x}}} 
print(F'{{{{{{{x}}}}}}}') #{{{25}}} 
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}} 
 
1)Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  
of  two  numbers.Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  
input 
Hint:  Use  F  string  to  print  results 
Code: 
import math 
try:    
    a=eval(input("Enter 1st number: ")) 
    b=eval(input("Enter 2nd number: ")) 
 
    sum= a + b 
    diff = a - b 
    prod = a * b 
    quot = a / b 
    rem = a % b 
    largest = max(a, b) 
    smallest = min(a, b) 
    sqrt_a = math.sqrt(a) 
    power = a ** b 
    gcd = math.gcd(a,b) 
    fact_a = math.factorial(a) 
 
    print(f'{a} + {b} = {sum}') 
    print(f'{a} - {b} = {diff}') 
    print(f'{a} * {b} = {prod}') 
    print(f'{a} / {b} = {quot}') 
    print(f'{a} % {b} = {rem}') 
    print(f'max({a}, {b}) = {largest}') 
    print(f'min({a}, {b}) = {smallest}') 
    print(f'sqrt({a}) = {sqrt_a}') 
    print(f'{a} ** {b} = {power}') 
    print(f'gcd({a}, {b}) = {gcd}') 
    print(f'fact({a}) = {fact_a}') 
except : 
    print("Input should be a integer or float") 
 
 
2)Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  
using  3rd  object 
Let  'x'  be  25  and  'y'  be   'Hyd' 
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25 
Hint:  Swap  references  but  not  objects 
Code: 
try: 
    a=eval(input("Enter 1st input: ")) 
    b=eval(input("Enter 2nd input: ")) 
 
    print(f'Before swap: {a=}, {b=}') 
    a,b=b,a 
    print(f'After swap: {a=}, {b=}') 
except: 
    print("for string inputs, use single quotes") 
 
3) Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function 
Enter 1st input : 10 
Enter 2nd input : 20 
Enter 3rd input : 15.8 
Largest  Input  :  20 
Code: 
try: 
    a=eval(input("Enter 1st input: ")) 
    b=eval(input("Enter 2nd input: ")) 
    c=eval(input("Enter 3rd input: ")) 
 
    max=a if a>b else b if b>c else c 
 
    print(f'Largest Input: {max}') 
     
except: 
    print("for string inputs, use single quotes") 
 
 
 
 
 
4) Write  a  program  to  print   '>'  if  1st  input  >  2nd  input, 
                                               '<'  if  1st  input  <  2nd  input  and 
                                               '='  if  inputs  are  same 
Code: 
try: 
    a=eval(input("Enter 1st input: ")) 
    b=eval(input("Enter 2nd input: ")) 
 
    max='>' if a>b else '<' if a<b else '=' 
 
    print(f'Result: {max}') 
     
except: 
    print("for strings, use quotes.") 
 
 
5)Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0 
 
1) What  is  the  result  if  input  is  -25 ?  --->  -1 
 
2) What  is  the  result  if  input  is  75 ?  --->  1 
 
3) What  is  the  result  if  input  is  0 ?  --->  0 
 
4) Use  nested  ternary  operator 
Code: 
try: 
    a=eval(input("Enter any number: ")) 
 
    result = 1 if a > 0 else -1 if a < 0 else 0 
    print(f'Result: {result}') 
     
except: 
    print("Input should be a number") 
 
 
 
 
6)Write  a  program  to  test  input  is  even  number  or  odd  number 
 
1) What  is  an  even  number  ?  --->  Divisible  by  2 
 
2) What  is  an  odd  number  ?  --->  Not  divisible  by  2 
 
3) Use  ternary  operator 
Code: 
try: 
    a=eval(input("Enter any number: ")) 
 
    result = 'Even Number' if a % 2 ==0 else 'Odd Number' 
    print(f'{result}') 
     
except: 
    print("Input should be a positive number") 
 
7)Write  a  program  to  determine  area  and  perimeter  of  rectangle 
 
1) What  are  the  inputs ?  ---> length  and   breadth 
 
2) What  are  the  outputs  ?  --->  area  and  perimeter 
 
3) What  is  the  area  of  rectangle  ?  --->  length * breadth 
 
4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth) 
Code: 
try: 
    a=eval(input("Enter Length: ")) 
    b=eval(input("Enter Breadth: ")) 
 
    area=a*b 
    per=2*(a+b) 
 
     
    print(f'Area of Rectangle with Length {a} and Breadth {b} is: {area:.2f} square units') 
    print(f'Perimeter of Rectangle with Length {a} and Breadth {b} is: {per:.2f} units') 
     
except: 
    print("Input should be a positive number") 
 
 
8) Write  a  program  to  determine  volume  of  a  sphere 
 
1) What  is  the  input ?  --->  radius 
 
2) What  is  the  output ?  --->  volume 
 
3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3 
Code: 
import math 
try: 
    a=eval(input("Enter Radius: ")) 
    pi=math.pi 
    Vol=(4/3) * pi * a**3 
    print(f'Volume of Sphere with Radius {a} is: {Vol:.2f} cubic units') 
     
except: 
    print("Input should be a positive number") 
 
9)Write  a  program  to  determine  simple  interest  and  compound  interest 
 
1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest 
 
2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest 
 
3) What  is  simple  interest  formula ?  ---> ptr / 100 
 
4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p 
Code: 
import math 
try: 
    a=eval(input("Enter Principle: ")) 
    b=eval(input("Enter Time-period: ")) 
    c=eval(input("Enter Rate of Interest: ")) 
 
    SI=(a * b * c) / 100 
    CI = a * (math.pow((1 + c / 100), b)) - a 
 
    print(f'Simple Interest: {SI:.2f}') 
    print(f'Compound Interest: {CI:.2f}') 
     
except: 
    print("Input should be a positive number") 
 
10) Write  a  program  to  swap  values  of  two  objects  using  3rd   object 
Let  x = 10  and  y = 25 
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10 
Code: 
try: 
    a=eval(input("Enter 1st input: ")) 
    b=eval(input("Enter 2nd input: ")) 
 
    print(f'Before swap: {a=}, {b=}') 
    temp=a 
    a=b 
    b=temp 
    print(f'After swap: {a=}, {b=}') 
except: 
    print("for string inputs, use single quotes") 
 
11)Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object 
Hint: One  addition  and  two  subtractions 
x = 25 
y =  10 
code: 
try: 
    a=eval(input("Enter 1st input: ")) 
    b=eval(input("Enter 2nd input: ")) 
 
    print(f'Before swap: {a=}, {b=}') 
    a= a + b 
    b= a - b 
    a= a - b 
    print(f'After swap: {a=}, {b=}') 
except: 
    print("Input should be number") 
 
 
 
12)Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object 
Hint: One  multiplication  and  two  divisions 
x =  -200 
y =  100 
Code: 
try: 
    a=eval(input("Enter 1st input: ")) 
    b=eval(input("Enter 2nd input: ")) 
 
    print(f'Before swap: {a=}, {b=}') 
    a= a * b 
    b= a / b 
    a= a / b 
    print(f'After swap: a={a:.0f}, b={b:.0f}') 
except: 
    print("Input should be number") 