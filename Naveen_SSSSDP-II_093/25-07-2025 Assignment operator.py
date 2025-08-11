a=25
print(a)
b=a
print(b)
print(a is b)
x=4
y=5
z=x+y*6
print(z)
#25=a
#a+b=x+y

a=b=c=25
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
#Multiple assignment
x,y,z=25,10.8,'Hyd'
print(x)
print(y)
print(z)
#plus equal
a=7
print(a,id(a))
a+=5
print(a,id(a))
#star equal
a,b,c=3,4,5
a*=b+c
print(a)
#percentile equal
a=20
a%=3+2*4
print(a)
#double star equal
a=3
a**=4
print(a)