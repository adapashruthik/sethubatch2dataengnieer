#1.  Find  outputs  (Home  work)

x = 25
y = F'{x}'
print(y) # 25
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10, 20, 30, 40]
print(type(y)) # <class 'str'>



#2. Find  outputs  (Home  work)

a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25<tab>10.8<tab>Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25<tab>b  =  10.8 <tab>c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25<tab>b=10.8<tab>c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') # 25<tab>10.8<tab>Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}<tab>b  =  {b}<tab>c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a<tab>b  =  b<tab>c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # Error due to x, y and z are not defined



#3.  Find  outputs  (Home  work)

x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') # {{25}}
print(F'{{{{{{x}}}}}}') # {{{x}}}
print(F'{{{{{{{x}}}}}}}') # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}') # {{{{x}}}}



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''


# 4.Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  inputHint:  Use  F  string  to  print  results

import math
a = eval(input("Enter 1st integer number :"))
b = eval(input("Enter 1st integer number :"))
print (f'{a}' " + " f'{b}' ' = ' f'{a+b}')
print (f'{a}' +" - "+ f'{b}' +' = ' +f'{a-b}')
print (f'{a}' +" * "+ f'{b}' +' = ' +f'{a*b}')
print (f'{a}' +" / "+ f'{b}' +' = ' +f'{a/b}')
print (f'{a}' +" % "+ f'{b}' +' = ' +f'{a%b}')
print ("max"+"("+(f'{a}' +" , "+ f'{b}')+")" +' = ' +f'{max(a,b)}')
print ("min"+"("+(f'{a}' +" , "+ f'{b}')+")" +' = ' +f'{min(a,b)}')
print (f'{a}' +" ^ "+ f'{b}' +' = ' +f'{a**b}')
print ("sqrt"+"("+(f'{a}')+")" +' = ' +f'{math.sqrt(a)}')
print ("gcd"+"("+(f'{a}' +" , " + f'{b}')+")" +' = ' +f'{math.gcd(a,b)}')
print ("fact"+"("+(f'{a}')+")" +' = ' +f'{math.factorial(a)}')



#5. Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object 
#Let  'x'  be  25  and  'y'  be   'Hyd'
#What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

#Hint:  Swap  references  but  not  objects

x = input("Enter 1st input :")
y = input("Enter 2st input :")
print("Before swap : " + "x="f'{x}'+ "     " + "y="f'{y}')
x, y = y, x
print("After swap : " + "x="f'{x}'+ "     " + "y="f'{y}')



#6. Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

x = eval(input("Enter 1st input :"))
y = eval(input("Enter 2st input :"))
z = eval(input("Enter 3rd input :"))
larg = x if x > y and x > z else y if y > z and y > x else z
print("Largest input : " ,larg)



#7. '''Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
 #                                              '<'  if  1st  input  <  2nd  input  and
  #                                             '='  if  inputs  are  same'''

x = eval(input("Enter 1st input :"))
y = eval(input("Enter 2st input :"))
sym = '<' if x < y else '>'
print("Result :" ,sym)


#8. Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

x = eval(input("Enter any +ve integer:"))
sym = 'Odd number' if x%2!=0 else 'Even number'
print(sym)


#9. Write  a  program  to  test  input  is  even  number  or  odd  number

x = eval(input("Enter 1st input :"))
sym = '1' if 0 < x else '-1' if 0 > x else "0"
print("Result :" ,sym)


#10. Write  a  program  to  determine  area  and  perimeter  of  rectangle

x = eval(input("Enter length :"))
y = eval(input("Enter breadth :"))
area = x * y
perimeter = 2*(x+y)
print("Area of rectangle :" ,area)
print("Perimeter of rectangle :" ,perimeter)


#11. Write  a  program  to  determine  volume  of  a  sphere

import math
r = eval(input("Enter radius :"))
volume = (4/3)(math.pi)(r**3)
print("Volume of sphere :" ,volume)


#12. Write  a  program  to  determine  simple  interest  and  compound  interest

p = eval(input("Enter principle amout :"))
t = eval(input("Enter time :"))
r = eval(input("Enter interest rate :"))
si = (p*t*r)/100
ci = p* (1 + r/100) ** t - p
print("Simple Interest :" ,si)
print("Compound Interest :" ,ci)


#13. Write  a  program  to  swap  values  of  two  objects  using  3rd   object

x = input("Enter 1st input :")
y = input("Enter 2st input :")
print("Before swap : " + "x="f'{x}'+ "     " + "y="f'{y}')
temp = x
x = y
y = temp
print("After swap : " + "x="f'{x}'+ "     " + "y="f'{y}')


#14. Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

x = eval(input("Enter 1st input :"))
y = eval(input("Enter 2st input :"))
print("Before swap : " + "x="f'{x}'+ "     " + "y="f'{y}')
x = x + y
y = x -y
x = x -y
print("After swap : " + "x="f'{x}'+ "     " + "y="f'{y}')


#15. Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

x = eval(input("Enter 1st input :"))
y = eval(input("Enter 2st input :"))
print("Before swap : " + "x="f'{x}'+ "     " + "y="f'{y}')
x = x * y
y = x // y
x = x // y
print("After swap : " + "x="f'{x}'+ "     " + "y="f'{y}')



