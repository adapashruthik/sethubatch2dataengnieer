# Find  outputs    (Home  work)

a = range(10 , 50 , 5)

print(type(a))
output:<class range>

print(a)

output:range(10 , 50 , 5) due to reference object of range is printed

print(*a)
output: 10 15 20 25 30 35 40 45

print(id(a))
output: address of an range object 

print(len(a))
output:8


print(*a[2 : 7] , sep = ' , ')
output:20 , 25 , 30 , 35 , 40
print(*a[ : : -1])
output:45 40 35 30 25 20 15 10
 
a[4] = 32
 output: error 'range' object does not support item assignment

print(a * 2)
output:ERROR DUE TO RANGE DOESNT SUPPORT DUPLICATE VALUES


#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')
output:10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)
output:0 1 2 3 4

c = range(10 , 1 , -1)
print(*c , sep = '...')
output:10...9...8...7...6...5...4...3...2

d = range(-10 , 0)
print(*d)
output:-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)
output:empty range due to positive step 1

f = range(2 , 2)
print(*f)
output:empty range due to positive step 1
g = range(10 , 11 , 0.1)
print(a)
output: error 
h = range('A' , 'F')
print(h)
output:error


#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r
print(a , b , c)
output:10,13,16

r = range(3)
x , y = r # error due to too many values
p , q  , r , s = r #error due to many variables
a , b , c = *r # doesn't need to assign * to variables a,b,c
