#Mutable Elements
#Float
a=10.8
print(a)#10.8
print(type(a))#<class 'float'>
print(id(a))#2115027146064
b=25.
print(type(b))#<class 'float'>
c=.689
print(c)#0.689
d=3.4E2
print(d)#340.0
print(type(d))#<class 'float'>
e=9.62e-2
print(e)#0.0962
print(9.8.2)
#SyntaxError: invalid syntax. Perhaps you forgot a comma?

#Complex
a=3+4j
print(a)# (3+4j)
print(type(a)) #<class 'complex'>
print(id(a))# 1373801487184
print(a.real)
3.0
print(a.imag)
4.0
print(type(a.real))
<class 'float'>
print(type(a.imag))
<class 'float'>

a=6j
print(a)
6j
print(type(a))
<class 'complex'>
print(a.real)
0.0
print(a.imag)
6.0
print(5+j6)
NameError: name 'j6' is not defined
print(3+4i)
SyntaxError: invalid decimal literal
print(4+j)
NameError: name 'j' is not defined
print(4+1j)
(4+1j)
print(4+0j)
(4+0j)

#Octal to Binary Conversion

a=0O6247
print(a)
3239
print(type(a))
<class 'int'>
print(id(a))
2244103117680
b=0o6247
print(id(b))
2244103119280
print(b)
3239
c=3239
print(id(c))
2244103119312
print(0o9248)
SyntaxError: invalid digit '9' in octal literal

#Hexadecimal to Decimal Conversion
a=0XA7B9
print(a)
42937
print(type(a))
<class 'int'>
b=0xBEEF
print(b)
48879
print(A7B9)
NameError: name 'A7B9' is not defined
print('A7B9')
A7B9
print(0XBEER)
SyntaxError: invalid hexadecimal literal (R is not Hexadecimal Element)
print(0XHYD)
SyntaxError: invalid hexadecimal literal(HY is not Hexadecimal Element)
print(0xA7G9B)
SyntaxError: invalid hexadecimal literal(G is not Hexadecimal Element)

#String

a="Rama Rao"
print(a)
Rama Rao
print(type(a))
<class 'str'>
print(id(a))
1320874296496
b='Hyd'
print(b)
Hyd
c='''Hyd is grren city.
Hyd is hitec city.
Hyd is Beautiful city.'''
print(c)
Hyd is grren city.
Hyd is hitec city.
Hyd is Beautiful city.

#Indexing
print(a[0])
H
print(a[1])
y
print(a[2])
d
print(a[3])
IndexError: string index out of range
print(a[-1])
d
print(a[-2])
y
print(a[-3])
H
print(a[-4]) 
IndexError: string index out of range
print(a[0]==a[-3])
True
a[2]='c'
TypeError: 'str' object does not support item
print(25[0])
TypeError: 'int' object is not subscriptable
print('25'[0])
2
print(True[1])
TypeError: 'bool' object is not subscriptable
print('True'[1])
r

#Star Operator as Repeater
a='Hyd'
print(a*3)
HydHydHyd
print(a*2)
HydHyd
print(a*1)
Hyd
print(a*0)

print(a*-1)

print(25*3)
75
print('25'*3)
252525
print('25'*4.0)
TypeError: can't multiply sequence by non-int of type 'float'
print(3*'Hyd')
HydHydHyd
print('25'*True)
25

#Length Function
print(3*'Hyd')
HydHydHyd
print('25'*True)
25
a='Hyd'
print(a,id(a))
Hyd 1635613762544
a=a*3
print(a,id(a))
HydHydHyd 1635613152432
print(len('Hyd'))
3
print(len('Rama Rao'))
8
print(len('9247'))
4
print(len(''))
0
print(len(' '))
1
print(len(689))
TypeError: object of type 'int' has no len()

#multiple quotes
a=""""Hyd"""
print(a)
"Hyd
print(len(a))
4
print(a[0])
"
print("""Hyd"""")
      
SyntaxError: unterminated string literal (detected at line 1)
b=""""""Hyd"""
print(b)
print(len(b))
"""
#Slicing

a = 'Sankar Dayal Sarma'
print(a[7 : 12])#Dayal
print(a[7 : ])#Dayal Sarma
print(a[ : 6])#Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])#Sankar Dayal Sarma
print(a[1 : 10 : 2])#akrDy
print(a[0 : : 2])#Sna aa am
print(a[1 : : 2])#akrDylSra
print(a[-5 : -1])#Sarm
print(a[::-1])#amraS layaD raknaS
print(a[-1:-5:-1])#amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])#kar Dayal Sa
print(a[2 : -5])#nkar Dayal
print(a[-1:-5])#empty
print(a[3 : 3])#empty

#type Conversion & Input
print(int(10.8))  #  Converts  float object  10.8  to  int  object  10
print(int(True))  #  Converts  bool object    True  to  int  object 1
print(int(False)) #0
print(int('25'))#25
print(int('0075'))#75
print(int(0B11010))#26
print(0B11010)#26
print(int(0O6247))#3239
print(0O6247)#3239
print(int(0XA7B9))#42937
print(0XA7B9)#42937
print(int(3 + 4j))#ERROR!TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print(int('25.4'))#ERROR!ValueError: invalid literal for int() with base 10: '25.4'

print(int('Ten'))#ValueError: invalid literal for int() with base 10: 'Ten'


print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))#0.0
print(float('92'))#92.0
print(float('36.4'))#36.4
print(float('0075'))#75.0
print(float(0B1010101))#85.0
print(float(0O6247))#3239.0
print(float(0XA7B9))#42937.0
print(float(3 + 4j))#TypeError: float() argument must be a string or a real number, not 'complex'

print(float('Ten'))#ValueError: could not convert string to float: 'Ten'


print(complex(3 , 4))#3+4j
print(complex(0 , 4))#4j
print(complex(3))#3+0j
print(complex(3.8 , 4.6))#3.8+4.6j
print(complex(3.8))#3.8+0j
print(complex(3 , 4.5))#3+4.5j
print(complex(True , False))#1+0j
print(complex(True))#1+0j
print(complex(False))#0j
print(complex(True , 4))#1+4j
print(complex('3'))#3+0j
print(complex('3.8'))#3.8+0j
print(complex(3 , '4'))#TypeError: complex() second arg can't be a string
print(complex('3' , 4))#TypeError: complex() can't take second arg if first is a string

print(complex('3' , '4'))#TypeError: complex() can't take second arg if first is a string
print(complex('Ten'))#ValueError: complex() arg is a malformed string      

print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))#True
print(bool(0.0))#False
print(bool(0.1))#True
print(bool(0 + 0j))#False
print(bool(10 + 20j))#True
print(bool(-15j))#True
print(bool('False'))#True
print(bool(''))#False
print(bool('Hyd'))#True
print(bool(' '))#True
print(bool('True'))#True

#Range
a = range(10 , 50 , 5)
print(type(a))#range(10, 50, 5)
print(a)#range(10, 50, 5)
print(*a)#10 15 20 25 30 35 40 45
print(id(a))#138599604903328
print(len(a))#8
print(*a[2 : 7] , sep = ' , ')#20 , 25 , 30 , 35 , 40
print(*a[ : : -1])#45 40 35 30 25 20 15 10
a[4] = 32#TypeError: 'range' object does not support item assignment
print(a * 2)#SyntaxError: invalid non-printable character U+00A0      


a = range(10 , 20)
print(*a , sep = ',')#10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)#0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')#10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)#empty
f = range(2 , 2)
print(*f)#empty
g = range(10 , 11 , 0.1)#TypeError: 'float' object cannot be interpreted as an integer

h = range('A' , 'F')#SyntaxError: invalid non-printable character U+00A0

r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)#10 13 16
r = range(3)
x , y = r#ValueError: too many values to unpack (expected 2)
p , q  , r , s = r#ValueError: not enough values to unpack (expected 4, got 3)
a , b , c = *r#SyntaxError: invalid non-printable character U+00A0
      
#LIst
a=[25,10.8,'Hyd',True,3+4j,None,'Hyd',25]
   
print(a)
   
[25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)
   
25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))
   
<class 'list'>
print(id(a))
   
2705009846976
print(len(a))
   
8
a[2]='Sec'
   
print(a)
   
[25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2:5])
   
['Sec', True, (3+4j)]
print(a[::-1])
   
[25, 'Hyd', None, (3+4j), True, 'Sec', 10.8, 25]

#List Methods
a=[]
   
print(a)
   
[]
a.append(25)
   
a.append(10.8)
   
a.append('Hyd')
   
a.append(True)
   
print(a)
   
[25, 10.8, 'Hyd', True]
a.remove('Hyd')
   
print(a)
   
[25, 10.8, True]
a.remove('25')
   
ValueError: list.remove(x): x not in list
print(a)
   
[10.8, True]
      
#* Operator
a=[25,10.8,'Hyd']
print(a)#[25, 10.8, 'Hyd']
print(id(a))#139621793991104
print(a*3)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a*2)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a*1)#[25, 10.8, 'Hyd']
print(a*0)#[]
print(a*-1)3#[]
print(a*4.0)#TypeError: can't multiply sequence by non-int of type 'float'
a=a*3
print(a)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))#139621792309696
a=[25]
print(a*a)#TypeError: can't multiply sequence by non-int of type 'list'      


a = list('Hyd')
print(a)#['H', 'y', 'd']
print(type(a))#<class 'list'>
print(len(a))#3
b = (10 , 20 , 15 , 18)
print(list(b))#[10, 20, 15, 18]
print(list(range(5)))#[0, 1, 2, 3, 4]
print(list(25))#TypeError: 'int' object is not iterable
a = [ ]
print(type(a))#[]
print(a)
print(len(a))#0
b = list()
print(b)#[]
print(len(b))#0

      
#Slicing in list
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[2 : 7])#[(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])#[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])#[25, (3+4j), True, 10.8]
print(list[1 : : 2])#[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#[10.8, True, (3+4j), 25]
print(list[1 : 4])#[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])#[True, None, 10.8]
print(list[3 : -3])#['Hyd', True]
print(list[2 : -5])#[(3+4j)]
print(list[-1:-5])#[]


#Iterating through list
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)#x :  Hyd
print('y : ' , y)#y :  True
for  x  in  list[2:7]:
	print(x)#(3+4j)
#output      
#Hyd
#True
#None
#10.8

a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#[10, 20, 30, 40, 50] 137314123827648
a[1 : 4] = [60 , 70]
print(a , id(a))#[10, 60, 70, 50] 137314123827648
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#SyntaxError: invalid non-printable character U+00A0

#Index out of range      
a =  [25]
print(a[1])#IndexError: list index out of range
print(a[1:])#IndexError: list index out of range

#Tuple
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#<class 'int'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'int'>
print(type(d))#<class 'tuple'>
print(a * 4)#100
print(b * 4)#(25, 25, 25, 25)
print(c * 4)#SyntaxError: invalid non-printable character U+00A0
print(d * 4)#SyntaxError: invalid non-printable character U+00A0

a = tuple('Hyd')
print(a)#('H', 'y', 'd')
print(type(a))#<class 'tuple'>
print(len(a))#3
b = [10 , 20 , 15 , 18]
print(tuple(b))#(10, 20, 15, 18)
print(tuple(range(5)))#(0, 1, 2, 3, 4)
print(tuple(25))#TypeError: 'int' object is not iterable


a = ()
print(type(a))#<class 'tuple'>
print(a)#()
print(len(a))#0
b = tuple()
print(b)#()
print(len(b))#0

a = (10 , 20 , 30)
print(a)#(10, 20, 30)
print(id(a))#138645167248256
a = a * 2
print(a)#(10, 20, 30, 10, 20, 30)
print(id(a))#138645168472704
      
#SET
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{None, True, 25, 10.8, 'Hyd', (3+4j)}
print(type(a))#<class 'set'>
print(len(a))#6
print(a[2])#TypeError: 'set' object is not subscriptable
print(a[1 : 4])
a[2] = 'Sec'
print(a * 2)#SyntaxError: invalid non-printable character U+00A0
print(a * a)#SyntaxError: invalid non-printable character U+00A0      

a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{False, 1, 'Hyd', ''}
print(len(a))#4
print(type(a))#<class 'set'>


a = set('Rama rAo')
print(a)#{'r', 'm', ' ', 'o', 'R', 'a', 'A'}
print(len(a))#7
print(set([10 , 20 , 15 , 20]))#{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))#{16, 10, 19, 13}
print(set(25))#TypeError: 'int' object is not iterable
print(set([25 , 10.8 , [] , 'Hyd']))#TypeError: unhashable type: 'list'

a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#<class 'list'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'dict'>
print(type(d))#<class 'set'>
print(a)#[]
print(b)#()
print(c)#{}
print(d)#set()

      
#DICTIONARY
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)#{None, True, 10.8, 'Hyd', 25}
print(len(a))#5
a . remove(25)
print(a)#{None, True, 10.8, 'Hyd'}
a . append(100)#AttributeError: 'set' object has no attribute 'append'
a . add(set())
a . add(())
a . add([])
print(a)#{None, True, 10.8, 'Hyd'}
a . add({})#SyntaxError: invalid non-printable character U+00A0


a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10:'Sec'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))#4

a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10:'Sec'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))#4

a = { [ ] : 25}#TypeError: unhashable type: 'list'
b = { ( ) : 25}
print(b)#{(): 25}
c = { { } : 25}#TypeError: unhashable type: 'dict'
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}#SyntaxError: invalid non-printable character U+00A0      

a = {}
print(type(a))#<class 'dict'>
print(len(a))#0
print(a)#{}
b = dict()
print(type(b))#<class 'dict'>
print(len(b))#0
print(b)#{}

      
#Accessing keys and values
a={10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(a)#{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(a.keys())#dict_keys([10, 20, 15, 18])
print(a.values())#dict_values(['Ramesh', 'Kiran', 'Amar', 'Sita'])
print(a.items())#dict_items([(10, 'Ramesh'), (20, 'Kiran'), (15, 'Amar'), (18, 'Sita')])
      

a={
    print('Hyd'),#Hyd
    print('sec'),#sec
    print('cyb')#cyb
  }
print(type(a))#<class 'set'>
print(a)#{None}
print(len(a))#1
      
_=25
print(_)#25
print(type(_))#<class 'int'>
a,_,c=10,20,30
print(a)#10
print(_)#20
print(c)#30
for _ in range(5):
    print(_,'Hello')#0 Hello
                    #1 Hello
                    #2 Hello
                    #3 Hello
                    #4 Hello

#Reusable and non resuable objects 
a=25
print(id(a))#137405425673672
a=35
print(id(a))#137405425673992
print(a)#35

a=25.7
print(id(a))#132664455809168
print(a)#25.7
print(type(a))#<class 'float'>
a=35.6
print(id(a))#132664455818864
print(a)#35.6
b=True
print(id(b))#132664467449280
b=False
print(id(b))#132664467448832
print(b)#False
c=None
print(id(c))#132664467414112
c=None
print(id(c))#132664467414112      

a='Hyd'
print(id(a))#139572569840624
a[1]='e'#TypeError: 'str' object does not support item assignment
a='Sec'
print(id(a))#136002770017792
b=(10,20,15,18)
print(id(b))#136002770044144
b[2]=19#TypeError: 'tuple' object does not support item assignment
b=(30,40,35,32)
print(id(b))#135155044828560
c=range(5)
print(id(c))#135155044801712
c[3]=10#TypeError: 'range' object does not support item assignment
c=range(5)
print(id(c))#137386893647120

a=25
b=25
print(a is b)#True
c='Hyd'
d="Hyd"
print(c is d)#True
e=False
f=False
print(e is f)#True
g=range(10)
h=range(10)
print(g is h)#False

a=[10,20,15,18]
b=[10,20,15,18]
print(a is b)#False
c={10:20,30:40}
d={10:20,30:40}
print(c is d)#False
e=(10,20,15,18)
f=(10,20,15,18)
print(e is f)#True
g={10,20,15,18}
h={10,20,15,18}
print(g is h)#False
#Arithmetic Operators     
print(10+20)#30
print(10.8+20.6)#31.400000000000002
print(3+4j+5+6j)#(8+10j)
print(True+False)#1
print("Hyder"+'abad')#Hyderabad
print('Sankar'+'Dayal'+'Sarma')#SankarDayalSarma
print('10'+'20')#1020
print([10,20,30]+[1,2,3])#[10, 20, 30, 1, 2, 3]
print((25,10.8,"hyd")+(3+4j,True,None))#(25, 10.8, 'hyd', (3+4j), True, None)
print({10,20}+{30,40})#TypeError: unsupported operand type(s) for +: 'set' and 'set'

print({10:"Hyd"},{20:"Sec"})#{10: 'Hyd'} {20: 'Sec'}
print(range(4)+range(5))#TypeError: unsupported operand type(s) for +: 'range' and 'range'
print(10+"20")#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([10,20,30]+5)#TypeError: can only concatenate list (not "int") to list
print([10,20,30]+(40,50,60))#TypeError: can only concatenate list (not "tuple") to list


print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#(-9+38j)
print(3 + 4j * 5 + 6j)#(3+26j)
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2)#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#TypeError: can't multiply sequence by non-int of type 'float'
print({10 , 20 , 15} * 2)#TypeError: unsupported operand type(s) for *: 'set' and 'int'
print({10 : 20 , 30 : 40} * 2)#TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print([10] * [20])#SyntaxError: invalid non-printable character U+00A0

print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#(-9+38j)
print(3 + 4j * 5 + 6j)#(3+26j)
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2)#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)#(25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#TypeError: can't multiply sequence by non-int of type 'float'
print({10 , 20 , 15} * 2)#TypeError: unsupported operand type(s) for *: 'set' and 'int'
print({10 : 20 , 30 : 40} * 2)#TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print([10] * [20])#SyntaxError: invalid non-printable character U+00A0

print(9.0 / 2)#4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#5.25
print(10 / 3)#3.33333
print(10 / 2)#5.0

print(9 // 2)  #   prev  integer  of (4.5) = 4
print(9.0 // 2)#4.0
print(9 // 2.0)#4.0
print(9.0 // 2.0)#4.0
print(10.5 // 2)#5.0
print(10 // 3)#3
print(10.0 // 3)  #    prev  integer  of  3.33 = 3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)#-5
print(-(18 // 4))#-4

print(9 % 5)#4
print(9.0 % 5)#4.0
print(9 % 5.0)#4.0
print(9.0 % 5.0)#4.0
print(10.5 % 2)  #   0.5
print(8.9 % 3)#2.9000000000000004

print(7 / 0)#ZeroDivisionError: division by zero
print(7 // 0)#ZeroDivisionError: integer division or modulo by zero
print(7 % 0)#SyntaxError: invalid non-printable character U+00A0
print(3 ** 4)#81
print(10 ** -2)#0.01
print(4 ** 3 ** 2)#262144
print(3 + 4 * 5 - 32 / 2 ** 3)#19.0
      
#Comparison Operators
print(9 >= 5)  #   True :  >  is  satisfied
print(9 >= 9)   #   True :  =  is  satisfied
print(9 >= 12)   #  False :  Both  are  not  satisfied
print(6 <= 8)#True
print(6 <= 6)#True
print(6 <= 4)#False
print(9 != 7)#True
print(6 == 8)#False
print(True  >  False)#True
print(3 + 4j == 3 + 4j)#True
print(3 + 4j == 5 + 6j)#False
print(3 + 4j != 5 + 6j)#True
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#TypeError: '>' not supported between instances of 'complex' and 'complex'

print('Rama'   >  'Rajesh')  #   True :  'm' > 'j'
print('Rama'  <  'Sita') #  True : 'R' < 'S'
print('Hyd'  ==  'Hyd')#True
print('Rama'  <=   'Ramana')#True
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#True

print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #   False : 10  is  not  >= 20
print(10 < 20 > 30)#False
print(1 < 2 < 3 < 4)#False
print(1 < 2 > 3 > 1)#False
print(4 > 3 >= 3 > 2)#SyntaxError: invalid non-printable character U+00A0

#Logical Operators
print(True  or  False) #  True
print(False  or  True) #   True
print(True  or  True) #  True
print(False  or   False)   #  False
print(10  or  20)#  10
print(0   or  20)  #  20
print(-25  or  0)#-25
print(''  or  35)#35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#(3+4j)
print('Hyd'   or   10.8)#Hyd

print(not  True) #   False
print(not  False) #  True
print(not  25)#False
print(not  0)#True
print(not  'Hyd')#False
print(not  '')#True
print(not  -10)#False
print(not  not  'Hyd')#True

i = 10
i = not  i > 14
print(i)#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#SyntaxError: invalid non-printable character U+00A0

print({10,20} | {30,20})#{10, 20, 30}
print({10:'Hyd',20:'Sec'} | {30:'Cyb',20:'Vja'})#{10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5))#TypeError: unsupported operand type(s) for |: 'range' and 'range'
print([10,20]|[30,20])#TypeError: unsupported operand type(s) for |: 'list' and 'list'

#Assignment Operators
a=25
print(a)#25
b=a
print(b)#25
print(a is b)#True
x=4
y=5
z=x+y*6
print(z)#34
25=a#SyntaxError: cannot assign to literal here. 
a+b=x+y#SyntaxError: cannot assign to expression here.

a=b=c=25
print(id(a))#138252158272968
print(id(b))#138252158272968
print(id(c))#138252158272968
print(a,b,c)#25 25 25

x,y,z=25,10.8,'Hyd'
print(x)#25
print(y)#10.8
print(z)#'Hyd'

a,b,c=3,4,5
a*=b+c
print(a)#27

a=20
a%=3+2*4
print(a)#9
a=3
a**=4
print(a)#81

#is and in operator
a=25
b=25
print(a is b)#True
print(a is not b)#False
print(a==b)#True      

a=25
b=25.0
print(a is b)#False
print(a is not b)#True
print(a==b)#True

a='Hyd'
b='Hyd'
print(a is b)#True
print(a is not b)#False
print(a==b)#True
print()
x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)#False
print(x is not y)#True
print(x==y)#True
print()
m=(1,2,3,4)
n=(1,2,3,4)
print(m is n)#True
print(m is not n)#False
print(m==n)#True
print(x==m)#False

list=[10,20,15,12,18]
print(15 in list)#True
print(19 in list)#False
print(14 not in list)#True
print(15 not in list)#False
s='Hyd is green City '
print('is' in s)#True
print('was' in s)#False
print('g' in s)#False
print('z' in s)#False
print('' in s)#True
print('gre' in s)#True
print('yd i' in s)#True
print(" in s)#SyntaxError: unterminated string literal 
print(" not in s)#SyntaxError: unterminated string literal

x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)#False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)#False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)#True
m = range(5)
n = range(5)
print(m==n)#True

a = [10,20,30]
b = (10,20,30)
print(a  is  b) #False
print(a==b)#False

a = 25
print(++a)  #  +(+a) = +a  =  25
print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a)#25
print(a--)#SyntaxError: invalid syntax
print(a--1)#26
print(-a)#-25
print(+-a)#-25
print(-+a)#-25

print('One');#One
print('Two');#Two
print('Three')#Three
print('hyd'); print('Sec') print('Cyb') #hyd
                                        #Sec
                                        #Cyb
