a=8
print(a)
print(type(a))
print(id(a))
print()
b=10.8
print(b)
print(type(b))
print(id(b))
print()
c=.689
print(c)
print()
d=3.4E2
print(d)#3.4*10^2=340
print(type(d))#<class 'float'>
print()
e=9.62e-2
print(e)#9.62*10^-2=0.0962
#print(9.4.3)#invalid synatax
#complex object
a=3+4j
print(a)
print(type(a))
print(id(a))
print(a.real)#3.0
print(a.imag)#4.0
print(type(a.real))
print(type(a.imag))
a=6j
print(a)
print(type(a))
print(a.real)
print(a.imag)
#print(5+j6)#error
#print(3+4i)
#print(4+j)
print(4+1j)
print(4+0j)
#bool object
a=True
print(a)
print(type(a))
print(id(a))
b=False
print(b)
print(type(b))
print(True+True)
print(True+False)
print(False+False)
print(True+True+True)
print(25+10.8+True)
print(True>False)
print(True)
print(False)
#print(true)
#print(false)
a=0xA7B9
print(a)
print(type(a))
b=0xBEEf
print(b)
print('A7B9')
#print(0xbeer)
print()
a=0o6427
print(a)
print(type(a))
print(id(a))
b=0o6427
print(id(a))#id's od a and b are same
c=3229
print(c)
print(id(c))
#print(0o9248)
#string object
a="Geo politics"
print(a)
print(type(a))
print(id(a))
b='politics'
print(b)
print(type(b))
c='''Hyd is green city
Hyd is beautiful city
Hyd is hitech city.'''
print(c)
a='Hyd'
print(a[0])
print(a[1])
print(a[2])
#print(a[3])  #  error 
print(a[-1])
print(a[-2])
print(a[-3])
#print(a[-4]) #  error
print(a[0]==a[-3])
#a[2]='c' #  TypeError: 'str' object does not support item assignment
#print(25[0])  #  TypeError: 'int' object is not subscriptable. indexing cannot be used on integer.
print('25'[0])
#print(True[0])
print('True'[0])
print()
a='Hyd'
print(a*3)
print(a*2)
print(a*1)
print(a*0)
print(a*-1)
print(25*3)
print('25'*3,sep=' ')