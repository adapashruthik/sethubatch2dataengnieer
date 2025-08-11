#1.  Find  outputs  (Home  work)

a = "Rama Rao" # Ref 'a' points to string object "Rama Rao"
print(a) # Prints value of object 'a' i.e. "Rama Rao"
print(type(a)) # Type of object 'a' i.e. <class 'str'>
print(id(a)) # Adress of object 'a'
 
b = 'Hyd' # Ref 'b' points to string object "Hyd"
print(b) # Prints value of object 'b' i.e.  "Hyd"

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.''' # Ref 'c' points to string object " Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city".It is a multi line string.
print(c) # Prints value of object 'c'


#2. Index   demo  program  (Home  work)

a = 'Hyd' # Ref 'a' points to string object "Hyd"
print(How  to  print  'H'  of  object  'a') # we can print "H" by using statement "print(a[0])"
print(How  to  print  'y'  of  object  'a') # we can print "y" by using statement "print(a[1])"
print(How  to  print  'd'  of  object  'a') # we can print "d" by using statement "print(a[2])"
print(a[3]) #Gets error because there is no 4th character in String 'a'
print(How  to  print  'd'  of  object  'a') # we can print "d" by using statement "print(a[-1])"
print(How  to  print  'y'  of  object  'a') # we can print "y" by using statement "print(a[-2])"
print(How  to  print  'H'  of  object  'a') # we can print "H" by using statement "print(a[-3])"
print(a[-4]) # Gets error because there is only 3 character in 'a'
print(a[0] ==  a[-3]) # Prints True because the condition is true.
a[2] = 'c' # Error due to String is an immutable object,we can't change or modify
print(25[0]) # Error due to syntax ,int object can't have indexes concept 
print('25'[0]) # prints '2' of string object '25'
print(True[1]) #Error due to bool objects don't have indexes concept 
print('True'[1]) # Prints 'r' of String 'True'



#3.  Find  outputs  (Home work)

a = 'Hyd' # Ref 'a' points to string object 'Hyd'
print(a * 3) # Prints object 'a' into three times i.e. 'HydHydHyd'
print(a * 2) # Prints object 'a' into two times i.e. 'HydHyd'
print(a * 1) # Prints object 'a' into one times i.e. 'Hyd'
print(a * 0) # Prints object 'a' into zero times i.e. ''(Empty string)
print(a * -1) # we can not print string into -1 times, result will be empty 
print(25 * 3) # prints 25 times 3 i.e. 75 because they are int objects
print('25' * 3) # Prints object '25' into three times i.e. '252525'
print('25' * 4.0) # Error due to 4.0,it should be int object not float object 
print(3 * 'Hyd') # Prints object 'Hyd' into three times i.e. 'HydHydHyd'
print('25' * True) # Prints object '25' into one time i.e. '25' , because value of True is 1 in operations



#4.  Find  outputs  (Home work)

a = 'Hyd' # Ref 'a' points to string object 'Hyd' 
print(a , id(a)) # Prints value of object 'a' i.e. 'Hyd' and adress of object 'a' 
a = a * 3 # 'a' will be updated as three times i.e. 'HydHydHyd'
print(a , id(a)) # Prints value of object 'a' i.e. 'HydHydHyd' and adress of object 'a'


#5. len()  function  (Home  work)

print(len('Hyd')) # Prints length of string object 'Hyd' i.e. 3
print(len('Rama Rao')) # Prints length of string object 'Rama Rao' i.e. 8
print(len('9247')) # Prints length of string object '9247' i.e. 4
print(len('')) # Prints length of string object '' i.e. 0
print(len(' ')) # Prints length of string object ' ' i.e. 1
print(len(689)) # Error because of there is no length of int objects



#6. Find  outputs  (Home  work)

a = """"Hyd""" # Ref 'a' points to string object '"Hyd'
print(a) # Prints value of object 'a' i.e. '"Hyd'
print(len(a)) # Prints length of string object 'a' i.e. 4
print(a[0]) # Print 0th index of object 'a' i.e. "
print("""Hyd"""") # Print 'Hyd"'
(b = """""Hyd""" # Ref 'b' points to string object '""Hyd'
print(b) # Print value of object 'b' i.e. '""Hyd'
print(len(b)) # Prints length of string object 'b' i.e. 5)



#8 Find  outputs
a = 'Sankar Dayal Sarma' # Ref 'a' points to string object '"Sankar Dayal Sarma'

print(a[7 : 12]) # Prints string  from  indexes  7  to  11  in  steps  of   1  i.e. Dayal
print(a[7 : ])  # Prints string  from  indexes  7  to  string length -1 i.e. 17  in  steps  of   1  i.e. Dayal Sarma
print(a[ : 6])  # Prints string  from  indexes  0  to  5  in  steps  of   1  i.e. Sankar
print(a[ : ])  #  a[ 0 :  18  : 1]  --->   string  from  indexes  0  to  17  in  steps  of   1  i.e.  Sankar<space>Dayal<space>Sarma
print(a[:  : ])  # Prints string  from  indexes  0  to  17 in  steps  of   1  i.e. Sankar Dayal Sarma
print(a[1 : 10 : 2])  # Prints string  from  indexes  1  to  9  in  steps  of   2  i.e. akrDy
print(a[0 : : 2])  # Prints string  from  indexes  0  to 17 in  steps  of   2  i.e. Sna aa am
print(a[1 : : 2]) # Prints string  from  indexes  1  to 17 in  steps  of   2  i.e. akrDylSra
print(a[-5 : -1]) # Prints string  from  indexes  -5  to -2 in  steps  of   1  i.e. Sarm
print(a[::-1]) # Prints string  from  indexes  -1  to -18 in  steps  of   1  i.e. amraS layaD raknaS
print(a[-1:-5:-1]) # Prints string  from  indexes  -1 to -4 in  steps  of   -1 i.e. amraS
print(a[ : : -2]) #   a[-1 :  -19 : -2]  --->  string  from  indexes  -1  to  -18  in  steps  of   -2  i.e.  arSlyDrka
print(a[3 : -3]) # Prints string  from  indexes  3  to -4 in  steps  of   1  i.e. kar Dayal Sa
print(a[2 : -5]) # Prints string  from  indexes  2 to -6 in  steps  of   1  i.e. nkar Dayal
print(a[-1:-5]) # Prints empty because there is no steps 
print(a[3 : 3])# prints empty due to there is no range between two indexes



#9.  Find  outputs  (Home  work)

a =  'A' # Ref 'a' points to string object 'A'
print(a[1]) # Error because string index out of range
print(a[1:]) # Error because string index out of range



#10. int()  function  demo  program

print(int(10.8))  #  Converts  float   object  10.8  to  int  object  10
print(int(True))  #  Converts  bool   object    True  to  int  object 1
print(int(False)) #  Converts  bool  object  False  to  int  object  0
print(int('25')) #  Converts  string object  '25'  to  int  object  25
print(int('0075')) #  Converts  string object '0075' to  int  object  75
print(int(0B11010)) #  Converts  binary number 11010  to  int  object  26
print(0B11010) #  Converts  binary number 11010  to  decimal equivalent number 26
print(int(0O6247)) #  Converts  octal number 6247  to  int  object  3239
print(0O6247) #  Converts  octal number 6249  to  decimal equivalent number 3239
print(int(0XA7B9)) #  Converts  hex number A7B9 to  int  object  42937
print(0XA7B9) #  Converts  hex number A7B9 to decimal equivalent number 42937
print(int(3 + 4j)) # Error
print(int('25.4')) #  Converts  float   object  25.4  to  int  object  25
print(int('Ten')) # Error because string Ten cannot be converted into int object



#11. complex()  function  demo  program

print(complex(3 , 4)) # Converts int objects 3 , 4 to complex object (3 + 4j)
print(complex(0 , 4))# Converts int objects 0 , 4 to complex object (0 + 4j)
print(complex(3))# Converts int object 3 , 0 to complex object (3 + 0j)
print(complex(3.8 , 4.6))# Converts float objects 3.8 , 4.6 to complex object (3.8 + 4.6j)
print(complex(3.8))# Converts float object 3.8, 0 to complex object (3.8 + 0j)
print(complex(3 , 4.5))# Converts int and float objects 3 , 4.5 to complex object (3 + 4.5j)
print(complex(True , False))# Converts bool objects 1 , 0 to complex object (1 + 0j)
print(complex(True))# Converts bool objects 1 , 0 to complex object (1 + 0j)
print(complex(False))# Converts bool objects 0 , 0 to complex object (0j)
print(complex(True , 4))# Converts int and bool objects 1 , 4 to complex object (1 + 4j)
print(complex('3'))# Converts string objects '3' to complex object (3 + 0j)
print(complex('3.8'))# Converts string objects '3.8' to complex object (3.8 + 0j)
print(complex(3 , '4'))# Error because second argument cannot be string
print(complex('3' , 4))# Error due to complex() cannot take second argument if first argument is string
print(complex('3' , '4'))# Error due to complex() cannot take second argument if first argument is string
print(complex('Ten'))# Error due to not changeable String to complex


#12. float()  function  demo  program

print(float(25))  #  Converts  int  object  25  to  float  object   25.0
print(float(True))   #  Converts  bool  object   True   to  float  object   1.0
print(float(False)) #  Converts  bool  object False  to  float  object   0.0
print(float('92')) #  Converts  string object  '92' to  float  object  92.0
print(float('36.4')) #  Converts  string  object  '36.4'  to  float  object   36.4
print(float('0075')) #  Converts  string  object  '0075  to  float  object   75.0
print(float(0B1010101)) #  Converts  binay number 1010101  to  float  object   85.0
print(float(0O6247))#  Converts  octal number 6247  to  float  object   3239.0
print(float(0XA7B9))#  Converts  hex number A7B9  to  float  object   42937.0
print(float(3 + 4j))# Error due to float object must be real object not complex
print(float('Ten'))#Error due to non changeable string Ten to float object




#13. str()  function  demo  program

print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) #  Converts   10.8  to  '10.8'
print(str(3 + 4j))#  Converts   3+4j to  '(3+4j)'
print(str(True))#  Converts    True to  'True'
print(str(False))#  Converts  False  to  'False'
print(str(None))#  Converts  None  to  'None'


#14.  bool()  function  demo  program

print(bool(0)) #  Converts   0  to  False
print(bool(10)) #  Converts   10 to  True Because 10 is non zero
print(bool(-25))#  Converts   -25  to  True
print(bool(0.0))#  Converts  0.0  to  False
print(bool(0.1))#  Converts   0.1 to  True
print(bool(0 + 0j))#  Converts   0+0j  to  False
print(bool(10 + 20j)) #  Converts   10+20j  to  True
print(bool(-15j))#  Converts   -15j to  True
print(bool('False'))#  Converts   'False' to  True
print(bool(''))#  Converts   ''  to  False
print(bool('Hyd'))#  Converts   'Hyd'  to  True
print(bool(' '))#  Converts   ' '  to  True
print(bool('True'))#  Converts   'True'  to  True



#15. hex()  function  demo  program

print(hex(25)) # Converts  int object 25 to hex number 0X19
print(hex(0B10101111010111))# Converts  binary number 10101111010111 to hex number 0X2bd7
print(hex(0O6247))# Converts  octal number 6247 to hex number 0Xca7



#16. oct()  function  demo  program

print(oct(195))# Converts  int object 195 to octal number 0o303
print(oct(0B10101110010))# Converts  binary number 10101110010 to octal number 0o2562
print(oct(0xA7B9))# Converts  hex number A7B9 to octal number 0o123671
