'''
1)Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 
try:
    m = int(input("Enter the month number(1-12) : "))
    if m==1:
        print("January")
    elif m==2:
        print("Feburary")
    elif m==3:
        print("March")
    elif m==4:
        print("April")
    elif m==5:
        print("May")
    elif m==6:
        print("June")
    elif m==7:
        print("July")
    elif m==8:
        print("August")
    elif m==9:
        print("September")
    elif m==10:
        print("Octomber")
    elif m==11:
        print("November")
    elif m==12:
        print("December")
    else:
        print("Input should be in between 1 and 12")
except:
    print("Input should be integer")
    


2)Write  a  program  to  test  year  is  leap  year  or  not

y = int(input("Enter any year : "))
if y%4==0 and y%100!=0 or y%400==0:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")



3)Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa


n = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : "))

match n:
    case 1:
        t = int(input("Enter  Celsius  temperature : "))
        print("Fahrenheit  Equivalent  : ",1.8*t+32)
    case 2:
        t = int(input("Enter  Fahrenheit temperature : "))
        print("Celsius  Equivalent  : ",(t-32)/1.8)
    case _:
        print("Invalid Input")


4)Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin


x = int(input("Enter the value of x co-ordinate : "))
y = int(input("Enter the value of y co-ordinate : "))

if x>0 and y>0:
    print(f"({x},{y}) lies on First Quadrant")
elif x<0 and y>0:
    print(f"({x},{y}) lies on Second Quadrant")
elif x<0 and y<0:
    print(f"({x},{y}) lies on Third Quadrant")
elif x>0 and y<0:
    print(f"({x},{y}) lies on Fourth Quadrant")
elif x>0 and y==0:
    print(f"({x},{y}) lies on X-axis")
elif x==0 and y>0:
    print(f"({x},{y}) lies on Y-axis")  
else:
    print(f"({x},{y}) lies on Origin")
    

5)Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : ")) 

print("Max is ", max(a,b,c))
print("Min is ", min(a,b,c))
print("Middle is ",)


6)Write  a  program  to  print  fibonacci  series  upto   x

n = int(input("Enter a number : "))
a,b = 0,1
while n>0:
       print(a)
       print(b)
       print(


for  x  in  {10:20,30:40,50:60}.keys():
	print(x)
print()

for  x  in  {10:20,30:40,50:60}.values():
	print(x)
    
print()
for  x  in  {10:20,30:40,50:60}.items():
	print(x)
    
print()
for  x  in  {10:20,30:40,50:60}:
	print(x)


a = [25,10.8,'Hyd',True,3 + 4j,None,'Sec']
for i in range(2,5):
    print(a[i],sep = '\t')


a = eval(input("Enter the list : ")) 
b = eval(input("Enter the list : ")) 
c = []
min_len = min(len(a),len(b))
for i in range(min_len):
    c.append(a[i]+b[i])
print("List 3 is : ",c)



# Input from user
n = int(input("Enter number of lines: "))

# Loop through each line
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)
    
 '''

n = int(input("How many lines? : "))

for i in range(1, n + 1):
    for j in range(1, 2 * n):  # Total width = 2n - 1 positions
        if j >= n - (i - 1) and j <= n + (i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print() 






