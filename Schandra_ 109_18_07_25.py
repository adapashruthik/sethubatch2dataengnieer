#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)
output: [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]

print(*a)
output:25  10.8  'Hyd'  True  3 + 4j  None 'Hyd'  25

print(type(a))

output:<class LIST> 

print(id(a))

OUTPUT: Adress of an obect list

print(len(a))	  

output: 8

a[2] = 'Sec'
print(a)
output:[25 , 10.8 , 'sec' , True , 3 + 4j , None , 'Hyd' , 25]

print(a[2 : 5])

output: ['sec', trur, 3+4j]

 # append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)
output: empty list
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)

output:[25,10.8,'hyd',True]

a . remove('Hyd')

print(a)
output:[25,10.8,True]

a . remove('25') //error due to str 25 is not there to remove
print(a)
 output:[25,10.8,True]


 #  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)
output:[25, 10.8, 'Hyd']
print(id(a))
output:adress of an object list 
print(a * 3) 
output:[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)
output:[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)
 output:[25, 10.8, 'Hyd']
print(a * 0)
output:[] due to *0 it will be 0 i.e empty

print(a * -1)
output:[] due to -1 it will be 0 i.e empty
print(a * 4.0)
output: error due to not multiplied with non int type float
a = a * 3
print(a)
output:[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']


print(id(a))
output:adress of an object list
a = [25]
print(a * a)
output:error list not a integer

 # list()  function  demo  program
a = list('Hyd')
print(a)
output:['h','y','d']
print(type(a))
OUTPUT:<CLASS LIST>
print(len(a))
OUTPUT: ///3
b = (10 , 20 , 15 , 18)
print(list(b))
OUTPUT:[10,20,15,18]
print(list(range(5)))
OUTPUT:[0,1,2,3,4]
print(list(25))
OUTPUT:ERROR DUE TO NOT ITERABLE OR coma is not there


'''
list()  function
'''
 # Find  outputs
a = [ ]
print(type(a))
output:class list1>
print(a)
output:[ ]
print(len(a))

output:0 due to no elements in the list
b = list()
print(b)
output:[]
print(len(b))
output:0 
 # Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])
output:[3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : ])
output:[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']


print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])
output:['hyd',10.8,none,True,'hyd',3+4j,10.8,25]
print(list[ : : 2])
output:[25,3+4j,True,10.8]
print(list[1 : : 2])
output:10.8,'hyd,none,'hyd]
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])

output:[10.8,true,3+4j,25]

print(list[1 : 4])
output:[10.8,3+4j,'hyd']

print(list[-4 : -1])
output:[True, None, 10.8]

print(list[3 : -3])
output:['Hyd', True]
print(list[2 : -5])
output:[(3+4j)]
print(list[-1:-5])
output:[]






 #  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)
output:x: Hyd
print('y : ' , y)
output:x: True
for  x  in  list[2:7]:

	print(x)

output: (3+4j)
        Hyd
        True
        None
        10.8

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))

output:[10, 20, 30, 40, 50] address of object list


a[1 : 4] = [60 , 70] 
print(a , id(a))
output:[10, 60, 70, 50] address of on object a
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))

output:[10, 20, 100, 200, 300, 50]
  Find  outputs  (Home  work)
a =  [25]
print(a[1]) error due to no element in the 1st position 
print(a[1:])
output:[] dut to empty element present from first postion in the list












tuple()  function
---------------
 # Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))
output:class int 

print(type(b))
output:class tuple
print(type(c))
output:class int


print(type(d))

output:class tuple
 
print(a * 4)
output:100 

print(b * 4)
output:(25,25,25,25)
print(c * 4)
output:100 

print(d * 4)
output:(25,25,25,25)

 # tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
 print(a)
output:('h','y','d')
print(type(a))
output:class tuple
print(len(a))
output:3 
b = [10 , 20 , 15 , 18]
print(tuple(b))
output:(10,20,15,18)
print(tuple(range(5)))
output:(0,1,2,3,4)
print(tuple(25))
output:erorr
'''
 # Find  outputs (Home  work)

a = ()
print(type(a))
output:class tuple
print(a)
output: ()


print(len(a))

output:0
b = tuple()
print(b)
output:()
print(len(b))
output:0











 # Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)
output:(10,20,30) 
print(id(a)) 
output:address of an object a
a = a * 2
print(a)
output:(10,20,30,10,20,30)

print(id(a))
output: address of an object tuple


  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)
output:{None, True, 25, 10.8, 'Hyd', (3+4j)}
print(type(a))
output:class set
print(len(a))
output:6  
print(a[2])
output: error due to no slicing 
print(a[1 : 4])
output: error
a[2] = 'Sec'
output: error  
print(a * 2)

output:error 
print(a * a)
output:error 



# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)
output:{False, 1, 'Hyd', ''}
print(len(a))
output:4
print(type(a))
output:class set
 #  set()  function demo  program
a = set('Rama rAo')
print(a)
output:{'m', 'a', 'R', 'A', 'o', 'r', ' '}
print(len(a))
output:7
print(set([10 , 20 , 15 , 20]))
outout:{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))
output:{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))
output:{16, 10, 19, 13}
print(set(25))
output:error 
print(set([25 , 10.8 , [] , 'Hyd']))
output:error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  ---> Returns  an  empty  set
'''
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))
output:class list

print(type(b))
output:
class tuple

print(type(c))
output: class set

print(type(d))

 output: class set
print(a)
output:[]
print(b)
output:()

print(c)
output:{}
print(d)

output:{}




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

output:{25,10.8,'Hyd',True,None,1}
print(len(a))
output:6
a . remove(25)

print(a)

output:{10.8,'Hyd',True,None,1}
a . append(100)
output: error
a . add(set())
output:error
a . add(())
output:()
a . add([])
output:error

print(a)
output:{()}

a . add({})

output:error


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}

print('set  with  print  function')

print(a)
print(How  to  print  set)
print(*a)

print('Iterate  thru  set  with  for  loop')

for i in a
print(i)

How  to  iterate  thru  set  with  for  loop


output:error sets doesn't have indexing so error occours
