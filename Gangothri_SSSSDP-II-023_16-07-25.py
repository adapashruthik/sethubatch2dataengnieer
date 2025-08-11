#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class 'str'>
print(id(a)) # Address of object a
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # it will line by line

# Index   demo  program  (Home  work)
a = 'Hyd'
print('Hyd'[0])  #  Char  at  index  0  of  object    'Hyd'  i.e.  'H'
print('Hyd'[1])  #  Char  at  index  1   of  object    'Hyd'  i.e.  'y'
print('Hyd'[2])  #  Char  at  index  2   of  object    'Hyd'  i.e.  'd'
print(a[3]) #  Error  :   Index  3  does  not  exist   in  'Hyd'
print('Hyd'[-1])  #  Char  at  index   -1    of  object    'Hyd'  i.e.  'd'
print('Hyd'[-2])  #  Char  at  index   -2    of  object    'Hyd'  i.e.  'y'
print('Hyd'[-3])  #  Char  at  index   -3    of  object    'Hyd'  i.e.  'H'
print(a[-4])  #  Error  :   Index  -4  does  not  exist   in  'Hyd'
print(a[0] ==  a[-3]) #  'H' == 'H'  is  True
a[2] = 'c'  #  Error :   'd'  can  not  be  replaced  with  'd'  as  str  object  is  immutable
print(25[0]) #  Error : Non-sequence  (such  as  int)  is  not  indexed
print('25'[0])  #  Char  at  index  0  of  object  '25'  i.e.  '2'
print(True[1])   #  Error :  Non-sequence  (such  as  bool)  is  not  indexed
print('True'[1])  #  Char  at  index  1   of  'True'    i.e.  'r'

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #  Repeats  string  thrice  i.e.  HydHydHyd
print(a * 2)  #  Repeats  string  twice   i.e.  HydHyd
print(a * 1)  #  Repeats  string  once   i.e.  Hyd
print(a * 0)  #  Repeats  string   0  times    i.e.   Empty  string
print(a * -1)  #  Repeats  string   -1   times    i.e.   Empty  string
print(25 * 3)  # 75
print('25' * 3) # 252525
print('25' * 4.0) #  Error due to float  operand  4.0
print(3 * 'Hyd')  #  HydHydHyd
print('25' * True)  #  Repeats  string  once    i.e.  25

#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) # Hyd   address of Hyd
a = a * 3
print(a, id(a)) # HydHydHyd  adress
      
# len()  function  (Home  work)
print(len('Hyd'))
print(len('Rama Rao'))
print(len('9247'))
print(len(''))
print(len(' '))
print(len(689))

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # "Hyd
print(len(a)) # 4
print(a[0]) # ""
print("""Hyd"""") # Error due to extra quotes while closing
b = """""Hyd"""
print(b) # ""Hyd
print(len(b)) #5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #  a[7 : 12 : 1]  --->  string from indexes 7 to 11 in steps of 1 i.e. Dayal
print(a[7 : ]) # a[7:18:1] ----> string from index 7 to 17 insteps of 1 i.e.Dayal Sarma
print(a[ : 6]) # a[0:6:1] ---> string from index 0 to 5 in step of 1 i.e. Sankar
print(a[ : ]) #a[0:18:1] ---> string from index 0 to 17 instep of 1 i.e. Sankar  Dayal  Sarma
print(a[:  : ])  #  a[0 : 18 : 1]  --->  string  from  indexes  0  to  17   in  steps  of   1  i.e.  Sankar  Dayal  Sarma
print(a[1 : 10 : 2]) #a[1:10:2] ---> string from indexes 1 to 9 in steps of 2 i.e.akrDy
print(a[0 : : 2]) #a[0:18:2] ---> string from indexes 0 to 17 in steps of 2 i.e.Sna<space>aa<space>am
print(a[1 : : 2]) #a[1:18:2] ---> string from indexes 1 to 17 in steps of 2 i.e. akrDylSra
print(a[-5 : -1]) #a[-5:-1:1] ---> string from indexes -5 to  -2   insteps of 1 i.e.Sarm
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18   in  steps  of   -1  i.e.  Reverse  string
print(a[-1:-5:-1]) #string from indexes -1 to -4 in steps of -1 i.e. amra
print(a[ : : -2]) #a[-1:-19:-2]--->string from indexes -1 to -18 in steps of -2 i.e. arSlyDrka
print(a[3 : -3])  #  a[3 : -3 : 1]  --->  string  from  indexes  3  to  -4  in  steps  of   1  i.e.  kar<space>Dayal<space>Sa
print(a[2 : -5]) #a[2:-5:1] --->string from indexes 2 to -6 in steps of 1 i.e. nkar<space>Dayal<space>
print(a[-1:-5]) #a[-1:-5:1]--->string from indexes -1 to  -6 in steps of 1 i.e.  Empty string
print(a[3 : 3]) #a[3:3:1]--->string from indexes 3 to 2 in steps of 1 i.e.  Empty string

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error because index 1 does not exist
print(a[1:]) # String without first char

# int()  function  demo  program
print(int(10.8))   #  Converts  10.8  to  10
print(int(True))    #  Converts   True  to   1
print(int(False)) # Converts False to 0
print(int('25')) #  Converts  '25'  to  25
print(int('0075')) #  Converts  '0075'  to   75
print(int(0B11010)) #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(0B11010)  #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(int(0O6247))  #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(0O6247)   #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(int(0XA7B9))   #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(0XA7B9)  #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(int(3 + 4j)) #  Error  :  complex  number  can not be converted to int
print(int('25.4')) #  Error :  string  float  can not be converted to int
print(int('Ten'))  #  Error :  'Ten'  can not be converted to int

# float()  function  demo  program
print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) # 0.0
print(float('92')) # 92.0
print(float('36.4')) # 36.4
print(float('0075')) # 75.0
print(float(0B1010101)) # 85.0
print(float(0O6247)) # 3239.0
print(float(0XA7B9)) # 42937.0
print(float(3 + 4j)) # error
print(float('Ten')) # error

# complex()  function  demo  program
print(complex(3 , 4)) # (3+4j)
print(complex(0 , 4)) # 4j
print(complex(3)) # (3+0j)
print(complex(3.8 , 4.6)) # (3.8+4.6j)
print(complex(3.8)) # (3.8+0j)
print(complex(3 , 4.5)) # (3+4.5j)
print(complex(True , False)) # (1+0j)
print(complex(True)) # (1+0j)
print(complex(False)) # 0j
print(complex(True , 4)) # (1+4j)
print(complex('3')) # (3+0j)
print(complex('3.8')) # (3.8+0j)
print(complex(3 , '4')) # Error 
print(complex('3' , 4)) # Error
print(complex('3' , '4')) # Error
print(complex('Ten')) # Error

#  bool()  function  demo  program
print(bool(0)) #   False
print(bool(10)) #   True :  10  is  non-zero
print(bool(-25)) # True
print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool(0 + 0j)) # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True
print(bool('False')) # True
print(bool('')) # True
print(bool('Hyd')) # True
print(bool(' ')) # True
print(bool('True')) # True

# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) #'10.8'
print(str(3 + 4j)) #'3+4j'
print(str(True)) # 'True'
print(str(False)) # 'False'
print(str(None)) # 'None'

# oct()  function  demo  program
print(oct(195)) # 00303
print(oct(0B10101110010)) # 002562
print(oct(0xA7B9)) # 00123671

# hex()  function  demo  program
print(hex(25)) #0X19
print(hex(0B10101111010111)) #0x2BD7
print(hex(0O6247)) # 0xca7
