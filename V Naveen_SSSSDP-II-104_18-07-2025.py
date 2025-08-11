#1. append()  and  remove()  methods  (Home  work)

a = [ ] # Ref 'a' points to empty list
print(a) #returns empty list
a . append(25) # inserts  25 to list object 'a' 
a . append(10.8) # inserts  10.8 at the end list
a . append('Hyd') # inserts  'Hyd' at the end list 
a . append(True) # inserts  true at the end of list
print(a)# prints list object 'a' i.e. [25 ,10.8 ,'Hyd' ,True]
a . remove('Hyd') #removes 'Hyd' from the list
print(a) # prints list object 'a' i.e. [25 ,10.8 ,True]
a . remove('25') #Error because there is no string '25' in the list
print(a)# prints list object 'a' i.e. [25 ,10.8 ,True]



#2.  Find  outputs  (Home  Work)

a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # prints object list i.e. [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) #prints all the elements of list 'a' i.e. 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) # Type of list object i.e. <class 'list'>
print(id(a)) # address of the list object 
print(len(a)) #returns number of elements in the list 'a' i.e 8
a[2] = 'Sec' # 2nd index of list 'a' will be modified i.e. from 'Hyd' to 'Sec'
print(a)# prints object list i.e. [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) #prints all the elements of list 'a' i.e. 25 10.8 Sec True 3+4j None Hyd 25
print(a[2 : 5]) # print list from the indexes 2 to 4 in steps of 1 and created a new list i.e ['Sec' ,True ,(3+4j)]



#3. list()  function  demo  program
a = list('Hyd')#converts string to list
print(a) # Prints the object list 'a' i.e. ['H' ,' y' ,'d']
print(type(a))# Type of list object i.e. <class 'list'>
print(len(a))#returns number of elements in the list i.e. 3
b = (10 , 20 , 15 , 18)#ref 'b' points to tuple
print(list(b))#converts tuple to list and returns list object i.e [10 ,20 ,15 ,18]
print(list(range(5))) #converts range to list and returns list object i.e [0 ,1 ,2 ,3 ,4]
print(list(25)) #error because non sequence object will be not converted to list



#4.  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # Prints the object list itself i.e. [25 , 10.8 , 'Hyd']
print(id(a)) #address of the list object 
print(a * 3)#prints list object three times i.e. [25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd']
print(a * 2)#prints list object two times i.e. [25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd']
print(a * 1)#prints list object one time i.e. [25 , 10.8 , 'Hyd']
print(a * 0)#Print empty list
print(a * -1) #Prints empty list
print(a * 4.0)#error due to multiplying with non int object ,it should be int object 
a = a * 3 # repeating list object 'a' into three times
print(a)#prints list object itself i.e. [25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd' ,25 , 10.8 , 'Hyd']
print(id(a)) #address of list object 
a = [25]#Ref 'a' points to list object 
print(a * a)#error due to multiplying with non int object



#5. Slice  demo  program (Home  work)

#        0      1     2        3      4       5      6      7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8   -7       -6      -5      -4     -3     -2     -1
print(list[2 : 7]) #  list[2 :  7 :  1]  --->  List  from  indexes  2 to  6 in  steps  of  1  i.e.  [3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])#  list[0 : 8  :  1]  --->  List  from  indexes  0  to  7 in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #  list[0 :  8 :  1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])#  list[-1 :  -9 :  -1]  --->  List  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  ['Hyd' ,10.8 ,None ,True ,'Hyd' ,3+4j , 10.8 ,25]
print(list[ : : 2])#  list[0 :  8 :  2]  --->  List  from  indexes  0  to  7  in  steps  of  2  i.e.  [25  , 3 + 4j  , True , 10.8]
print(list[1 : : 2])#  list[1 :  8 :  2]  --->  List  from  indexes  1  to  7  in  steps  of  2  i.e.  [10.8 , 'Hyd' ,  None , 'Hyd']
print(list[ : : -2]) #  list[-1 :  -9 : -2]  --->  List  from  indexes   -1  to  -8  in  steps  of   -2   i.e.  ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])#  list[-2 :  -9:  -2]  --->  List  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  [10.8 ,True ,3+4j ,25]
print(list[1 : 4])#  list[0
1 :  8
4 :  1]  --->  List  from  indexes  1  to  3  in  steps  of  1  i.e.  [ 10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])#  list[-4 :  -1 :  1]  --->  List  from  indexes  -4  to  -2  in  steps  of  1  i.e.  [True, None  ,10.8]
print(list[3 : -3])#  list[3 :  -3 :  1]  --->  List  from  indexes  3  to  -4  in  steps  of  1  i.e.  [ 'Hyd' , True ]
print(list[2 : -5])#  list[2 :  -5 :  1]  --->  List  from  indexes  2  to  -6  in  steps  of  1  i.e.  [3 + 4j]
print(list[-1:-5])#  list[-1 :  -5 :  1]  --->  List  from  indexes  -1  to  -6  in  steps  of  1  i.e. Empty list[]



#6. Find  outputs
a = [ ]# ref 'a' points to Empty list
print(type(a)) #type of list object i.e. <class 'list'>
print(a)#prints empty list
print(len(a)) # number of elements in list i.e. 0
b = list() # ref 'b' points to list object 
print(b) # prints empty list 
print(len(b)) #number of elements in list i.e. 0


#7.  Find  outputs  (Home  work)
#     0   1     2    3    4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#prints the object list itself and address of list object i.e. [10 , 20 , 30 , 40 , 50] <space> address 
a[1 : 4] = [60 , 70]#updates indexes 1 to 3 with 60 ,70 remaining will be same ,because of excess index ,no elements to be updated ,40 in list 'a' will be removed i.e. [10 ,60 ,70 ,50]
print(a , id(a))#prints the object list itself and address of list object i.e. [10 , 60 , 70  , 50] <space> same address
a[2: 4] = [100 , 200 ,  300]#updates indexes 2 to 3 with 100 ,200 , 300 remaining will be same i.e. [10 ,60 ,10 ,200 ,300]
print(a , id(a))#prints the object list itself and address of list object i.e. [10 , 60 , 100  , 200 ,300] <space> same address



#8.  Find  outputs  (Home  work)
#       0      1      2      3       4       5     6       7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] # unpacking list with x and y respected to indexes 3 to 4
print('x : ' , x) # prints x: Hyd
print('y : ' , y) # prints y: True
for  x  in  list[2:7]:
	print(x) # print all the elements from indexex 2 to 6 i.e. (3+4j)<nextline> 'Hyd' <nextline> True <nextline> None<nextline> 10.8



#9. Find  outputs  (Home  work)
a = (25)#Ref 'a' points to int object, it is int object not tuple because tuple object must have  a comma after each element
b = 25, #ref 'b' points to tuple object 
c = 25 #ref 'c' points to int object 
d = (25,)#ref 'd' points to tuple object
print(type(a))# Type of int object i.e. <class 'int'>
print(type(b)) #Type of tuple object i.e. <class 'tuple'>
print(type(c))#Type of int object i.e. <class 'int'>
print(type(d))#Type of tuple object i.e. <class 'tuple'>
print(a * 4) #Prints int object 'a' with multiplied by 4 i.e. 100
print(b * 4)#prints tuple object four times i.e. (25 ,25 ,25 ,25)
print(c * 4)#Prints int object 'a' with multiplied by 4 i.e. 100
print(d * 4)#prints tuple object four times i.e. (25 ,25 ,25 ,25)



#10.  Find  outputs  (Home  work)
a =  [25]#ref 'a' points to list object [25]
print(a[1]) #Error due to index out of range
print(a[1: ])#Error due to index out of range




#11. Find  outputs (Home  work)
a = ()# ref 'a' points empty tuple
print(type(a)) #Type of tuple object i.e. <class 'tuple'>
print(a) # prints empty tuple
print(len(a)) #prints number of elements of tuple i.e. 0
b = tuple()# ref 'b' points to tuple object tuple()
print(b) #prints empty tuple 
print(len(b)) #prints number of elements in tuple i.e. 0


#12. tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') #ref 'a' points to tuple object,which is converted from string to tuple ('Hyd') ----> ('H' ,'y' ,'d')
print(a)# prints tuple object itself i.e. ('H' ,'y' ,'d')
print(type(a)) #prints type of tuple object i.e. <class 'tuple'>
print(len(a)) #prints number of elements of tuple i.e. 3
b = [10 , 20 , 15 , 18] #ref 'b' points to list object 
print(tuple(b))#converts list to tuple and returns tuple objects i.e. (10 ,20, 15 ,18)
print(tuple(range(5)))# converts range to tuple and returns tuple objects i.e. (0 ,1 ,2 ,3 ,4)
print(tuple(25))#error due to not sequence objects will be not converted to sequence



#13.  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'} 
print(a)#prints set object itself in unordered manner and  removed duplicate elements i.e {25 ,True ,None ,'Hyd' ,10.8 ,(3+4j)}(may be )
print(type(a))# type of set object i.e. <class 'set'>
print(len(a)) #number of elements in set i.e. 6
print(a[2]) #error due to set doesn't support indexes because it is unordered object
print(a[1 : 4])#error due to set does not support slicing because set is unordered object
a[2] = 'Sec' #Errror due to set doesn't support modification 
print(a * 2)#Error due to set doesn't support repetition 
print(a * a) #errro due to set doesn't support repetition



#14. Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)#ref 'a' points to tuple objects (10 , 20 , 30)
print(a) #prints tuple object itself i.e. (10 , 20 , 30)
print(id(a)) #address of the tuple object 
a = a * 2 #prints tuple object two times i.e.(10 , 20 , 30 ,10 ,20 ,30)
print(id(a))#address of the tuple object



#15.  set()  function demo  program
a = set('Rama rAo') # converts string to set
print(a) #prints set object itself i.e. it will print in any order when each time we print { 'r' ,'R' ,'a' ,'m' , 'a' ,'A' , 'o' ,' '}
print(len(a)) # number of elements in set i.e. 8
print(set([10 , 20 , 15 , 20])) # converts list to set and may returns {10 ,20 ,15} ,and duplicate elements will be removed 
print(set((25 , 10.8 , 'Hyd' , 10.8))) # converts tuple to set and may returns as {25 ,'Hyd' ,10.8}
print(set(range(10 , 20 , 3))) #converts range to set from indexes 10 to 19 in steps of 3 and returns  {10 ,13 ,16 ,19}
print(set(25))#error due to non sequence objects can not be converted into sequence 
print(set([25 , 10.8 , [] , 'Hyd'])) # error due to list in list which is not converted to set


#16. Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #returns the object set 'a' i.e. {1 ,'Hyd' , False ,''}
print(len(a)) #number of elements in set i.e. 4
print(type(a)) #type of set object i.e. <class 'set'>



#17. Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() #Ref 'a' points to empty set
a . add(25) # inserts 25 anywhere in the set
a . add(10.8) # inserts 10.8 anywhere in the set
a . add('Hyd') # inserts 'Hyd' anywhere in the set 
a . add(True)# inserts True anywhere in the set 
a . add(None) #inserts None anywhere in the set 
a . add('Hyd') inserts 'Hyd' anywhere in the set 
a . add(1) # inserts 1 anywhere in the set 
print(a)#prints the set object i.e. { 25 ,10.8 ,None ,'Hyd' ,True}
print(len(a)) #number of elements in set i.e. 5
a . remove(25) #removes 25 from the set
print(a) # prints set object i.e. {10.8 ,'Hyd' , True ,None}
a . append(100) #error because of using append insteed of add
a . add(set()) #error due to set in set not permitted 
a . add(())# tuple will be added to list 'a' 
a . add([]) #error due to list in set not permitted 
print(a) #prints set of object 'a' i.e. {10.8 ,None , True ,() ,'Hyd'}
a . add({})#error due to set in set not permitted



#18. Find  outputs  (Home  work)
a =   [ ] #ref 'a' points to empty list
b =   ( )#ref 'b' points to empty tuple 
c =   {}#ref 'c' points to empty dict
d =   set() #ref 'd' points to empty set
print(type(a))# type of list object i.e. <class 'list'>
print(type(b))# type of tuple object i.e. <class 'tuple'>
print(type(c))# type of dict object i.e. <class 'dict'>
print(type(d))# type of set object i.e. <class 'sett'>
print(a) #returns []
print(b)# returns ()
print(c)#returns {}
print(d)# returns set()



#19. How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)#using print function 
print('Iterate  thru  set  with  for  loop')
for x in a:
    print x #using for loop
