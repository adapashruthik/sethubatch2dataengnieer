ADAPA SHRUTHIK
# eval()  function  demo  program
print(eval('25'))# string object 25 converted to integer object 25
print(eval('10.8'))# string object 10.8 converted to float object 10.8
print(eval('False')) #False
print(eval('3+4j')) #3+4j
print(eval('Hyd')) #Hyd
print(eval("    'Hyd'   ")) #Hyd   
print(eval('3 + 4 * 5')) #23
print(eval('[10 , 20 , 15 , 18]')) #[10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))#{10,20,15,18,12}
print(eval('(10 , 20 , 30)'))#(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) #{10 : 'Sec'}
print(eval(4 + 5)) # argument must be in string Error

 #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#hyd
hyd = 'Sec' 
print(eval('hyd'))#Sec
sec = '25' 
print(eval('sec')) #25
print(eval(sec)) #25 integer 
cyb = 10.8
print(eval('cyb')) #10.8
print(eval(cyb)) #argument must be in string Error

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) #Hyd  None


 #  Find  outputs  (Home  work)
print(bool('False')) #True
print(eval('False')) #False
print(bool('')) #False
print(eval('  ""  ')) #Empty string
print(eval('')) #argument must be written
print(eval('  " "   '))#space
print(eval(' ')) #Error

 # What  is  the  advantage  of  eval(input()) ? we can change string object to any appropriate object 
x = eval(input('Enter  any  input  :  ')) #imput from keyboard ex 5
print(type(x)) #<class 'int'>
print(x) #5

# What  is  a  better  approach  to  read  string  input ?  #input() method
a = input('Enter  any  string  :  ')# ex: hyd
print(len(a))#3
print(a) #hyd
b = eval(input('Enter   any  string  : '))# ex : 'hello'
print(len(b)) #5
print(b) #hello

 # sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #25   10.8    Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')#25<nextLine>10.8<nextLine>Hyd
print(a , b , c) #25 10.8 Hyd
print(a , b , c , separator = ':')#Error

 # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25 10.8 Hyd---
print(a , b , c , sep = ',,,')#25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd<tab-space><tab-space><tab-space>
print(a , b , c)#25 25 25

 # Find outputs  (Home  work)
print('Hyd') #Hyd
print() #nothing printed and move to nextLine
print('Sec') #Sec
print()#nothing printed and move to nextLine
print('Cyb')#Cyb

 # Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25 
b = '%f'  %a
print(b) #'25.0'
print(type(b)) #<class 'str'>
x = 10.8 
y = '%d'  %x
print(y) #10
print(type(y)) #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) [10 , 20 , 15 , 18]
print(type(n)) #<class 'str'>

 # Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #  <4 spaces   >10.9
print('%10.3f'  %a)#   <3 spaces>10.927
print('%.2f'  %a) #10.93
print('%.6f'  %a) #10.927400
print('%f'  %a)  #10.927400

 # Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)    # Hyd
print('%s' , a)    # '%s' Hyd
print('%s'  a)     #Error
print('%s' , %a)   #Error
print(a) #Hyd
 # Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #converts list to string [10 , 20 , 30 , 40]
print('%s' , a) #%s [10 , 20 , 30 , 40]
print('%s'  a) #Error
print('%s' , %a) #Error
print('%l'  %a) #Eror
print(a) #[10 , 20 , 30 , 40]
 
 #Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c))#25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c))#25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c) #%d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c) #Eror
print('%d    %g    %s'  ,  %(a , b , c))#Eror
print('%d    %g    %s'    %a%b%c) #Eror
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #25 10.927400 Hyd