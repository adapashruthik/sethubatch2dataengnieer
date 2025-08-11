#===========================================Operators===========================
print({10,20} | {30 , 20})# {10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#{10:'Hyd',20:'Vja',30:'Sec'}
#print(range(4) | range(5))#Error
#print([10,20] | [30,20])#Error 

a = 25
print(a)#25
b =  a#Assigning reference 'a' to 'b'
print(b)#25
print(a  is  b)#True 
x = 4
y = 5
z = x + y * 6#4+5*6=34
print(z)#34
#25=a#Error 
#a+b=x+y#Error 

a = b = c = 25
print(id(a))#Address of object 'a'
print(id(b))#Same Address
print(id(c))#Same Address 
print(a,b,c)# 25 25 25

x,y,z = 25,10.8,'Hyd'
print(x)#25
print(y)#10.8
print(z)#Hyd 

a,b,c = 3,4,5
a*= b+c# a = a*(b+c) -> 3*(4+5) -> 27
print(a)#27 

a = 20
a %= 3+2*4# a=a%(3+2*4) -> 20%11 -> 9
print(a)#10 

a = 25
b = 25
print(a  is  b)#True 
print(a  is  not  b)#False 
print(a==b)#True 

a = 25
b = 25.0
print(a  is  b)#False
print(a  is  not  b)#True 
print(a==b)#True 

a = 'Hyd'
b = 'Hyd'
print(a  is  b)#True 
print(a  is  not  b)#False 
print(a==b)#True 
print()
x = [1,2,3,4]
y = [1,2,3,4]
print(x is y)#False 
print(x  is  not  y)#True 
print(x==y)#True 
print()
m = (1,2,3,4) 
n = (1,2,3,4)
print(m  is  n)#True 
print(m  is  not  n)#False 
print(m==n)#True 
print(x==m)#False 
print()

list = [10,20,15,12,18]
print(15 in list)#True 
print(19 in list)#False 
print(14 not in list)#True
print(15 not in list)#False 
print()
s = 'Hyd is green city'
print( 'is' in s)#T 
print('was' in s)#F 
print('g' in s)#T 
print('z' in s)#F
print(' ' in s)#T 
print('gre' in s)#T 
print('yd i' in s)#T  
print('' in s)#T 
print(''not in s)#F 
print()

x = [1,2,3,4]
y = [1,2,4,3]
print(x == y)#False 
a = (4,1,3,2)
b = (4,2,3,1)
print(a == b)#False  
p = {1,2,3,4}
q = {4,1,3,2}
print(p == q)#True 
m = range(5)
n = range(5)
print(m == n)#True
print() 

a = [10,20,30]
b = (10,20,30)
print(a is b) #False 
print(a == b) #False  

