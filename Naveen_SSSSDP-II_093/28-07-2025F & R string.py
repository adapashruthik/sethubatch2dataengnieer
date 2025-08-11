#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))
print()
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
#print(F'{x =}  \t   {y =}   \t  {z =}')           # no object in x , y , z
print()
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')
print(x)
#F string assignment
x=25
print(F'{x}')
print(F'x')
print('{x}')
print('x')
print(x)
print(F'x={x}')
print(F'{x=}')
print(F'x=')
print(F'x:{x}')
print(F'{x:}')
print()
#R string 
a='Hyd is \n green \t city'
print(a)
b=R'Hyd is \n green \t city'
print(b)
c='Hyd is \\n green \\t city'
print(c)