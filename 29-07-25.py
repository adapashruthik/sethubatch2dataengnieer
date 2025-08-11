
year=int(input("enter the year:"))
if  year % 100!=0 or year % 400==0 and year % 4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")

#second program
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print("largest number=",a)
else:
     if b>c:
        print("largest number=",b)
     else:
        print("largest number=",c)

#third program
m=int(input("enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius "))
match m:
    case 1:
        d=float(input("enter celsius temperature"))
        f=1.8*d+32
        print("farenheit eqvalent",f)
    case 2:
        d=float(input("enter farenheit temperature"))
        c=(d-32)/1.8
        print("celsius eqvalent:",c)
    case _:
        print("invalid input")

#fourth program
x=int(input("enter the value of x:"))
a,b=0,1
print("fibonacci series up to",x,":")
while a<=x:
    print(a, end=' ')
    a,b=b,a+b

#fifth program
list1=eval(input("enter 1st list"))
list2=eval(input("enter 2nd list"))
result=[]
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
    print("list 1 :",list1)
    print("list 2 :",list2)
    print("sum list:",result)