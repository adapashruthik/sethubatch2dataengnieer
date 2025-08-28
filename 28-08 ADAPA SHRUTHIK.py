#ADAPA SHRUTHIK

'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

Enter String:RamA raO
{'A': 3, 'O': 1}
'''

n= input("Enter String:")
n= n.upper()
d= {}
for i in n:
    if i in 'AEIOU':
        d[i]= d.get(i, 0)+1
print(d)    

 
 # Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)    
print(b)  #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'} 
a . update(b)   # list does not support update 

#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)  # error in dict only 2 sequnce elemmets should be required
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)  #  error in dict only 2 sequnce elemmets should be required
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)   # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))  # <class 'dict'>

# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)  # {15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)   # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

# Find outputs  (Home  work)
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
# End  of  the  function
print('Begin')   # begin
x = f1()   
print(x)    # hyd 
	    # sec
	    # cyb

print(type(x))  # class nonetype
print('End')    # end

# Find  outputs  (Home  work)
def  f1():
	return  10 , 20 , 30
# End  of  the  function
x = f1()
print(x)    # (10,20,30)
print(type(x))  # <class 'tuple'>
a , b , c =  f1()
print(a)  # 10
print(b)  # 20
print(c)  # 30
print('for  loop')  # foe loop
for  k   in   f1():
	print(k)   # 10
			# 20
			# 30

# Find  outputs
def    f1():
        return  10
        return  20
        return  30
# End  of  the  function
print('Begin')  # begin
x = f1()
print(x)    # 10
print('End')  # end
return   100   # error no def 

#  Find  outputs
f1()# f1 not defined
def   f1():
        print('Hello')  # hello  
print(f1())
print(f1)  # hello

# Find  outputs  (Home  work)
print('Hello')   # hello
def  f1():
        print('f1  function')  # f1 function
#End  of   function
print('Hi') # hi
print(f1())   # none
print(f1)  # <function f1 at 0x7aa18f12c180>
print('Bye')   # bye

#  Find  outputs
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
#End  of  the  function
print('Begin')   # begin
print(type(f1)) # <class 'function'>
print(id(f1)) # 100001
print('End') # end

#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  # 30
print(add('Hyder' , 'abad'))  # Hyderabad
print(add(10.8 , 20.6))   # 31.4
print(add(True , False))n # 1
print(add(3 + 4j , 5 + 6j))   # (8+10j)
print(add(25 , 10.8))  # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))  # [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10 , '20'))  # error 

# Find  outputs (Home  work)
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three  argument  function :  10  20  30
f1(40 , 50) # Two  argument  function :  40  50
f1(60) # Single  argument  function  :  60
f1() # No-argument  function

'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
'''
import math
def   prime(n):
    if n>=2:
        for i in range(2,math.sqrt(n)+1):
            if n % i == 0:
                return False
    return True
'''
1) prime(25)  --->
    How  many  times  is  for  loop  executed ?  --->  5

2) prime(11) --->
    How  many  times  is  for  loop  executed ?  --->  4

3) prime(2) --->
    How  many  times  is  for  loop  executed ?  --->  0
    How  many  times  is  for  loop  executed ?  --->  0

4) prime(49) --->
    How  many  times  is  for  loop  executed ?  --->  7
'''
import math

def   prime(n):
    if n>=2:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
    return True
    
try:

    n=eval(input("Enter Integer Number :"))
    
    if prime(n):
        print("Prime Number")
    else:
        print("not a prime numebr")
except:
    print("Invalid Input")
# Find  outputs  (Home  work)
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# End  of  the  function
disp(25 , 'Rama  Rao' , 10000.0) #Emp  Number  :  25 	  Emp Name  :  Rama  Rao 	  Salary  :  10000.0
disp('Sita' , 20000.0 , 35) #Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35