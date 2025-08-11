#1. Membership operators demo program (Home work)

list = [10 , 20 , 15 , 12 , 18] # Ref list points to list i.e.[10 , 20 , 15 , 12 , 18]
print(15 in list) #True
print(19 in list) #False
print(14 not in list) #True
print(15 not in list)#False
s = 'Hyd is green city' # Ref 's' points to String object i.e.'Hyd is green city'
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True
print('' not in s) #False



#2. Find outputs (Home work)

a = 'Hyd' #Ref 'a' points to String object 'Hyd'
b = 'Hyd' #Ref 'b' points to  same String object 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) #True
print() # Empty
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False 
print(x  is  not  y) #True
print(x == y) #True
print() #Empty
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)
print(m  is  n) # True
print(m  is  not  n) #False
print(m == n) #True
print(x == m) # False



#3. Find outputs (Home work)

a = 25 # Ref 'a' points to int object 25
b = 25.0 # Ref 'a' points to float object 25.0
print(a  is  b) # False
print(a  is  not  b) # True
print(a == b) # True



#4. Identity operators demo program

a = 25 # Ref 'a' points to int object 25
b = 25 # Ref 'a' points to same int object 25
print(a  is  b) #True
print(a  is  not  b) # False
print(a == b) # True



#5. Find outputs (Home work)

a = 20 # Ref 'a' points to int object 20
a %= 3 + 2 * 4 # a=a%3+2*4
print(a) # 9



#6. Find outputs (Home work)

a = 3 # Ref 'a' points to int object 3
a *= 4 #a=a*4
print(a) # 81



#7. Multiple  Assignment (Home work)

x , y , z = 25 , 10.8 , 'Hyd' # referencew 'x' , 'y' and 'z' points to int , float , string objects respectively 
print(x) # 25
print(y) # 10.8
print(z) # 'Hyd'



#8. Find outputs (Home work)

a , b , c = 3 , 4 , 5 # References 'a','b' and 'c' points to int objects
a *= b + c # a =a*b+c
print(a) # 27



#9.  Assignment  operators  demo  program  (Home  work)

a = 25 #ref 'a' points to int object 25
print(a) # prints value of object 'a' i.e. 25
b =  a # ref 'b' points to same object 'a'
print(b) # 25
print(a  is  b) #True
x = 4 # Ref 'x' points to int object 4
y = 5 # Ref 'y' points to int object 5
z = x + y * 6 # z=4+5*6
print(z) # 34
25 = a # error due to, it should be only a reference on left side 
a + b = x + y # error due to, it should be only a reference on left side



#10. Find outputs (Home work)

a = b = c = 25 # References 'a','b' and 'c' are points to same int object 25
print(id(a)) # Address of int object 'a' 
print(id(b))# Address of int object 'b' , same as 'a' 
print(id(c))# Address of int object 'c' ,same as 'a' and 'b' 
print(a , b , c) # 25 25 25



#11.  Find  outputs

print({10 , 20}  |  {30 , 20}) # {10, 20, 20} , because of set doesn't have duplicate elements 2nd 20 will not be concatenated
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'Hyd' , 20 : 'Vja', 30 : 'Cyb' }
print(range(4) | range(5)) #Error due to range objects can't be concatenated and added
print([10 , 20]  |  [30 , 20]) # Error due to list can be concatenated using '+' operator



#12. Find outputs (Home work)

x = [1 , 2 , 3 , 4] # Ref 'x' points to list  [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3] # Ref 'y' points to list  [1 , 2 , 4 , 3]
print(x == y)  # False
a = (4 , 1 , 3 , 2) # Ref 'a' points to tuple  (4 ,1 ,3 ,2)
b = (4 , 2 , 3 , 1)  # Ref 'b' points to tuple  (4 ,2 ,3 ,1)
print(a == b) # False
p = {1 , 2 , 3 , 4}  # Ref 'p' points to dict {1, 2 ,3, 4}
q = {4 , 1 , 3 , 2}  # Ref 'p' points to dict  {4 ,1 ,3 ,2}
print(p == q)# True
m = range(5) # Ref 'm' points to range object
n = range(5)# Ref 'n' points to range object
print(m == n) #True



#13. Find outputs (Home work)

a = [10,20,30] # Ref 'a' points to list [10, 20, 30]
b = (10,20,30) # Ref 'b' points to tuple(10, 20 ,20)
print(a  is  b) # False
print(a  ==  b) #False
