#  Find  outputs 
print({10 , 20}  |  {30 , 20}) #{10,20,30} 
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})  #{10:Hyd,20:vja,30:cyb} 
print(range(4) | range(5))  #error:range can’t be combined 
print([10 , 20]  |  [30 , 20]) #error:list can be combined with + operator 
#  Assignment  operators  demo  program  (Home  work) 
a = 25 
print(a)  #25 
b =  a  #assign  value of object a to the reference b  
print(b)  #25 
print(a  is  b) #True:both the values are same 
x = 4 
y = 5 
z = x + y * 6  # z=4+5*6=4+30=34;stores 34 
print(z) #34 
25 = a #error:LHS side:it should not be object 
a + b = x + y #error:LHS side:it should not be object 
# Find outputs (Home work) 
a = b = c = 25 #Declare multiple objects at a time 
print(id(a)) #address of object a 
print(id(b)) #Same address of a 
print(id(c)) # Same address of a 
print(a , b , c) # 25 25 25 
# Multiple  Assignment (Home work) 
x , y , z = 25 , 10.8 , 'Hyd' 
print(x) #25 
print(y) #10.8 
print(z)#Hyd 
# Find outputs (Home work) 
a , b , c = 3 , 4 , 5 
a *= b + c #a=a*b+c➔a=12+5=17 
print(a) #17 
# Find outputs (Home work) 
a = 20 
a %= 3 + 2 * 4 #a=a%11➔a=9 
print(a) # 9 
# Find outputs (Home work) 
a = 3 
a **= 4 #a=a**4➔a=81 
print(a) #81 
# Identity operators demo program 
a = 25 
b = 25 
print(a  is  b) #True:statisfied 
print(a  is  not  b) #False:Both are same 
print(a == b)  #True:Equal 
# Find outputs (Home work) 
a = 25 
b = 25.0 
print(a  is  b) #False:reference are compared 
print(a  is  not  b) #True: references are compared 
print(a == b) #True:object Values are compared 
# Find outputs (Home work) 
a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) #True 
print(a  is  not  b) #False 
print(a == b) #True:Object values are same 
print() #print empty string 
x = [1 , 2 , 3 , 4] 
y = [1 , 2 , 3 , 4] 
print(x is y) #False:List is not reusable 
print(x  is  not  y) #True:List is not reusable 
print(x == y) #True 
print()  #print empty string  
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4) 
print(m  is  n) #True:Tuple is reusable 
print(m  is  not  n) #False 
print(m == n) #True 
print(x == m) #False:list and tuple are two different classes. 
# Membership operators demo program (Home work) 
list = [10 , 20 , 15 , 12 , 18] 
print(15 in list) #True 
print(19 in list) #False 
print(14 not in list) #True 
print(15 not in list) #False 
s = 'Hyd is green city' 
print( 'is' in s) #True 
print('was' in s) #False 
print('g' in s) #True 
print('z' in s) #False 
print(' ' in s) #True 
print('gre' in s) #True 
print('yd i' in s) #True 
print('' in s) #Ture 
print('' not in s) #False 
# Find outputs (Home work) 
x = [1 , 2 , 3 , 4] 
y = [1 , 2 , 4 , 3] 
print(x == y) #False:not in Order 
a = (4 , 1 , 3 , 2) 
b = (4 , 2 , 3 , 1) 
print(a == b) #False:not in Order 
p = {1 , 2 , 3 , 4} 
q = {4 , 1 , 3 , 2} 
print(p == q) #True 
m = range(5) 
n = range(5) 
print(m == n) # True 
# Find outputs (Home work) 
a = [10,20,30] 
b = (10,20,30) 
print(a  is  b)  #False 
print(a  ==  b) #False 