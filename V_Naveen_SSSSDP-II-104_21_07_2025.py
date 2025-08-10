#1.  Find   outputs (Home work)

i = 10 # Ref 'i' points to int object 10
i = not  i > 14
print(i) # Prints True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # Prints True


#2. not  operator  demo  program

print(not  True) #   False
print(not  False) #  True
print(not  25) # False
print(not  0) # True
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) # False
print(not  not  'Hyd') # True


'''
not  operator
----------------
1) What  does  not  operator  do ?  ---> Complement  operation

2) Is  not  a  unary  operator  ?  ---> Yes  due  to  single  operand
    What  about  and ,  or ? ---> Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  --->  Right  to  Left
    What  is  the  associativity  of  binary  operators ?  --->  Left  to  Right  except  for  **
'''



#3.  or  operator  demo program

print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)  #  False
print(10  or  20) #  10
print(0   or  20)  #  20
print(-25  or  0) # -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # (3 + 4j)
print('Hyd'   or   10.8) # 'Hyd'


'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  ---> When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''



#4. Chaining  relational  opeartors  (Home work)

print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30) # False
print(1 < 2 < 3 < 4) # True
print(1 < 2 > 3 > 1) # False
print(4 > 3 >= 3 > 2) # True


#5.  Find  outputs  (Home  work)

print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd') # True
print('Rama'  <=   'Ramana') # True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') # True


'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->  Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? --->  1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  ---> 512

5) What  is  the  range  of  unicode  values ?  ---> 0  to  511

6) What  are  the  unicode  values  of  'A'  to  'Z'  ?  ---> 65  to  90
     What  are  the  unicode  values  of  'a'  to   'z'  ?  --->  97  to  122
     What  are  the  unicode  values  of   '0'  to  '9' ?  ---> 48  to  57
     What  is  the  unicode  value  of   '$' ?  --->  36
     What  is  the  unicode  value  of  space ?  ---> 32

7) What  is  another  name  of  unicode ?  --->  Extended  Ascii (American  standard  code  for  information  and  interchange)
'''



#6.  Relational  operators  demo  program (Home  work)

print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8) # True : < is satisfied
print(6 <= 6) # True : = is satisfied
print(6 <= 4) # False : both < and = are not satisfied
print(9 != 7) # True : != is satisfied
print(6 == 8) # False : == is not satisfied
print(True  >  False) # True : > is satisfied
print(3 + 4j == 3 + 4j) # True : == is satisfied
print(3 + 4j == 5 + 6j) # False : == isw not satisfied
print(3 + 4j != 5 + 6j) # True : != is not satisfied
print(10 == 10.0) # True : == is satisfied
print(3 + 4j >  3 + 4j) # Error


'''
1) Can  complex  numbers   be  compared ?   ---> Yes  with  ==  and  !=

2) When  can  complex  numbers   be  not  compared  ?  ---> Wiith  > , <  , >=  and  <=
'''



#7. ** operator demo program

print(3 ** 4) # 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) # 262144
print(3 + 4 * 5 - 32 / 2 ** 3) # 19.0




'''
**  operator
---------------
1) What  is  **  operator  called ?  --->  Exponential  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a ** b  ** c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  ---> Left  to  right '''



#8. Find outputs

print(7 / 0) # Error due to zero division error
print(7 // 0) # Error due to zero division error
print(7 % 0) # Error due to zero division error



#9. % operator demo program

print(9 % 5) # 4
print(9.0 % 5) # 4.0
print(9 % 5.0) # 4.0
print(9.0 % 5.0) # 4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3) # 2.9


'''
%   operator
---------------
1) What  does  %  operator  do ?  ---> Performs  division  and  returns  remainder

2) When  is  the  result  of  %  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of  %  operator  float ?  ---> When  at  least  one  operand  is  float
'''



#10.  //  operator  demo  program

print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2) # 4.0
print(9 // 2.0) # 4.0
print(9.0 // 2.0) # 4.0
print(10.5 // 2) # 5.0
print(10 // 3) # 3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3) # 2.0
print(18 // 4) # 4
print(-18 // 4) # -5
print(-(18 // 4)) # -4



'''
//  operator
--------------
1) What  does  //  operator do ?  --->  Same  as  /  operator  but  returns  previous  integer  of  /  result

2) What  is  the  result  of  integer // integer ?  --->  Integer  quotient
    What  is  the  result  of  integer // float ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  ---> Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0

3) What  is  the  result  of  integer / integer ?  ---> Float  quotient
    What  is  the  result  of  integer / float ?  ---> Float  quotient
    What  is  the  result  of  float / integer ?  ---> Float  quotient
    What  is  the  result  of  float / float ?  ---> Float  quotient

4) When  is  the  result  of  //  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of   //  operator  float  with  .0 ?  ---> When  at  least  one  operand  is  float
'''



#11.  /  operator  demo  program

print(9.0 / 2) # 4.5
print(9 / 2.0) # 4.5
print(9.0 / 2.0) # 4.5
print(9 / 2)  #  4.5
print(10.5 / 2) # 5.25
print(10 / 3) # 3.33
print(10 / 2) # 5.0


'''
What  does  /  operator  do  ?  --->  Peforms  division   and  returns  float  quotient
'''



#12. Find outputs (Home work)

print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9 + 38j)
print(3 + 4j * 5 + 6j) # (3 + 26j)
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # Error due to sequence(list) can not be multiplied by non float, it should be integer
print({10 , 20 , 15} * 2) # Error due to set does not contain duplicate elements
print({10 : 20 , 30 : 40} * 2) # Error due to dictionary does not contain duplicate keys
print([10] * [20]) # Error due to sequence can not be multiplied with sequence



#13. Find outputs (Home work)

print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j) # (8 + 10j)
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [ 10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd' , 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # Error due to set elements can not be duplicated
print({10 : 'Hyd'} + {20 : 'Sec'}) # Error due to dict keys cannot be duplicated
print(range(4) + range(5)) # Error due to range elemets cannot be duplicated
print(10 + '20') # Error due to non Sequence elemets can not be added with sequence elements
print([10 , 20 , 30] + 5) # Error due to non Sequence elemets can not be added with sequence elements
print([10 , 20 , 30] + (40 , 50 , 60)) # Error due to non list object can not be cancatenated ,it is possible with list to list



#14. Find  outputs(Home  work)

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False because a and b have different references
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False because c and d have different references
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # False because a and b have different references
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False because g and h have different references



#15. Find  outputs  (Home  work)

a = 25
b = 25
print(a  is  b) # True due to python internally caches small integers from -5 to 256
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True due to python automatically interns some strings --especially short strings
e = False
f = False
print(e  is  f) # True due to python uses a singleton for True and False
g = range(10)
h = range(10)
print(g  is  h) # False due to python creates new memory when each time we call range()



#16.  Find  outputs  (Home  work)

a = 'Hyd'
print(id(a)) # Address of String object 
a[1] = 'e' # Error due to string is not indexed and immutable
a = 'Sec'
print(id(a)) # Address of String object, which is different from above address 
b = (10 , 20 , 15 , 18)
print(id(b)) # Address of tuple 
b[2] = 19 # Error due to tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b)) # Address of tuple, which is different from above address of 1st tuple object
c = range(5)
print(id(c)) # Address of range object
c[3] = 10  # Error due to range is immutable
c = range(5)
print(id(c)) # Address of range object, which is same address because same range object



#17. Find  outputs (Home  work)

a = 25.7
print(id(a)) # Address of float object
print(a) # 25.7
a = 35.6 
print(id(a)) # Address of float object, which is different from 1st float object
print(a) # 35.6
b = True
print(id(b)) # Address of bool object
b = False
print(id(b)) # Address of bool object, which is different from 1st bool object
c = None
print(id(c)) # Address of NoneType object
c = None
print(id(c)) # Address of NoneType object, which is same address of 1st NoneType object



#18.  Find  outputs

a = 25
print(id(a)) # Address of the int object 
a = 35
print(id(a)) # Address of the int object, which is different from 1st int object



#19.  Anonymous  object  demo  program

_ = 25
print(_) # 25
print(type(_)) # Type of int object <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # O Hello <nextline> 1 Hello <nextline> 2 Hello <nextline> 3 Hello <nextline> 4 Hello <nextline>
	                     


'''
1) What  is   _   called ?   --->  Anonymous  object  (or) Nameless  object

2) How  many  nameless  objects  can  be  a  program ?  --->  Just  one  (or)  zero

3) What  happens  when  another  nameless  object  is  created ?  --->  Existing  nameless  object  gets  deleted

4) Can  there  be  multiple  nameless  objects  in  a  program ?  --->  No

5) _ = 10
    _ = 20
   What  happens  when  _ = 20  is  executed ?  --->  A  new  nameless  object  is  created  with  value  20  and
																				  old  nameless  object  with  10  is  lost
'''



#20.  Find  outputs (Home  work)

a = {
		print('Hyd') , # Hyd
		print('Sec') , # Sec
		print('Cyb') # Cyb
	} 
print(type(a)) # Type of set object <class 'set'>
print(a) # {None} because there is no values in set
print(len(a)) # 1



#21. How  to  print  dictionary  in  different  ways

a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # 'Dictionary  with  print  function' i.e. {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
How  to  print  dictionary  with  print()  function
print(a.keys()) #'Keys  of  dictionary' i.e. dict_keys([10, 20, 15, 18])
How  to  print  each  key  of  dict  'a'
print(a.values()) #'Values  of  dictionary' i.e. dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])
How  to  print  each  value  of  dict  'a'
print(a.items()) #'All  the  tuples  of  dict_items   object' i.e. dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])
How  to  print  each  tuple  of  the  list  in  dict_items  object
for t in a.items:
    print(t) #'Elements  of  each   tuple' i.e. (10, 'Ramesh') <nextline> (20, 'Kiran') <nextline> (15, 'Amar') <nextline> (18, 'Sita')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
for k, v in a.items:
	print(k, '-->', v) #'Keys  and  values  of  dictionary' i.e. 10 --> Ramesh <nextline> 20 --> Kiran <nextline> 15 --> Amar <nextline> 18 --> Sita
How  to  print  each  key  and  corresponding  value  in  dict  'a'
