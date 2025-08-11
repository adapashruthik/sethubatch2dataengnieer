x=25
y=F'{x}' # coverts int object 25 to string object '25' and assigns to y
print(y) # 25
print(type(y))  # <class 'str'>
x=10.8
y=F'{x}' # converts float object 10.8 to string object '10.8'
print(y) # 10.8
print(type(y)) # <class 'str'>
x=[10,20,30,40]
y=F'{x}' # converts list object [10,20,30,40] to string object '[10,20,30,40]'
print(y) # [10,20,30,40]
print(type(y)) # <class 'str'>
print()

a,b,c=25,10.8,'Hyd'
print(F'{a} \t {b} \t {c}') # 25   10.8   Hyd
print(F'a={a} \t b={b} \t c={c}') # a=25   b=10.8   c=Hyd
print(F'{a=} \t {b=} \t {c=}') # a=25   b=10.8  c=Hyd
print(F'{a:} \t {b:} \t {c:}') # 25  10.8  Hyd : prints value and ignores colon(:)
print('a={a} \t b={b} \t c={c}') # a={a}  b={b}   c={c}
print(F'a=a \t b=b \t c=c') # a=a b=b c=c 
#print(F'{x=} \t {y=} \t{z=}')# x,y,z are not defined

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25 : value of object is printed when x is in odd number of braces
print(F'{{x}}')   #  {x} : object name is printed when x is in even number of braces
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')  #  {{x}}
print(F'{{{{{x}}}}}')  #  {{25}}
print(F'{{{{{{x}}}}}}')  #  {{{x}}}
print(F'{{{{{{{x}}}}}}}')  #  {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')   #  {{{{x}}}}

#program to determine sum,diff,product,quotient,largest, and smallest of two numbers and also remainder, sqrt of 1st input,power, gcd and factorial
import math
x=eval(input('Enter 1st integer number: ')) # reads 1st integer from keyboard and assigns to x
y=eval(input('Enter 2nd integer number: ')) # reads 2nd integer from keyboard and assigns to y
print(F'{x} + {y} =',x+y) # 17
print(F'{x} - {y} =',x-y) # 3
print(F'{x} * {y} =',x*y) # 70
print(F'{x} / {y} =',x/y) # 1.4285714285714286
print(F'{x} % {y} =',x%y) # 3
print(F'max({x},{y}) =',max(x,y)) # 10
print(F'min({x},{y}) =',min(x,y)) # 7 
print(F'{x} ^ {y} =',math.pow(x,y)) # 10000000.0
print(F'sqrt({x}) =',math.sqrt(x)) # 3.1622776601683795
print(F'gcd({x},{y}) =',math.gcd(x,y)) # 1
print(F'fact({x}) =',math.factorial(x)) # 3628800

#program to swap values of any two objects in a single statement without using 3rd values
x=eval(input('Enter 1st input: ')) # reads 1st input from keyboard and assigns to x
y=eval(input('Enter 2nd input: ')) # reads 2nd input from keyboard and assigns to y
print('Before swap: x =', x, 'y =',y)  #  x=25 y=Hyd
x,y=y,x # swaps the references of x and y
print('After swap: x =', x, 'y =',y)   #   x=Hyd  y=25

print()
#program to determine largest of three inputs without using max() function
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
z=eval(input('Enter 3rd input: '))
print('Largest input',x if x>y>z else y if x<y>z else z)

print()
#program to print '>' if 1st input > 2nd input, '<' if 1st input < 2nd input and '=' if both are same
try:
    x=eval(input('Enter 1st input: '))
    y=eval(input('Enter 2nd input: '))
    print('Result: ', '>' if x>y else '<' if x<y else '=')
except:
    print('Input cannot bool or complex ')    

print()
#program to print 1  if  input is +ve, -1 if input is -ve and 0 if input is 0
x=eval(input('Enter any input: '))
print('Result: ', 1 if x>0 else -1 if x<0 else 0)



print()
#program to test if input is even number or odd number
x=eval(input('Enter any +ve input: '))
print('Result: ' , 'even number' if x%2==0 else 'odd number')

print()
#program to determine area and perimeter of rectangle
try:
    import math
    x=eval(input('Enter length of rectangle: '))
    y=eval(input('Enter breadth of rectangle: '))
    area=x*y
    perimeter=2*(x+y)
    print('Area of the rectangle: ',area)
    print('Perimeter of the rectangle: ',perimeter)
except:
    print('input cannot be string')

print()
#program to determine volume of a sphere
import math
r=eval(input('Enter radius: ')) # 4
volume=4/3*math.pi*(r**3)
print('Volume of sphere: ',volume)# 29.321531433504735

print()
# program to determine simple interest and compound interest
p=eval(input('Enter principal: '))
t=eval(input('Enter time in years: '))
r=eval(input('Enter rate of interest: '))
simple_interest=(p*t*r)/100
compound_interest=p*(1+r/100)**t-p
print('Simple interest : ',simple_interest)
print('compound interest : ',compound_interest)

print()
#program to swap values of two objects using 3rd object
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
print('Before swap: x =', x, 'y =',y)
z=x+y
x=z-x
y=z-y
print('After swap: x =', x, 'y =',y)
print()
#program to swap values of two objects without using 3rd object
x=eval(input('Enter 1st input: '))
y=eval(input('Enter 2nd input: '))
print('Before swap: x =', x, 'y =',y)
x=x+y
y=x-y
x=x-y
print('After swap: x =', x, 'y =',y)
print()
#program to swap values of two objects without using 3rd object
x=eval(input('Enter 1st input: ')) # -200
y=eval(input('Enter 2nd input: '))  #  100
print('Before swap: x =', x, 'y =',y)  #  x = -200 y = 100
x=x*y
y=x/y
x=x/y
print('After swap: x =', x, 'y =',y)   #  x = 100.0 y = -200










