# ADAPA SHRUTHIK

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30))   # ERROR 

'''
(10,20,15,18)
<class 'tuple'>
4

()
ERROR!
<class 'tuple'>
0

([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100, 200, 150),)
<class 'tuple'>
1



'''


#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	return sum(a)/len(a)
	# End  of  the  function
print(avg(10 , 20 , 15 , 18))  # 15.75
print(avg(25 , 10.8 , True))   # 12.26
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))  # true 
print(avg())  # error 
print(avg(25))  # 25.0
print(avg(3 + 4j , 5 + 6j))  # (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))  # error

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
    return ' '.join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # sankar dayal sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # hyd is green city
print(concat('Python', 'Is', 'A', 'Great', 'Language'))  # python is a great language 
print(concat())  # 
print(concat('Python'))  # python 
print(concat(1, 2, 3))  # error

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)    #a : 10  \t   b  :  (20,30,40)
f1(50 , 60)   #a : 50  \t   b  :  (60,)
f1(70)  #a : 70  \t   b  :  ()
f1(a = 80)   # #a : 80  \t   b  :  ()
f1(b = (10 , 20 , 30) , a = 40)  # #Error
f1()    #a : 25 \t   b  :  ()
f1(a = 10 , (20 , 30 , 40))  # Error
f1(25 , b = (10 , 20 , 30))  #Error
f1(25 , a = (10 , 20 , 30))#Error
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10,20,30)  \t   b  :  (10,20,30)
f1(a = (10 , 20 , 30),10,20,30)#Error


#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)   #a : (10,20,30)  \t   b  :  40 	
f1(50 , b = 60) #a : (50,)  \t   b  :  60
f1(b = 70) # #a : ()  \t   b  :  70
f1(b = 10 , a = (20 , 30 , 40))  # #Error
f1(b = 10 , (20 , 30 , 40))  # #Error
f1() # #Error
f1(10 , 20 , 30 , (10 , 20 , 30))  #Error
f1(10 , 20 , 30 , 40)# #Error
f1(25)  # #Error
f1(10 , 20 , 30 , b = (10 , 20 , 30))   #a : (10,20,30)  \t   b  :  (10,20,30)


#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) #a  :  10  \t  b  :  (20,30,40)  \t  c  :  50
f1(60 , 70 , c = 80) #a  :  60  \t  b  :  (70,)  \t  c  :  80
f1(90 , c = 100)#a  :  90  \t  b  :  ()  \t  c  :  100
f1(a = 1 , 2 , c = 3)#Error
f1(1 , 2 , 3) #Error	
f1(a = 1 , b = 2 , c = 3)   #Error
f1(a = 25 , 100 , 200 , 300 , c = 35)#Error


# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):  # invalid 
        pass  
def  f2(*a , b):  # vallid
        pass
def  f3(a , *b): # valid
        pass
def  f4(a , b): # valid
        pass
def    f5(a , *b , c):  # valid
        pass
def   f6( * , a , *b , c):  # invalid
       pass
def   f7(a , *b , c ,  /):  # invalid
       pass

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40},(50,60))

'''output
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''

# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

'''
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender='m')
f1()
'''
output
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results
'''

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary=10000.0)

''' 
output
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)  # #Emp  Number  :  25  \t  Emp  Name  :  Sita  \t  Salary  :	10000.0')
f1(empno = 25 , empname = 'Sita' , salary = 10000.0) #Error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)  #  #{'empno' : 25 , 'ename' : 'Sita' , 'sal' : 10000.0}
f2(empno = 25 , empname = 'Sita' , salary=10000.0) #{'eno' : 25 , 'empname' : 'Sita' , 'salary' : 10000.0}
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
'''
output
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''


'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5

Hint:  Use  while  loop

Iteration         a          op        b        result
------------------------------------------------------
       1               3          +          4           7   --->  'a'

	   2              7          *          5           35   --->  'a'

	   3             35         -          6           29   --->  'a'

	   4             29         /          2           14.5   --->  'a'

	   5            14.5       =          ---           ----
'''
#Program
exp=input("Enter an Expresion: ")
a=int(exp[0])
i=1
while exp[i]!='=':
    if exp[i]=='+':
        a=a+int(exp[i+1])
    elif exp[i]=='*':
        a=a*int(exp[i+1])
    elif exp[i]=='-':
        a=a-int(exp[i+1])
    elif exp[i]=='/':
        a=a/int(exp[i+1])
    i+=2
print(a)


'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch     int(ch)       a[int(ch)]         s
--------------------------------------------------------
                                                                     ''
     1              '9'       9               'Nine'          '' + 'Nine' + ' '

	 2             '2'       2               'Two'          'Nine ' + 'Two' + ' '

	 3             '4'       4               'Four'          'Nine Two ' + 'Four' + ' '

	 4             '7'       7               'Seven'        'Nine Two Four ' + 'Seven' + ' '
'''

n=input("Enter a number")
a=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
s=''
for x in n:
    s=s+a[int(x)]+' '
print(s)

'''
Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                                                  PACES
									                  ACESP
												      CESPA
												      ESPAC

2) What  are  the  indexes  of  SPACE ?  ---> 0  to  4
     What  are  the  indexes  of  PACES ?  ---> 1  to  4 , 0  to  0
     What  are  the  indexes  of  ACESP ?  ---> 2  to  4 , 0  to  1
     What  are  the  indexes  of  CESPA ?  ---> 3  to  4 , 0  to  2
     What  are  the  indexes  of  ESPAC ?  ---> 4  to  4 , 0  to  3

3) What  are  the  indexes  in  general ?  --->  i  to  length - 1   and   0  to  i - 1
'''
s=input("Enter a string: ")
for i in range(len(s)):
    print(s[i:]+s[:i])

'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                        	7 * 2 = 14
				 7 * 3 = 21
				 .....
				 7 * 10 = 70
'''

n=int(input("Enter input: "))
for i in range(1,11):
    print(F'{n} * {i} = {n*i}')


'''
Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
---------------------
       1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'
'''

n=int(input("Enter no.of lines: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i):
        ch=chr(65+j)
        print(ch+' ',end='')
    print()


'''
Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M
900  -  CM
500 -  D
400 - CD
100 -   C
90  -  XC
50  -  L
40  -  XL
10  -  X
9  -  IX
5  -  V
4  -  IV
1  -  I

1) What  is  the  output  if  input  is  3878 ? ---> MMMDCCCLXXVIII 

2) What  is  the  result  of  3878 // 1000 ?  --->  3
    How  many  M's  are  concatenated  to  the  sting ?  --->  Three  becoz  3878 / 1000  is  3
    What  is  the  result  of  3878 % 1000 ?  --->  878

3) What  is  the  result  of  878 // 900 ?  --->  0
    How  many  CM's  are  concatenated  to  the  string ?  ---> Zero  becoz  878 / 900  is  0
    What  is  the  result  of  878 % 900 ?  --->  878

4) What  is  the  result  of  878 // 500 ?  ---> 1
     How  many  D's  are  concatenated  to  the  string ?  ---> One  becoz  878 / 500  is  1
     What  is  the  result  of  878 % 500 ?  ---> 378
      and  so  on
'''
n=int(input("Enter a number: "))
s=''
a={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
for x in a.keys():
    c=n//x
    s=s+(c)*a[x]
    n=n%x
print(s)

#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) 
	print('b : ' , b) 
	print('c : ' , c) 
	print() 
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')
'''
a :  10
b :  20
c :  30

a :  11
b :  40
c :  31

a :  50
b :  22
c :  32

Bye

'''

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)

'''
10
20
11
'''