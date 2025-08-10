print(eval('25'))#25:evaluates str'25'to int 25
print(eval('10.8'))#10.8
print(eval('False'))#False
print(eval('3+4j'))#3+4j
#print(eval('Hyd'))#Name error
print(eval("  'HYd'  "))#Hyd: the inner quotes make 'Hyd' a string
print(eval('3+4*5'))#23
print(eval('[10,20,15,18]'))#[10,20,15,18]
print(eval('{10,20,15,18,20,12,18}'))#{18,20,10,12,15}
print(eval('(10,20,30)'))#(10,20,30)
print(eval("{10:'Hyd',10:'sec'}"))#{10:'sec'}
#print(eval(4+5))#error: eval() must be a string not an integer
print()
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#hyd: the inner quotes make 'hyd' a string.so eval() evaluates it to 'hyd'
hyd = 'Sec'# reference 'hyd' points to str object 'Sec'
print(eval('hyd'))#sec:eval() returns the value of the object 'hyd'
sec = '25'#reference 'sec' points to str object '25'
print(eval('sec'))#25
print(eval(sec))#25: eval() evaluates the string '25' to int 25
cyb = 10.8#reference 'cyb' points to float object 10.8
print(eval('cyb'))#10.8:eval() evaluates the string 'cyb' to float 10.8
#print(eval(cyb))#error:eval() expects a string not a float
print()
#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd <next line>None :prints the Hyd and then converts str 'none' to None type'None"
print()
#  Find  outputs  (Home  work)
print(bool('False'))# true: it is non empty string
print(eval('False'))# False: converts string to bool
print(bool(''))#False:empty string
print(eval('  ""  '))#empty string
#print(eval(''))#error:eval() expects a string not an empty string
print(eval('  " "   '))#<space>
#print(eval(' '))#error:eval() expects a string not a space
'''
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))#converts the string to appropriate object and input reads the string from the keyboard
print(type(x))#prints type of x
print(x)#prints value of x

print()
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')#reads input string from the keyboard
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))#reads string input and converts to apppropriate value
# print(len(b))#prints length of b
print(b)#print value of b
print()
'''
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')#   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')#25 10.8 Hyd
print(a , b , c , sep = '---')#25...10.8...Hyd
print(a , b , c , sep = '\n')#25<next line>10.8<next line>Hyd
print(a , b , c)#25 10.8 Hyd
#print(a , b , c , separator = ':')#error:seperator is invalid keyword argument for print()
print()
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25 10.8 Hyd___
print(a , b , c , sep = ',,,')#25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25:10.8:Hyd<3 spaces>
print(a , b , c)#25 10.8 Hyd
print()
# Find outputs  (Home  work)
print('Hyd')#Hyd
print()#blank line
print('Sec')#Sec
print()#blank line
print('Cyb')#Cyd
print()
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]#reference 'l' points to list object [10,20,30,40]
t = (10 , 20 , 30 , 40)#reference 't' points to tuple object (10,20,30,40)
s = {10 , 20 , 30 , 40}#reference 's' points to set object {10,20,30,40}
print(l , t , s)#[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}(set is unordered)
print()
#  Find  outputs (Home  work)
a = 25# reference 'a' points to int object 25
b = '%f'  %a# converts int 25 to float 25.000000
print(b)#25.000000
print(type(b))#<class 'str'>
x = 10.8# reference 'x' points to float object 10.8
y = '%d'  %x# converts float 10.8 to int 10
print(y)#10
print(type(y))#<class 'str'>
m = [10 , 20 , 15 , 18]# reference 'm' points to list object [10,20,15,18]
n = '%s'  %m# converts list [10,20,15,18] to string '[10, 20, 15, 18]'
print(n)#[10,20,15,18]
print(type(n))#<class 'str'>
print()
# Find  Outputs  (Home  work)
a = 10.9274#reference 'a' points to float object 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)#<6 spaces>10.9
print('%10.3f'  %a)#<4 spaces>10.927
print('%.2f'  %a)#10.93
print('%.6f'  %a)#10.927400
print('%f'  %a)#10.927400
print()
# Find  outputs (Home  work)
a = 'Hyd'# reference 'a' points to str object 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) #Hyd
print('%s' , a)#%s Hyd
#print('%s'  a)#error
#print('%s' , %a)#error
print(a)#hyd
print()
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]# reference 'a' points to list object [10,20,30,40]
print('%s'  %a)#[10,20,30,40]
print('%s' , a)#%s [10,20,30,40]
#print('%s'  a)#error
#print('%s' , %a)#error
#print('%l'  %a)#Error
print(a)#[10,20,30,40]
print()
#Find outputs  (Home  work)
a = 25# reference 'a' points to int object 25
b = 10.9274# reference 'b' points to float object 10.9274
c = 'Hyd'# reference 'c' points to str object 'Hyd'
print('%d    %f    %s'  %(a , b , c))#25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c))#25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))#25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c)#%d %g %s 25 10.9274 Hyd
#print('%d    %g      %s'   a , b , c)#error
#print('%d    %g    %s'  ,  %(a , b , c))#error
#print('%d    %g    %s'    %a%b%c)#error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)#25 10.927400 Hyd