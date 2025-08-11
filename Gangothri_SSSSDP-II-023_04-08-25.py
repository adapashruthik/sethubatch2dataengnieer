# Find  outputs  (Home  work)
for i in range(1 , 8):
	print(i)
	if i%3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
# End of loop
print('Outside loop')                                                                                                                                                              
'''Output:                                                                                                                                                                                    
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop'''

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # SyntaxError: 'continue' not properly in loop
	print('Sec')
	
# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')                                                                                                                                                                 
'''Output:                                                                                                                                                                    
1
Sec
Hello
2
Sec
Hello
3
Outside loop'''

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')                                                                                                                                                                
# Output: SyntaxError: 'break' outside loop

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')                                                                                                                                                                
'''output:1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop'''

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop') 
'''output:
1
Sec
Hello
2
Sec
Hello
3                                                                         
'''
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop') 
'''output: 
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else  suite
Outside  loop'''

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')
'''output:
1
Sec
Hello
2
Sec
Hello
3
Outside  loop'''

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')
'''output:
1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else  suite
Outside loop'''

# Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

list= input("Enter the elements into list").split()
n = input("Enter the element to find: ")
i=0
while(i<len(list)):
    if(list[i] == n):
      print(f"{n} is found at {i}")
      break
    i+=1
else:
    print("Not found")
user_input = input("Enter list elements separated by spaces: ")
elements = user_input.strip().split()
target = input("Enter the element to search for: ")
index = 0
count = 0
while index < len(elements):
    if elements[index] == target:
        print(f"{target} is found at index {index}")
        count += 1
    index += 1
print(f"{target} is found {count} times")
'''output:
Enter list elements separated by spaces: 20 26 17 19 30 55 19 25
Enter the element to search for: 19
19 is found at index 0
19 is found at index 6
19 is found 2 times'''

#  Walrus   operator (:=)  demo  program
print(a := 25)#25
print(a = 25)#error
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)#13
print(a)#6
print((a = 6) + 7)#error

# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
if  c = 0: # error
	print('Hyd')
else:
	print('Sec')
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)
Let  inputs  be  25 , 10.8 , True ,  ctrl + z
sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3
1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs
2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError
3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
'''
try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))  #  Read  each  input  until  user  strikes  ctrl + z
		sum += x #  Adds  each  input  to  sum
		ctr +=1 #  Counts  number  of  inputs
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError: #  Executed  when  1st  input  itself  is  ctrl+z
		print('Enter  at  least  one  input')
except  (NameError , TypeError):  #  Executed  when  input  is  a  string
	print('Input  can  not  be  string')
#  del  operator  demo program  (Home  work)
a = 25
print(a)#25
del   a
print(a)#error
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del a
print(b , c)#25 25
print(a)#error
del b
print(c)25
print(b)#error
del c
print(c)#error
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#25 10.8 Hyd
del   a , b , c
print(a)#error
print(b)#error
print(c)#error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
del  a[2]
print(a)#[10, 20, 18]
del  a
print(a)#error
print(a[0])#error
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #(10, 20, 15, 18)
print(a[0])  #10
del a[2]
del a
print(a)  #error
print(a[0]); # error