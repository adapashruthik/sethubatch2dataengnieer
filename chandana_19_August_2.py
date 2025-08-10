
'''# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue  #  moves the control to next iteration of the loop
	else:
			print('Sec')	
	print('Hello')
# End of loop
print('Outside loop')  

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue  #  error:continue statements only be used in for and while
	print('Sec')

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break  #  as 3%3==0 moves the control out of the loop 
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')   

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break  # error: break statements are only be used in for and while loop
	print('Sec')

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass  #  it is am empty statement
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()  #  stops the program execution
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue  # moves the control to next iteration of the loop
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break  #  as 3%3==0 control moves out of the loop
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')
'''
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break  #  never executes because i is never equal to 8
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')
'''
#program to search for an element in the list without using in operator and print Found or not found message
x=eval(input('Enter any list: '))
y=eval(input('Enter the element to be searched : '))
for i in range(0,len(x),1):
    if x[i]==y:
        print('Found at index ',i)
        break
else:
    print('Not Found')

print()
#program to search for an element in the list and print index of each element and also no,of times it is found
x=eval(input('enter any list :'))
y=eval(input('Enter the element to be searched : '))
sum=0
for i in range(0,len(x),1):
	if x[i]==y:
		sum+=1
		print(F'{y} is found at index ',i)
print(F'{y} is found {sum} times')

#  Walrus   operator (:=)  demo  program
print(a := 25)  #  assigns 25 to ref 'a'
#print(a = 25)  #  error
print(a)  #  25
print(a := 6 + 7)  #  13
print(a)  #  13
print((a := 6) + 7)  #  13
print(a)  #  6
#print((a = 6) + 7)
	
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')  #  Hyd: as a==0
else:
	print('Sec')
if  b := 0:  #  cannot assign values in condition so it is false
	print('Hyd')
else:
	print('Sec : ' , b)  #  sec : 0
#if  c = 0:  #  cannot assign values in condition
#	print('Hyd')
#else:
#	print('Sec')


# Program to determine average of inputs terminated with ctrl+z (without walrus operator)
sum = 0
ctr = 0
while True:
    try:
        x = eval(input("Enter input (ctrl+z to stop) : "))
        sum += x
        ctr += 1
    except EOFError:
        break
if ctr > 0:
    print("Average :", sum / ctr)
else:
    print("No inputs")


#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a  #  deletes reference a by default
#print(a)  #  error: there is no ref 'a'

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  #  25 25 25
del   a # delete ref 'a'
print(b , c)  #  25 25
#print(a)  #  error: there is no ref a 
del   b  #  deletes ref 'b'
print(c)  #  25
#print(b)  # error
del   c   #  deletes ref 'c' and pvm deletes object '25'
#print(c)  #  error: no ref 'c'

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)  #  25 10.8 Hyd
del   a , b , c   # deletes ref a,b,c
print(a)  # error
print(b)  # error
print(c)  # error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  #  [10, 20, 15, 18]
del  a[2]  #  deletes 15
print(a)   #  [10, 20, 18]
del  a   # deletes ref a 
#print(a)  # error
#print(a[0])  #  error

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #  (10, 20, 15, 18)
print(a[0])  #  10
#del  a[2]  #  tuple doesn't support item deletion
del  a  #  deletes ref 'a'
#print(a)  #  error
print(a[0])  # error
'''
