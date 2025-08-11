# float  object  demo  program (Home  work)
a = 10.8
print(a) # 10.8
print(type(a))# <class,float>
print(id(a))#21231503732390
b = 25.
print(b)#25.0
print(type(b)) #<class,float>
c = .689
print(c)#0.689
d = 3.4E2
print(d)#340.0
print(type(d))#<class,float>
e = 9.62e-2
print(e)#0.0962
print(9.8.2) #invalid syntax


# complex object demo program
a = 3 + 4j
print(a)#(3+4j)
print(type(a))#<class,'complex'>
print(id(a))#128758524544689
print(a . real)#3.0
print(a . imag)#4.0
print(type(a . real))#<class,'float'>
print(type(a . imag))#<class,'float'>

# Find outputs (Home work)
a = 6j
print(a)#6j
print(type(a))#<class,'complex'>
print(a.real)#0.0
print(a.imag)#6.0
print(5 + j6)#NameError: name 'j6' is not defined
print(3 + 4i)  #invalid decimal literal
print(4+j)#NameError: name 'j' is not defined
print(4 + 1j)#(4+1j)
print(4 + 0j)#(4+0j)

 # bool object demo program  (Home  work)
a = True
print(a)#True
print(type(a))#<class,'bool'>
print(id(a))#123169342041089
b = False
print(b)#False
print(type(b))#<class,'bool'>
print(True + True)#2
print(True + False)#1
print(False + True)#1
print(False + False)#0
print(True + True + True)#3
print(25 + 10.8 + True)#36.8
print(True > False)#True
print(True)#True
print(False)#False
print(true)#NameError: name 'true' is not defined.
print(false)#NameError: name 'false' is not defined.

# Find  outputs (Home  work)
a = 0O6247
print(a)#3239
print(type(a))#<class,'int'>
print(id(a))#154826429831312
b = 0o624
print(id(b))#154826429831312
print(b)#3239
c = 3239
print(c)#3239
print(id(c))#184262400857326
print(0o9248)#SyntaxError: invalid digit '9' in octal literal

# Find  outputs  (Home  work)
a = 0XA7B9
print(a)#42937
print(type(a))#<class ,'int'>
b = 0xBEEF
print(b)#48879
print(A7B9)#NameError: name 'A7B9' is not defined
print('A7B9')#A7B9
print(0XBEER)#SyntaxError: invalid hexadecimal literal
print(0XHYD)#SyntaxError: invalid hexadecimal literal
print(0xA7G9B)#SyntaxError: invalid hexadecimal literal

 # Find outputs (Home  work)
a = 9248
print(a)#9248
print(type(a))#<class,'int'>