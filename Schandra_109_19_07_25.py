# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
output:{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))
output: <class dictonary>
print(How  to  obtain  value  key  10)
output:print(a[10])
print(How  to  obtain  value  key  20)
output:print(a[20])
print(How  to  obtain  value  key  15)
output:print(a[15])
print(How  to  obtain  value  key  18)
output:print(a[10])
print(a[19])
output:error 
print(a[0])
output:error due to no key in dictonary
print(a['Amar'])
output:error due to not called the output by using value
How  to  modify  value  of   key  15  to  'Krishna'
output:a[15]='Krishna' 
How  to  remove  20 :  'Kiran'  from  dict  'a'
output: del a[20] 
How  to  append  25 : 'Vamsi'  to  dict  'a'

output:a[25]='Vamsi'

print(a)
output:{10 : 'Ramesh' ,  15 : 'Amar' , 18 : 'Sita',25:'Vamsi'}
print(len(a))

output:4
print(a * 2)

output:error due to dictonary cannot repeat

# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)
output:{10:'sec'}
print(len(a))
output:1 
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)
output:{'R' : 'Red' , 'G' : 'Green' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}

print(len(b))
output:5

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)
output:{True:'may be'}
print(len(a))
output:1

# Find  outputs
a = { [ ] : 25}
output:error 
b = { ( ) : 25}
print(b)
output:{():25}
c = { { } : 25}
output:error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
output:{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))
output:1
e = {set() : 10.8}
output:error due to doesn't keep multiple keys and single value



# Find  outputs
a = {}
print(type(a))
output:<class dict>
print(len(a))
output:0
print(a)
output:{}
b = dict()
print(type(b))
output:<class dict>
print(len(b))
output:0
print(b)
output:{}
