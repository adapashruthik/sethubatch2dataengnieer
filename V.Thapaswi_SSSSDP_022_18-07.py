#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)
print(*a)
print(type(a))
print(id(a))
print(len(a))
a[2] = 'Sec'
print(a)
print(a[2 : 5])
print()
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)
a . remove('Hyd')
print(a)
#a . remove('25')#error
print(a)
print()
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)
print(id(a))
print(a * 3)
print(a * 2)
print(a * 1)
print(a * 0)
print(a * -1)
#print(a * 4.0)#error
a = a * 3
print(a)
print(id(a))
a = [25]
#print(a * a)#error
print()
# list()  function  demo  program
a = list('Hyd')
print(a)
print(type(a))
print(len(a))
b = (10 , 20 , 15 , 18)
print(list(b))
print(list(range(5)))
#print(list(25))#error
print()
# Find  outputs
a = [ ]
print(type(a))
print(a)
print(len(a))
b = list()
print(b)
print(len(b))
print()
# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])
print(list[ : : ])
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])
print(list[ : : 2])
print(list[1 : : 2])
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])
print(list[1 : 4])
print(list[-4 : -1])
print()
#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)
print('y : ' , y)
for  x  in  list[2:7]:
	print(x)
print()
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))
a[1 : 4] = [60 , 70]
print(a , id(a))
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))
print()
#  Find  outputs  (Home  work)
a =  [25]
#print(a[1])#error
print(a[1:])

print()
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a * 4)
print(b * 4)
print(c * 4)
print(d * 4)
print()
# Find  outputs (Home  work)
a = ()
print(type(a))
print(a)
print(len(a))
b = tuple()
print(b)
print(len(b))
print()
# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)
print(id(a))
a = a * 2
print(a)
print(id(a))
print()
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)
print(type(a))
print(len(a))
#print(a[2])#error
#print(a[1 : 4])#error
#a[2] = 'Sec'#error
#print(a * 2)#error
#print(a * a)#error
print()
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)
print(len(a))
print(type(a))
print()
#  set()  function demo  program
a = set('Rama rAo')
print(a)
print(len(a))
print(set([10 , 20 , 15 , 20]))
print(set((25 , 10.8 , 'Hyd' , 10.8)))
print(set(range(10 , 20 , 3)))
#print(set(25))#error
#print(set([25 , 10.8 , [] , 'Hyd']))#error
print()
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a)
print(b)
print(c)
print(d)
print()
# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)
print(len(a))
a . remove(25)
print(a)
#a . append(100)#error
#a . add(set())#error
a . add(())
#a . add([])#error
print(a)
#a . add({})#error
print()
