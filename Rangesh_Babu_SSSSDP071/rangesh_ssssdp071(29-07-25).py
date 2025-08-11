1)Write a program to test year is leap year or not
 1) What is leap year ?---> Divisible by 4 but not by 100 (or) divisble by 400
 2) Are 2016 , 2020 , 2024 leap years?---> Yes becoz leap year for every 4 yearrs
 3) Are 1700 , 1800 , 1900 leap years?---> No becoz no leap year for every 100 years
 4) Are 1600 , 2000 , 2400 leap years?---> Yes becoz leap year for every 400 years
 5) Hint: single if with 3 conditions and else
 Code:
 try:
 year=int(input('Enter Year : '))
 if (year%4==0 and year%100==0) or (year%400==0):
 print('Leap Year')
 else:
 print('Not Leap Year')
 except:
 print('Input should be integer')
 2) Write a program to determine largest of three numbers with if and else
 Hint: Write multiple conditions
 Code:
 first=int(input("Enter the first number: "))
 second=int(input("Enter the second number: "))
 third=int(input("Enter the third number: "))
 if first > second and first > third:
 print(f"{first} is the largest number")
 elif second >third:
 print(f"{second} is the largest number")
 else:
 print(f"{third} is the largest number")
 3) Write a program to convert celsius temperature to farenheit and vice-versa
1) What is the formula to convert celsius to farenheit ?---> 1.8 * temp + 32
 2) What is the formula to convert farenheit to celsius ?---> (temp- 32) / 1.8
 Code:
 num=int(input('Enter 1 to convert celsius to farenheit or Enter 2 to
 convert farenheit to celsius'))
 if num==1:
 temp=float(input('Enter temperature in celsius: '))
 farhenheit=1.8*temp+32
 print('Temperature in farenheit is:', farhenheit)
 elif num==2:
 temp=float(input('Enter temperature in farenheit: '))
 celsius=(temp-32)/1.8
 print(f'Temperature in celsius is:{celsius:.2f}')
 else:
 print('Invalid input')
 4) Write a program to test a point (x , y) lies in 1st quadrant , 2nd quadrant , 3rd
 quadrant ,4th quadrant , x- axis , y- axis or origin
 1) What are the values of x and y in 1st quadrant?---> Both are +ve
 2) What are the values of x and y in 2nd quadrant?---> 'x' is-ve and 'y' is +ve
 3) What are the values of x and y in 3rd quadrant?--->Both are-ve
 4) What are the values of x and y in 4th quadrant?---> 'x' is +ve and 'y' is-ve
 5) What are the values of x and y on x-axis?--->'x' is non-zero and 'y' is 0
 6) What are the values of x and y on y-axis?---> 'x' is 0 and 'y' is non-zero
 7) What are the values of x and y if point is origin ?---> Both are zeroes
 8) Hint: Use if .. elif
 Code:
 x=float(input('Enter X coordinate:'))
 y=float(input('Enter Y coordinate:'))
 if x>0 and y>0:
 print(f"point ({x},{y}) is in the first quadrant")
 elif x<0 and y>0:
 print(f"point ({x},{y}) is in the second quadrant")
 elif x<0 and y<0:
 print(f"point ({x},{y}) is in the third quadrant")
elif x>0 and y<0:
 print(f"point ({x},{y}) is in the fourth quadrant")
 elif x==0 and y==0:
 print(f"point ({x},{y}) is at the origin")
 elif x==0 and y!=0:
 print(f"point ({x},{y}) is on the Y axis")
 elif x!=0 and y==0:
 print(f"point ({x},{y}) is on the X axis")
 else:
 print("Invalid input")
 5)Write a program to determine largest , smallest and middle of three numbers
 a =10
 b =20
 c =7
 max= 20
 min = 7
 mid = (10+20+7)-(20+7)=10
 Code:
 a=float(input('Enter 1st number:'))
 b=float(input('Enter 2nd number:'))
 c=float(input('Enter 3rd number:'))
 max=a
 if b>max and b>c:
 max=b
 print('largest Number ',max)
 elif c>max and c>b:
 max=c
 print('largest Number',max)
 min=a
 if b<min and b<c:
 min=b
 print('Smallest Number ',min)
 elif c<min and c<b:
 min=c
print('Smallest Number ',min)
 middle=(a+b+c)-(min+max)
 print('Middle number ',middle)
 6)Write a program to determine three sides form a triangle or not
 1) Find area if it is an equilateral triangle
 What is an equilateral triangle ?---> All the three sides should be same
 What is the area of equilateral triangle ?---> sqrt(3) / 4 * a ^ 2
 2) Find perimeter if it is an isosceles triangle
 What is an isoscles triangle ?---> Any two sides are same
 What is the perimeter of isoscles triangle ?---> a + b + c
 3) Find both if it is scalene triangle
 What is a scalene triangle ?---> All the three sides are different
 What is the area of scalene triangle ?---> sqrt(s * (s- a) * (s- b) * (s- c))
 What is the value of 's' ?--->
 (a + b+c) /2
 What is the perimeter of scalene triangle ?---> a + b + c
 4) What is the qualification of triangle ?---> Sum of every two sides should be > 3rd
 side
 5) Hint: Use nested if
 Code:
 import math
 side1=float(input('Enter 1st side:'))
 side2=float(input('Enter 2nd side:'))
 side3=float(input('Enter 3rd side:'))
 if side1+side2>=side3 or side1+side3>=side2 or side2+side3>=side1:
 if side1==side2==side3:
 area=(math.sqrt(3)/4)*side1**2
 print(f'area {area:.2f}')
 elif side1==side2 or side2==side3 or side1==side3:
 perimeter=side1+side2+side3
 print('perimeter ',perimeter)
 elif side1!=side2!=side3:
 s=(side1+side2+side3)/2
area=math.sqrt(s * (s- side1) * (s- side2) * (s- side3))
 print(f'area {area:.2f}')
 perimeter=side1+side2+side3
 print('perimeter ',perimeter)
 7)Write a program to determine roots of a quadtratic equation a * x ^ 2 + b *x + c= 0
 where a !=0
 1) What is the value of discriminant ?---> b ^ 2- 4ac
 2) What are the roots called if disc > 0 ?---> Real and distinct
 What is the formula for root1 ?---> (-b + sqrt(disc)) / 2a
 What is the formula for root2 ?---> (-b- sqrt(disc)) / 2a
 3) What are the roots called if disc is 0 ?---> Real and same
 What is the formula for root ?--->-b / 2a
 4) What are the roots called if disc < 0 ?---> Complex (or) Imaginary roots
 What is the formula for real part ?--->-b / 2a
 What is the formula for imag part ?---> sqrt(-disc) / 2a
 What is root1 if real part is 3 and imag part is 4?---> 3+4j
 What is root2 if real part is 3 and imag part is 4?---> 3-4j
 Code:
 import math
 a=float(input("Enter coefficient a: "))
 b=float(input("Enter coefficient b: "))
 c=float(input("Enter coefficient c: "))
 discriminant = b**2- 4*a*c
 if a == 0:
 print("Coefficient 'a' cannot be zero for a quadratic equation.")
 else:
 if discriminant > 0:
 root1 = (-b + math.sqrt(discriminant)) / (2 * a)
 root2 = (-b- math.sqrt(discriminant)) / (2 * a)
 print(f"The roots are real and different: {root1} and {root2}")
 elif discriminant == 0:
 root =-b / (2 * a)
 print(f"The roots are real and the same: {root}")
 elif discriminant < 0:
 realPart =-b / (2 * a)
 imaginaryPart = math.sqrt(-discriminant) / (2 * a)
print(f"The roots are complex and different: {realPart} + {imaginaryPart}i and {realPart}
{imaginaryPart}i")
 else:
 print("the equation is in the form ax^2 + bx + c = 0.")
 8)Write a program to determine a point(x , y) lies inside , outside or on the circle.
 Center is origin and radius is 'r'
 1) What is the distance between origin and point (x , y) ?---> sqrt(x ^ 2 + y ^ 2)
 2) Where is the point if distance > raidus ?---> Outside the circle
 3) Where is the point if distance < raidus ?---> Inside the circle
 4) Where is the point if distance and raidus are same ?---> On the circle
 Code:
 import math
 x=float(input('Enter X-Coordinate:'))
 y=float(input('Enter Y-Coordinate:'))
 r=float(input('Enter Radius:'))
 distance = math.sqrt(x**2 + y**2)
 if distance >r:
 print('Point is outside the circle')
 elif distance < r:
 print('Point is inside the circle')
 else:
 print('Point is on the circle')
 # Find outputs (Home work)
 m=4
 match m:
 case 1:
 print('One')
 case 2:
 print('Two')
 case 3:
 print('Three')
 print('Bye') # Bye
 # Identify Error
 i = 2
match i:
 case 1:
 print('One')
 case _:
 print('None of the above')
 case 2:
 print('Two')
 print('Bye')
 Error: Wild character case is written in the middle.
 # Find outputs (Home work)
 m=2
 match m:
 case 1:
 print('One')
 case _:
 case _:
 print('End')
 print('Hello')
 print('Bye')
 Error: Two Wild card characters are presented.
 # Find outputs (Home work)
 m=1
 match m:
 case 1:
 print('Hyd')
 case 1:
 print('Sec')
 case 1:
 print('Cyb')
 print('Bye') # Hyd <nextLine> Bye
 # Find outputs (Home work)
 ch = 'B'
 match ch:
 case 'A':
 print('Apple')
case 'B':
 print('Book')
 case 'C':
 print('Cafe')
 case _:
 print('None of the above')
 print('Bye') #Book<nextLine>Bye
 '''
 1) What are the outputs if input is-6 ?--->Hyd<nextLine>Sec<nextLine>Cyb<nextLine>Bye
 2) What are the outputs if input is 15 ?--->one <nextLine>Two<nextLine>
 Three<nextLine>Bye
 3) What are the outputs if input is 10.8 ?--->India<nextLine>China<nextLine>
 Usa<nextLine>Bye
 4) What are the outputs if input is 0 ?---> Hyd<nextLine>Sec<nextLine>Cyb<nextLine>Bye
 5) What are the outputs if input is-10 ?---> one<nextLine>Two<nextLine>
 Three<nextLine>Bye
 6) What are the outputs if input is 7 ?---> Hyd<nextLine>Sec<nextLine>Cyb<nextLine>Bye
 '''
 x =eval(input('Enter any number : '))
 match x:
 case 7 |-6 | 0:
 print('Hyd')
 print('Sec')
 print('Cyb')
 case-10 | 15:
 print('One')
 print('Two')
 print('Three')
 case _:
 print('India')
 print('China')
 print('Usa')
 # End of match
 print('Bye')
 '''
 1) What is the output when input is (-10 ,-20) ?--->Quadrant
2) What is the output when input is (10,0) ?--->X-axis
 3) What is the output when input is (0,-20)?--->y-axis
 4) What is the output when input is (0, 0)?--->origin
 5) What is the output when input is (10,20, 30)?--->Not apoint
 6) What is the output when input is [10, 20] ?--->not apoint
 7) What is the output when input is [0,-25] ?--->not a point
 8) What is the output when input is () ?--->Error
 9) What is the output when input is {10,20} ?--->Not apoint
 10) What is the output when input is (25,) ?--->x-axis
 11) What is the output when input is {10: 20}?--->Not a point
 '''
 tpl = eval(input('Enter any point in the form of (x , y) : '))
 match tpl:
 case (0 , 0):
 print('Origin')
 case (0 , y):
 print('y- axis')
 case (x , 0):
 print('x- axis')
 case (x , y):
 print('Quadrant')
 case _:
 print('Not a point')
 9)Write a program to determine bill amount and input is units
 Units
 Cost------------------------------------------------------------
 First 100 units(0- 99)
 Rs. 3.00 / unit
 Next 100 units(100- 199) Rs. 3.50 / unit
 Next 200 units(200- 399) Rs. 4.00 / unit
 Next 300 units(400- 699) Rs. 4.50 / unit
 Above 700 units(>= 700)
 Rs. 5.00 / unit--------------------------------------------------------------
Let units be 1200
 What is the bill amount?---> 100 * 3.00 + 100* 3.50 +200 *4.00 + 300* 4.50 +500*5.00
 Hint: Use match ... case but not if ... else
Code:
 units = int(input('Enter units : ')) # 75
 match units // 100:
 case 0:
 cost = units * 3.00
 case 1:
 cost = 100*3.00+(units-100) * 3.50
 case 2|3:
 cost = 100*3.00+100*3.50+(units-200) * 4.00
 case 4|5|6:
 cost = 100*3.00+100*3.50+200 * 4.00+(units-300) * 4.50
 case _:
 cost = 100*3.00+100*3.50+200 * 4.00+300 * 4.50+(units-700)* 5.00
 print(f'The cost of {units} units is Rs. {cost:.2f}')
 10)Write a program to print fibonacci series upto x
 Let input be 10
 What are the outputs ?---> 0, 1, 1,2, 3,5,8
 1) What is the formula for 10th term?---> 9th term +8th term
 What is the formula for 3rd term?--->
 2nd term+1st term
 What is the formual for ith term ?---> (i-1)th term + (i- 2) term
 2) What are the first two terms ?---> 0 and 1 (No formula)
 3) Hint: Use while loop
 Code:
 x =int(input("Enter the limit: "))
 a, b = 0, 1
 while a <= x:
 print(a)
 a, b = b, a +b
 # Find outputs
 while True:
 print('Hello')
 print('Bye') #Infinite Loop
 # Find outputs
 while False:
 print('Hello')
print('Bye') #Bye
 # Find outputs (Home work)
 How to print each element of list [10 , 20 , 15 , 18] with for loop
 print()
 for i in list:
 print(i)
 How to print each character of string 'Hyd' with for loop
 print()
 str='Hyd'
 str=list(str)
 for i in str:
 print(i)
 How to print each element of range(5) with for loop
 for i in range(5):
 print(i)
 # Find outputs (Home work)
 for x in {10 : 20, 30: 40,50: 60} . keys():
 print(x)
 print()#10 30 50
 for x in {10 : 20, 30: 40,50: 60} . values():
 print(x)
 print() # 20 40 60
 for x in {10 : 20, 30: 40,50: 60} . items():
 print(x)
 print() # (10:20) (30:40) (50:60)
 for x in {10 : 20, 30: 40,50: 60}:
 print(x) # 10 30 50
 a ={10 : 20 , 30:40, 50:60}
 for x , y in a.items():
 print(x , y , sep = '...') #10…20…<nextline>30…40<nextline>50…60
 for x , y in a:
 print(x , y) #error
 for x , y in {10: 20 ,30:40, 50:60}:
print(x , y , sep = '...')#error
 # Identify error (Home work)
 for x in 123:
 print(x) #error:integer is immutable
 # Find outputs (Home work)
 for x in ():
 print(x) #empty tuple
 for x in []:
 print(x) # empty list
 for x in {}:
 print(x) #empty dict
 for x in set():
 print(x) #empty set
 for x in '':
 print(x) #empty string
 for x in range(10 , 10):
 print(x) #empty
 for x in range():
 print(x) # error
 for x in (25):
 print(x)#error
 # Nested Loop demo program
 for i in range(1 , 4):
 for j in range(1 , 5):
 print(i , j) #
 print('Hello')
 print('Bye')
 output:
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
 # How to print each element and the corresponding index
 a =[25, 10.8 , 'Hyd' , True]
 print('Indexed based for loop')
 How to print each element and the corresponding index with index based for loop
 for i in range(len(a)):
 Print(i,a[i])
 print('For each loop')
 How to print each element and the corresponding index with for ... each loop(Do not
 use 2nd variable)
 for x in reversed(a):
 print(x)
 # How to print list elements in reverse order without slice
 a =[25, 10.8 , 'Hyd' , True]
 print('Indexed for loop')
 How to print each element of list in reverse order with indexed based for loop
 for i in range(len(a)-1,-1,-1):
 print(a[i])
 How to print each element of list in reverse order with for each loop (Do not use 2nd
 variable and slice)
 for x in reversed(a):
 print(x)
 11)Write a program to add two lists and store results in 3rd list
 1st list---> [10 , 20 , 15 , 18]
 2nd list---> [30 , 40 , 35 , 12 , 100 , 200 , 300]
3rd list ?---> [10 + 30 , 20 + 40 , 15 + 35 , 18 + 12] = [40, 60,50, 30]
 Hint: Use append() method
 Code:
 a =[10, 20, 15, 18]
 b =[30, 40, 35, 12, 100, 200, 300]
 c =[]
 for i in range(len(a)):
 c.append(a[i] + b[i])
 print(c)
 # How to print list elements from indexes 2 to 4 without slice
 a =[25, 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
 print('Indexed for loop')
 How to print elements from indexes 2 to 4 of list 'a' with indexed based for loop
 for i in range(2,5):
 print(a[i])
 How to print elements from indexes 2 to 4 of list 'a' with for each loop without using
 2nd variable and slice
 index = 0
 for x in a:
 if 2 <= index <= 4:
 print(x)
 index += 1
 # Tricky program
 # Find outputs (Home work)
 a =[10, 20 , 15, 18]
 for i in range(len(a)):
 a[i] += 1
 print('a : ' , a)#a:11 21 16 19
 b =[10 , 20, 15,18]
 for x in b:
 x += 1
 print('b : ' , b)#10 20 15 18