#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)
OUTPUT: Rama rao
print(type(a))
OUTPUT:<class Str>
print(id(a))
OUTPUT: address of an object reference a
b = 'Hyd'
print(b)
OUTPUT:Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)

OUTPUT:Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city



# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')
OUTPUT:print(a[0])

print(How  to  print  'y'  of  object  'a')
OUTPUT:print(a[1])
print(How  to  print  'd'  of  object  'a')
OUTPUT:print(a[2])
print(a[3])
OUTPUT: index out of bonds (error) not defined
print(How  to  print  'd'  of  object  'a')
OUTPUT:print(a[-1])
print(How  to  print  'y'  of  object  'a')
OUTPUT:print(a[-2])
print(How  to  print  'H'  of  object  'a')
OUTPUT:print(a[-3])
print(a[-4])
OUTPUT: index out of bonds (error) not defined
print(a[0] ==  a[-3])
Output:True
a[2] = 'c'
output:False
print(25[0])
output:eroor due to 25 not defined Str
print('25'[0])
output:2
print(True[1])
output:eroor not defined 
print('True'[1])
output:r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)
output:HydHydHyd
print(a * 2)
output:HydHyd
print(a * 1)
output:Hyd
print(a * 0)
output: empty Str" "
print(a * -1)
output:   empty Str " "
print(25 * 3)
output:75 due to interger value multiopuied by 3 
print('25' * 3)
output:252525
print('25' * 4.0)
output:ERROR due to Str no t multipied by float
print(3 * 'Hyd')
output:HYDHYDHYD
print('25' * True)
output": 25 because True is equal to 1 25*1=25

#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))
output:hyd adress of an object reference a

a = a * 3
outpiut:hyd Str is multiplied by 3 so object hyd is converted into hydhydhyd
print(a , id(a))
output:hydhydhyd , Adress of an object reference a


# len()  function  (Home  work)
print(len('Hyd'))
output:3 due to 3 characters
print(len('Rama Rao'))
output:8
print(len('9247'))
output:4
print(len(''))
output: there is no space between the single quotes  i.e is 0
print(len(' '))
output:1
print(len(689))
output:error due to 689 is not a Str


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)
output:"hyd
print(len(a))
output:4
print(a[0])
output:" 
print("""Hyd"""")
output:hyd

b = """""Hyd"""
print(b)
output:""hyd
print(len(b))
output:5



# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])
output: Dayal  --->   string  from  indexes  7 to  12  in  steps  of   1 i.e dayal
print(a[7 : ])
output:Dayal sarma

print(a[ : 6])
output:sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])
output:'Sankar Dayal Sarma'

print(a[1 : 10 : 2])
output:akrdy due to step of 2
print(a[0 : : 2])
output:sna aa sra due to step of 2 skipped two charcaters
print(a[1 : : 2])
output:akrdylsra   due to step of 2 skipped two charcaters
print(a[-5 : -1])
output: sarm
print(a[::-1])
output:amras layad raknas
print(a[-1:-5:-1])
output:amra
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3])
output:kar Dayal s
print(a[2 : -5])
output:ankar dayal 
print(a[-1:-5])
output:amra
print(a[3 : 3])
output:k due to same index step of 1


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1



#  Find  outputs  (Home  work)
a =  'A'
print(a[1])
output: error due to index out of range
print(a[1:])
output: EMPTY DUE TO NO CHARACTER IN POSITION 1



# int()  function  demo  program
print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) 0
output:Converts  bool   object    False  to  int  object 0
print(int('25'))
output:25
print(int('0075'))
output:0075
print(int(0B11010))
output:26
print(0B11010)
output:26
print(int(0O6247))
output:3239  converts octa decimal to int object
print(0O6247)
output:3239 octa decimal to int object

print(int(0XA7B9))
output:42937 converts hexa decimal to int object

print(0XA7B9)
output:42937 convertion of hexa decimal to decimal equivalent
print(int(3 + 4j))
output:  ERROR
print(int('25.4'))
output:25.4
print(int('Ten'))
output:error 



'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer





# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False))
OUTPUT:0.0
print(float('92'))
OUTPUT:92.0
print(float('36.4'))
OUTPUT:36.4
print(float('0075'))
OUTPUT:75.0
print(float(0B1010101))
OUTPUT:85.0
print(float(0O6247))
OUTPUT:3239.0
print(float(0XA7B9))
OUTPUT:42937.0
print(float(3 + 4j))
OUTPUT:sTRING

print(float('Ten'))

OUTPUT:ERROR





'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float




# complex()  function  demo  program
print(complex(3 , 4))
OUTPUT:3+4J
print(complex(0 , 4))
OUTPUT:4J
print(complex(3))
OUTPUT:3+0J
print(complex(3.8 , 4.6))
OUTPUT:(3.8+4.6j)
print(complex(3.8))
OUTPUT:3.8+0J
print(complex(3 , 4.5))
OUTPUT:3+4.5J
print(complex(True , False))
OUTPUT:1+0J
print(complex(True))
OUTPUT:1+0J
print(complex(False))
OUTPUT:0J
print(complex(True , 4))
OUTPUT:1+4J
print(complex('3'))
OUTPUT:3+0J
print(complex('3.8'))
OUTPUT:3.8+0J
print(complex(3 , '4'))
OUTPUT:ERROR  DUE TO 2ND ARG IS sTR
print(complex('3' , 4))
OUTPUT:ERROR   DUE TO FIRST ARG IS sTR
print(complex('3' , '4'))
OUTPUT:ERROR DUE TO FIRST ARG IS sTR
print(complex('Ten'))
OUTPUT:ERROR





#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25))#   True :  -25  is  non-zero

print(bool(0.0))
OUTPUT:False
print(bool(0.1))
output:True is  non-zero


print(bool(0 + 0j))
outout:False
print(bool(10 + 20j))
output:True
print(bool(-15j))
output: True -15  is  non-zero
print(bool('False'))

output:True due to non empty Str
print(bool(''))
output:False due to empty Str

print(bool('Hyd'))
output:True
print(bool(' '))
output:true
print(bool('True'))
output:True


'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ? --->  False
    What  about  non-zero ?  --->  True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  --->  False
    What  about  non-empty  string ?  --->	True

4) When  is  x + yj  treated  as  False ?  --->  When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as  True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''



# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8))
output:'10.8'
print(str(3 + 4j))
output:"3+4j"
print(str(True))
output:"True"
print(str(False))
output:"False"
print(str(None))
output:"None"


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''

# oct()  function  demo  program
print(oct(195))
output:0o303 convert decimal integer to octal integer
print(oct(0B10101110010))
output:0o2562

print(oct(0xA7B9))
output:0o123671














'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number

# hex()  function  demo  program
print(hex(25))
output:0x19
print(hex(0B10101111010111))
output:0x2bd7
print(hex(0O6247))
output:0xca7






'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number
