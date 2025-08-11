#1. Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #Prints {10 : 'Sec'} because keys should be not same ,so automatically hyd will be replaced with sec
print(len(a)) #number of elements in dictionary i.e. 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}  
print(b)#prints {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'} because of same keys will be not allowed in dictionary
print(len(b)) #number of elements in dictionary i.e.4


#2. Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}# Ref 'a' points to dictionary 
print(a)# prints dictionary with all elements i.e. {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#type of dictionary i.e. <class 'dict'>
print(a[10])#using a[10] we can obtain  value  key  10
print(a[20])# using a[20] we can obtain  value  key  20
print(a[15])#using a[15] we can obtain  value  key  15)
print(a[18]) #using a[18] we can obtain  value  key  18)
print(a[19])# throws error because there is no key with 19
print(a[0]) #throws error because there is no key with 0
print(a['Amar']) #erro due to we can print keys by using values ,it is not permitted 
a[15] = 'Krishna' #  to  moify  value  of   key  15  to  'Krishna'
del a[20] #  to  remove  20 :  'Kiran'  from  dict  'a'
a[25]='Vamsi' # to  append  25 : 'Vamsi'  to  dict  'a'
print(a)#prints {10 : 'Ramesh'  , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a))# number of elements in dictionary i.e. 4
print(a * 2)#error because of dictionary does not permitted duplicate elements



#3. Find  outputs
a = { [ ] : 25} # error because of key will be not sequence,it should be non sequence and only immutable object will be permitted 
b = { ( ) : 25}
print(b) # prints { ( ) : 25} because tuple is immutable 
c = { { } : 25}# error because of key will be not sequence,it should be non sequence and only immutable object will be permitted 
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #prints {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) # number of elements in dictionary i.e.1
e = {set() : 10.8} ## error because of key will be not sequence,it should be non sequence and only immutable object will be permitted



#4. Find  outputs
a = {} #ref 'a' points to empty dictionary 
print(type(a))#type of dictionary i.e. <class 'dict'>
print(len(a))#number of elements in dictionary i.e. 0
print(a)# prints empty dictionary 
b = dict() #ref 'b' points to empty dictionary 
print(type(b))#type of dictionary i.e. <class 'dict'>
print(len(b))#number of elements in dictionary i.e. 0
print(b) # prints empty dictionary



#5.  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#prints {True : 'May be'} because all the keys are same 
print(len(a))#number of elements in dictionary i.e. 1
