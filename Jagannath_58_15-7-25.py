# float  object  demo  program (Home  work)
a = 10.8
print(a)              # Ref 'a' points to object 10.8
print(type(a))        #value of object 'a' <class 'float'>
print(id(a))          #address of 'a' may be 10000
b = 25.
print(b)              #Ref 'b'  points to object 25
print(type(b))        #value of object 'b' <class 'int'>
c = .689
print(c)              # Ref 'c' points to object 689
d = 3.4E2
print(d)              #Ref 'd' points to object 3.4*10*10
print(type(d))        # value of 'd' <class 'float'>
e = 9.62e-2
print(e)              #Ref 'e' points to 9.62*-10*-10
print(9.8.2)          #Invalid

# complex object demo program
a = 3 + 4j
print(a)              # Ref 'a' points to object 3+4j
print(type(a))        # value of 'a' <class 'complex'>
print(id(a))          # address of 'a' may be 1000
print(a . real)         3.0
print(a . imag)         4.0
print(type(a . real)) #<class 'float'>
print(type(a . imag)) # <class 'float'>

# Find outputs (Home work)
a = 6j
print(a)                 6j
print(type(a))           <class 'complex'>
print(a.real)             0.0
print(a.imag)             6.0
print(5 + j6)           Invalid j should not before 6
print(3 + 4i)           Invalid i should not be written instead of j
print(4+j)              Invalid value is not there before j
print(4 + 1j)           4+1j
print(4 + 0j)           4+0j

# bool object demo program  (Home  work)
a = True
print(a)                 True 
print(type(a))           <class 'boolean'>
print(id(a))             # value of 'a' may be 10000
b = False
print(b)                 False
print(type(b))           <class 'boolean'>
print(True + True)       2
print(True + False)      1
print(False + True)      1
print(False + False)     0
print(True + True + True)3
print(25 + 10.8 + True)  36.8
print(True > False)      True 
print(True)              1
print(False)             0
print(true)              Invalid 
print(false)             Invalid

# Find  outputs (Home  work)
a = 0O6247
print(a)                 Equivalence number 
print(type(a))           <class 'int'>
print(id(a))             #value of 'a' may be 1000
b = 0o6247
print(id(b))             # value of 'b' may be 10000
print(b)                 Equivalence number 
c = 3239
print(c)                 3239
print(id(c))             # Value of 'c' may be 10000
print(0o9248)            Invalid

# Find  outputs  (Home  work)
a = 0XA7B9
print(a)                 Equivalence number 
print(type(a))           <class 'int'>
b = 0xBEEF
print(b)                 Equivalence number 
print(A7B9)              Invalid 
print('A7B9')            A7B9
print(0XBEER)            Invalid 
print(0XHYD)             Invalid 
print(0xA7G9B)           Invalid

# Find outputs (Home  work)
a = 9248
print(a)                 9248
print(type(a))           <class 'int'>
