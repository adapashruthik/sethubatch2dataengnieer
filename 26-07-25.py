#first program
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))

#second program
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
#print(F'{x =}  \t   {y =}   \t  {z =}')

#third program
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')


#fourth program
a=int(input('Enter 1st  integer number :  '))
b=int(input('Enter 2nd  integer number :  '))
print(F'{a} + {b} = {a + b}')
print(F'{a} - {b} = {a - b}')
print(F'{a} * {b} = {a * b}')
print(F'{a} / {b} = {a / b}')
print(F'{a} % {b} = {a % b}')
print(f'max({a} , {b}) = {max(a , b)}')
print(f'min({a} , {b}) = {min(a , b)}')
import math
print(f'{a}^{b} = {math.pow(a , b)}')
print(f'sqrt({a}) = {math.sqrt(a)}')
print(f'gcd({a} , {b}) = {math.gcd(a , b)}')
print(f'fact({a}) = {math.factorial(a)}')

#fifth program
x=eval(input('enter 1st input:'))
y=eval(input('enter 2nd input:'))
print(f'before swap:{x=} , {y=}')
x,y=y,x
print(f'after swap:{x=} , {y=}')

#sixth program
a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
c=eval(input('Enter 3rd input: '))
res=a if a>b and a>c else b if b>a and b>c else c
print("largest input is :",res)

#seventh program
a=float(input('Enter any number: '))
res="1" if a>0 else "-1" if a<0 else "0"
print("result is :",res)

#eighth program
a=eval(input('Enter any +ve integer: '))
res="even number" if a%2==0 else "odd number"
print("result is :",res)

#ninth program
l=eval(input('enter any length:'))
b=eval(input('enter any breadth:'))
perimeter=2*(l+b)
area=l*b
print("the perimeter is :",perimeter)
print("the area is :",area)

#tenth program
r=eval(input('Enter any radius: '))
import math
vol=4/3*math.pi*r**3
print("the volume is :",vol)

#eleventh program
p=eval(input('Enter any principal amount: '))
t=eval(input('Enter any time in years: '))
r=eval(input('Enter any rate of interest: '))
si=p*t*r/100
ci=p*(1+r/100)*(t-p)
print("the simple interest is :",si)
print("the compound interest is :",ci)

#twelfth program
x=10
y=25
print("before swap x and y are :",x,y)
temp=x
x=y
y=temp
print("after swap x and y are :",x,y)

#thirteenth program
x=10
y=25
print("before swap x and y are :",x,y)
x=x+y
y=x-y
x=x-y
print("after swap x and y are :",x,y)

#fourteenth program
x=200
y=100
print("before swap x and y are :",x,y)
x=x*y
x=x//y
y=x//y
print("after swap x and y are :",x,y)


