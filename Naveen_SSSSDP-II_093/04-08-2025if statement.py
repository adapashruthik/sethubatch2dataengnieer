#assignment1
'''
if ():
    print('One')
    print('Two')
    print('Three')
else:
if []:             # if cannot be indented with else, space bar needed before if
    print('Four')
    print('Five')
    print('Six')
else:               # else should be indented with if
if {}:
    print('Seven')
    print('Eight')
    print('Nine')
else:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')
'''
'''
#determine a number is even or odd with if statement
try:
    n=int(input('Enter any integer:'))
    if n%2==0:
        print('Even number')
    else:
        print('Odd number')
except:
    print('Input should be integer')
'''
'''
#assignment
if(10,20,30):
    print('Hyd')
    print('Sec')
    print('Cyb')
else:
    print('One')
    print('Two')
    print('Three')
print("bye")
print()
'''
'''
#assignment
if():
    print('Hyd')
    print('Sec')
    print('Cyb')
else:
    print('One')
    print('Two')
    print('Three')
print('Bye')
'''
'''
#assignment3
if{10:20,30:40}:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')
'''
#assignment4
'''
if { }:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')
'''
#print month name for input month number by using if and elif
'''
month_num = int(input("Enter month number (1 to 12): "))
if month_num == 1:
    print("Month: January")
elif month_num == 2:
    print("Month: February")
elif month_num == 3:
    print("Month: March")
elif month_num == 4:
    print("Month: April")
elif month_num == 5:
    print("Month: May")
elif month_num == 6:
    print("Month: June")
elif month_num == 7:
    print("Month: July")
elif month_num == 8:
    print("Month: August")
elif month_num == 9:
    print("Month: September")
elif month_num == 10:
    print("Month: October")
elif month_num == 11:
    print("Month: November")
elif month_num == 12:
    print("Month: December")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
'''
#print digit in words with else and if(do not use elif)
'''
try:
    digit = int(input("Enter a digit (0 to 9): "))
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
                                            print("Not a digit")
except:
        print('Input should be an integer')
'''
#test year is leap year or not
'''
try:
    year=int(input('Enter 4-digit year:'))
    if year %4 ==0 and year % 100!=0 or year % 400==0:
        print('Leap year')
    else:
        print('Not a leap year')
except:
    print('Input should be an integer')
'''
#determine largest of three numbers with if and else
'''
try:
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    c=eval(input('Enter 3rd input:'))
    if a>b>c:
        print('Largest number :',a)
    elif b>c:
        print('Largest number:',b)
    else:
        print('Largest number :',c)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be a complex number')
'''
#celsius temperature to farenheit and vice versa
'''
try:
    ch=int(input('Enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius'))
    if ch==1:
        c=float(input('Enter cesius temperature:'))
        print('Farenheit Equivalent :',1.8*c+32)
    elif ch==2:
        f=float(input('Enter farenheit temperature:'))
        print(F'celsius equivalent:{(f-32)/1.8:.2f}')
    else:
        print('Invalid input')
except:
    print('Input should be a number')
'''
#quadrant x-axis and y-axis or origin
'''
try:
    x=float(input('Enter value of x co-ordinate:'))
    y=float(input('Enter value of y co-ordinate:'))
    if x>0 and y>0:
        print('1st quadrant')
    elif x<0 and y>0:
        print('2nd quadrant')
    elif x<0 and y<0:
        print('3rd quadrant')
    elif x>0 and y<0:
        print('4th quadrant')
    elif x!=0 and y==0:
        print('X axis')
    elif x==0 and y!=0:
        print('Y axis')
    else:
        print('Origin')
except:
    print('Input should be a number')
'''
#determine largest,smallest and middle of three numbers
'''
try:
    a=float(input('Enter first input:'))
    b=float(input('Enter second input:'))
    c=float(input('Enter third input:'))
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    mid = (a+b+c)-(max+min)
    print('Largest input:',max)
    print('Smallest input:',min)
    print('Middle input:',mid)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be a complex number')
'''
#determine three sides form a triangle or not
'''
import math
try:
    a=float(input('Enter 1st side:'))
    b=float(input('Enter 2nd side:'))
    c=float(input('Enter 3rd side:'))
    if a+b>=c and b+c>=a and c+a>=b:
        if a==b==c:
            print('Equilateral triangle')
            area=math.sqrt(3)/4*a*a
            print(F'Area:{area:.2f}')
        elif a==b or b==c or a==c:
            print('Isoscles triangle')
            p=a+b+c
            print(F'Perimeter:{p}')
        else:
            print('Scalene triangle')
            s=(a+b+c)/2
            area=math.sqrt(s*(s-a)*(s-b)*(s-c))
            print(F'Area:{area:.2f}')
            print(F'Perimeter:{2*s}')
    else:print('Not a triangle')
except:
    print('Input should be a number')
'''
#determine roots quadratic equation
'''
import math
a=float(input('Enter value of a:'))
if a==0:
    print('Value of a can not be 0')
    exit()
b=float(input('Enter value of b:'))
c=float(input('Enter value of c:'))
disc=b**2-4*a*c
if disc>0:
    print('Roots are real and distinct')
    roots1=(-b+math.sqrt(disc)/(2*a))
    roots2=(-b-math.sqrt(disc)/(2*a))
    print(F'Root 1:{root1:.2f}')
    print(F'Root 2:{root2:.2f}')
elif disc<0:
    print('Roots are imaginary or complex')
    real=-b/(2*a)
    imag=math.sqrt(-disc)/(2*a)
    print(F'Root1:{real}+{imag}j')
    print(F'Root2:{real}-{imag}j')
else:
    print('Roots are real and equal')
    root=-b/(2*a)
    print(F'Root1:{root}')
    print(F'Root2:{root}')
'''
#centre of origin and radius is 'r'
'''
import math
x=float(input('Enter value of x:'))
y=float(input('Enter value of y:'))
r=float(input('Enter radius of circle:'))
d=math.sqrt(x**2+y**2)
if d>r:
    print('point is outside the circle')
elif d>r:
    print('Point is inside the circle')
else:
    print('Point is on the circle')
'''