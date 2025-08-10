'''
#program to add, subtract, multiply,and divide two complex numbers
x=complex(input('enter 1st complex number :'))
y=complex(input('enter 2nd complex number :'))
print('sum: ',x+y)
print('Difference :',x-y)
print('Product :',x*y)
print('Division :',x/y)

print()

# Identify  error
else:
		print('else  suite')# no if statement
print('Outside')


#identify error
if 9>5 # : is mandatory after if 
	print('hello') 
print('Bye')

# Identify  error
if  9 > 12:
	print('Hyd')
else # : is mandatory after else
	print('Sec')
	
# Identify  error
if  (10,20,15): # indentation error
print('Hyd')
else:
print('Sec')

# Identify  error
if  (): # indentation error
			print('Hyd')
	else: 
					print('Sec')
print('Bye')

# Identify  error
if  { }: # suite should not be braces
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: # indentation error i
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: # indentation error 
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#program to determine a number is even or odd with if statement
x=int(input('enter a number :'))
if (x%2==0):
    print(F'{x} is even number')
else:
    print(F'{x} is odd number')
'''
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
'''
one
two
three
Bye: if condition is empty so it is false . so, else statement is executed

'''
print()
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
'''
Hyd
sec
cyb
Bye: if condition is non empty dictionary . so, stmts of if are executed'''
print()
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Bye : if condition is False: empty set 
print()
#program to print month name for input month number by using if and elif 
try:
    x=int(input('Enter a number(1-12) :'))
    if (x==1):
        print('January')
    elif(x==2):
        print('February')        
    elif(x==3):
        print('March')
    elif(x==4):
        print('April')
    elif(x==5):
        print('May')
    elif(x==6):
        print('June')
    elif(x==7):
        print('July')
    elif(x==8):
        print('August')
    elif(x==9):
        print('September')
    elif(x==10):
        print('October')
    elif(x==11):
        print('November')
    elif(x==12):
        print('December')
    else:
        print('Input should be between 1 and 12')
except:
     print('input should be integer')

#program to print digit in words with else and if(do not use elif)
x=int(input('Enter a number(0-9): '))
if(x==0):
    print('Zero')
else:
    if(x==2):
        print('one')
    else:
        if(x==2):
            print('two')
        else:
            if(x==3):
                print('three')
            else:
                if(x==4):
                    print('four')
                else:
                    if(x==5):
                        print('Five')                        
                    else:
                        if(x==6):
                            print('Six') 
                        else:
                            if(x==7):
                                print('Seven')
                            else:
                                if(x==8):
                                    print('eight') 
                                else:
                                    if(x==9):
                                        print('Nine')
                                    else:
                                        print('Invalid')                 




