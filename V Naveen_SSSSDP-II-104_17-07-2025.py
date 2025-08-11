#1. Find  outputs    (Home  work)

a = range(10 , 50 , 5) #Ref 'a' points to range object range(10 ,50 ,5)
print(type(a)) #prints type of range object i.e. <class 'range'>
print(a) #prints range object itself as range(10 ,50 ,5)
print(*a) #prints elements of range object i.e. 10 15 20 25 30 35 40 45
print(id(a)) #prints address of range object 
print(len(a)) # print number elements are in range object i.e. 8
print(*a[2 : 7] , sep = ' , ') #prints   
elements of range object from 2 to 6 in steps of 1 with comma seperation i.e. 20 ,25 ,30 ,35 ,40
print(*a[ : : -1]) #prints all the elements of range object i.e. 45 40 35 30 25 20 15 10
a[4] = 32 #Error due to no modification permitted in range object because range is immutable object 
print(a * 2) #Error because there is no repetition to range object due to no duplicate elements will be permitted


#2.  Find  outputs  (Home  work)

a = range(10 , 20) #Ref 'a' points to range object range(10 ,20)
print(*a , sep = ',') #prints all range elements with comma seperation in steps of 1 i.e. 10 , 11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19
b = range(5) #Ref 'b' points to range object range(5)
print(*b) # prints all range elements in steps of 1 from 0 to 4 i.e. 0 1 2 3 4 
c = range(10 , 1 , -1) #Ref 'c' points to range object range(10,1,-1)
print(*c , sep = '...') # prints all range elements from 10 to 2 in steps of with three dot seperation i.e. 10...9...8...7...6...5...4...3...2
d = range(-10 , 0) #Ref 'd' points to range object range(-10 , 0 ,1)
print(*d) # Prints all range elements form -10 to -1 in steps of 1 i.e. -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)# Ref 'e' points to range object range(-10)
print(*e) # empty range 
f = range(2 , 2)#Ref 'f' points to range object range(2 ,2)
print(*f) # prints empty range
g = range(10 , 11 , 0.1) #Error due to range can hold only integer numbers not float and string
h = range('A' , 'F') # Ref 'h' points to range object range('A' ,'F')
Print(*h)#Error due to range can hold only integer numbers not float and string


#3.  Find  outputs  (Home  work)

r = range(10 ,  17 , 3) #Ref 'r' points to range object range(10 ,17, 3)
a , b , c = r # Assigned elements of 'r' to a ,b ,c or we can say unpacking elements with three objects
print(a , b , c) #prints elements of range object 'r' with Assigned object i.e. 10 13 16
r = range(3)# Ref 'r' points to range object range(0 ,3,1)
x , y = r #Error due unpacking with 2 object but in range object there are 3 elements i.e. 0 1 2
p , q  , r , s = r # error due to not enough valuea to unpack 
a , b , c = *r # Error due invalid starred usage 

(Note: * represent unpacking)





