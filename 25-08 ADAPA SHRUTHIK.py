ADAPA SHRUTHIK

#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40} 
b = {30 , 40 , 50 , 60}
c = a . intersection(b)     
print(c)  # {30 ,40}
print(type(c)) # classs set
d = a & b    
print(d)   # {30,40}
print(type(d))   # class set 
print(c  is  d)   #  false
print(c  ==  d)    # true


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
								Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  --->  a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  there  is  no  intersection()  method  in  list  class
'''
# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)   # {10,20}
print(type(c))  # class set
d = a - b
print(d)   # {10,20}
print(type(d))  # class set
print(c  is  d)  # false
print(c  ==  d)   # true


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) Is  set . difference(list)  valid  ?  --->
							Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c) { 10,20,50,60}
print(type(c))  # class set
d = a ^ b
print(d)   #   { 10,20,50,60}
print(type(d))   # class set
print(c   is   d)  # false 
print(c  ==   d) # true


'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)  # {1,4,9,16,25,36,49,64,81,100}
print(type(a))   # class set

'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  --->  '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

program

	

Enter  input  string :  Rama Rao
String  without  duplicates  :   ao mR

'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  ---> [False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''

program

lst = eval(input("Enter a list: "))
print(list(set(lst)))

'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

lst1 = eval(input("Enter a list1: "))
lst2 = eval(input("Enter a list1: "))
a=set(lst1).intersection(lst2)
print(list(a))


#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(How  to  print  value  25  in  dict  'a')   # print(a['Empno'])
print(How  to  print  'Rama Rao'  in  dict  'a')   # print(a['Ename'])    
print(How  to  print  value  1000.65   in  dict  'a') # print(a['Sal']) 
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)     # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))    # 1000001
How  to  modify  1000.65  to  2000   # a['Sal'] = 2000   
How  to  modify  'Rama  Rao'  to  'Sita'  # a['Ename'] = 'Sita' 
How  to  modify  25   to  35   #a['Empno'] = 35
print(a)  ## {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) # 1000001
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
How  to  append  'Gender' : 'M'  to  dictionary  'a'    # a['Gender'] = 'M'  
How  to  append  'Married' :  True  to  dictionary  'a' # a['Married'] = True    
print(a) # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}
# Find  outputs (Home  work)
a = { }
How  to  append  10 : 'Rama'  to  dictionary  'a'   #  a[10] = 'Rama'
How  to  append  20 : 'Sita'  to  dictionary  'a'   # a[20] = 'Sita'
How  to  append  15 : 'Rajesh'  to  dictionary  'a'   # a[15] = 'Rajesh'
How  to  append  18 : 'Kiran'  to  dictionary  'a'    #a[18] = 'Kiran'
print(a)  #  {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)  # {'Empno': 25, 'Ename': 'Rama Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())  # true 
print(60  in  a . keys())  # false
print(60  in  a . values())  # true 
print(30  in  a . values())   #false
print(50  in  a)  # true
print(20  in  a)   # true
print(70  not  in  a . keys())   # false
print(40  not  in  a . values())  # false
print(25  not  in  a)  # true

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)  # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))   #  class str
b = eval(a)  
print(b)  #  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b))  # class dict

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)  # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)   #  false 
print(a  ==  b)   # true 
c = a
print(a  is   c)  # true 
print(a  ==  c)   # true

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}  
print(d)    #  {10, 20, 15, 18, 14, 25, 19}  
print(type(d))   # class set
e = {**a , **b , **c}
print(e)  # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'} 
print(type(e))  # class dict


'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

a = {}
n = int(input("How many employees do you want to enter: "))
for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    a[name] = salary  # Append to dictionary
print("Employee Salary Dictionary:")
print(a)


How many Employees ? : 4
Enter Emp Name : AAA
Enter Salary : 100000
Enter Emp Name : BBB
Enter Salary : 200000
Enter Emp Name : CCC
Enter Salary : 150000
Enter Emp Name : DDD
Enter Salary : 175000
{'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}


''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''



n=input("Enter String  :").split(',')

d={}
for i in n:
    a,b=i.split('=')
    d[a]=eval(b)
print(d)












a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))    # 3
b = {}
print(len(b))   # 0


'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
'''


#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))  # 90
print(sum(a . values()))  # 120
print(sum(a))    # 90
print(sum(a . items()))  # error 


# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))  # 40
print(min(a . keys()))  # 7
print(max(a . values()))  # 50
print(min(a . values()))  # 5
print(max(a . items()))  # (40,5)
print(min(a . items()))   # (7,28)
print(max(a))   # 40
print(min(a))  # 7


#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)   # {10 : 'Hyd',  20 : 'Sec', 15 : 'Cyb',20: 'Pune'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)  {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e))  #error only 2 elemts should br there
f = [[10] , [20] , [30]]
print(dict(f))   #error  2 elemts should br there
print(dict([10 , 20]))  # not valid becuse nested sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))  #  {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h))  # error 
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))  # {10: [20, 30], 40: [50, 60], 70: [80, 90]}



'''
dict()  function
------------------
1) What  is  the  argument  of  dict()  function ?  --->Nested  sequence  such  as  list  of  tuples , list  of  lists , tuple  of  tuples , tuple  of  lists,
											set  of  tuples  and  so  on

2) What  does  dict(nested-sequence)  do ?  --->  Converts  nested  sequence  to  dictionary

3) How  many  elements  can  be  in  each  inner  sequence ?  --->  Exactly  two  elements
    What  are  the  two  elements  of   each  inner  sequence ?  ---> key  and   value

4) Is  dict(sequence)  valid ?  --->  No  becoz  argument  is  not  a  nested  sequence
'''

# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)  # [5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)   # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)  # [(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) # [20,18,15,10,5]
print(a)  #  {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}

'''
Tricky  program
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''
program 

dict1= eval(input("Enter dictionary: "))
sorted = dict(sorted(dict1.items()))
print(sorted)


# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)  # {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a)  # {}
del  a
print(a)  # error because no name defined as a



# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)  # {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
print(a  is  b)   # false
print(a  ==  b)  # true 

#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)  # [10, 20, 15, 18]
print(type(b))b  # class dict
for  x  in   b:
        print(x)  # 10
20
15
18



'''
What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
'''
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)  # [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')
print(type(b))  # class dict
for  x   in   b:
        print(x)   #	(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')   #  10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune


# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') # 10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')   # error
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')    # error
for  x , y   in  a:
       print(x , y , sep = ' ... ')     # error


'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  ---> (key , value)
'''

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)  # 10
print(y)  # 20 
print(z)   # 30
print()  # prints nothing
x , y , z = a . values()
print(x)  # rama 
print(y)  # sita
print(z)    # rajesh
print()
x , y ,  z = a . items()
print(x)   # (10, 'Rama')
print(y)  # (20, 'Sita')
print(z)  #(15, 'Rajesh')
print()  # ()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)  # 10 Rama
print(rno2 , sname2)  # 20 Sita
print(rno3 , sname3)  # 15 Rajesh


'''
Tricky  program
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

1) What  is  the  string  after  it  is  converted  to  uppercase ?  --->  'RAMA RAO'

2) What  is  the  result  of  sorted('RAMA RAO') ?  --->  [' ' , 'A' , 'A' , 'A' , 'M' , 'O' , 'R' , 'R']

3) What  is  dictionary  'a'  initially ?  --->  { }

4) What  is  the  first  element  in  list ?  --->  ' '
    What  action  to  be  made  for  ' ' ?  --->  Ignore  becoz  it  is  not  an  alphabet

5) What  is  the  2nd  element  in  list ?  ---> 'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 = 0 + 1 = 1
    What  does  a['A']  =  1  do ?  --->  Appends  'A' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 1}

6) What  is  the  3rd  element  in  list ?  --->  'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 =  1 + 1 = 2
    What  does  a['A']  =  2  do ?  --->  Modifies  value  of  'A'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 2}

7) What  is  the  4th  element  in  list ?  --->  'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 =  2 + 1 = 3
    What  does  a['A'] = 3  do ?  --->  Modifies  value  of  'A'  to  3  in dict  'a'
    What  is  dictionary  'a' ?  ---> {'A' : 3}

8) What  is  the  5th  element  in  list ?  --->  'M'
     What  is  a['M']  ?  --->  	 a . get('M' , 0) + 1 =  0 + 1 = 1
    What  does  a['M'] = 1  do ?  --->  Appends  'M' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'A' : 3 , 'M' : 1}

9) What  is  the  6th  element  in  list ?  ---> 'O'
     What  is  a['O']  ?  --->  a . get('O' , 0) + 1 =  0 + 1 = 1
     What  does  a['O'] = 1  do ?  ---> Appends  'O' : 1  to  dict  'a'
     What  is  dictionary  'a' ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1}

10) What  is  the  7th  element  in  list ?  ---> 'R'
      What  is  a['R']  ?  --->  a . get('R' , 0) + 1 =  0 + 1 = 1
       What  does  a['R'] = 1  do ?  --->  Appends  'R' : 1  to  dict  'a'
	  What  is  dictionary  'a' ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 1}

11) What  is  the  last  element  in  list ?  --->  'R'
      What  is  a['R']  ?  --->  a . get('R' , 0) + 1 =  1 + 1 = 2
      What  does  a['R'] = 2  do ?  ---> Modifies  value  of  'R'  to  2  in dict  'a'
      What  is  dictionary  'a' ?  --->  	{'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}

11) Finally  what   is  dict  'a' ?  ---> {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
'''


s=input("Enter the string")
s=s.upper()
b=sorted(s)
d={}
for i in range(1,len(b)):
    d[b[i]]=d.get(b[i],0)+1
print(d)