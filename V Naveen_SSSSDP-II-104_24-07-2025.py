#1. eval()  function  demo  program

print(eval('25')) # 25
print(eval('10.8')) # 10.8 
print(eval('False')) # Flase
print(eval('3+4j')) # 3 + 4j
print(eval('Hyd')) # Hyd
print(eval("    'Hyd'   ")) # Hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)')) # (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5)) # Error due to arg should a string



#2.  Tricky  program

# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec' # Ref hyd points to string object 'sec'
print(eval('hyd')) # Sec
sec = '25' # Ref sec points to string object '25'
print(eval('sec')) # 25
print(eval(sec)) # Error due to arg should be a string
cyb = 10.8 # Ref cyd points to float object 10.8
print(eval('cyb')) # Error due to arg should be a string
print(eval(cyb)) # Error due to arg should be a string



#3.  Tricky  program

#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd



#4.  Find  outputs  (Home  work)

print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # Empty 
print(eval('')) # Error due to arg should be a string not empty
print(eval('  " "   ')) # <space>
print(eval(' ')) # <space>



#5. What  is  the  advantage  of  eval(input()) ?

x = eval(input('Enter  any  input  :  ')) # if user input is 25 then, eval(input(25)) --> eval('25') --> 25
print(type(x)) # <class 'int'>
print(x) # 25


#6. What  is  a  better  approach  to  read  string  input ?

a = input('Enter  any  string  :  ') # if user input is 25 then, --->input(25)
print(len(a)) # 2
print(a) # 25 --> which is a string '25'
b = eval(input('Enter   any  string  : ')) # if user input is 25 then, --> eval(input(25)) --> eval('25') --> 25
print(len(b)) # Error due non sequences does not have lengths
print(b) # 25 --> which is integer 25



#7. sep  argument  demo  program  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd' 
print(a , b , c , sep = ',') # 25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25<tab>10.8<tab>Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25<nextline>10.8<nextline>Hyd
print(a , b , c) # 25<space>10.8<space>Hyd
print(a , b , c , separator = ':') # Error due to there is keyword seperator in python , it should be sep



#8. Find  outputs  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25<space>10.8<space>Hyd---
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd(it will print after --- of above print function output)
print(a , b , c , sep = ':::' , end = '\t\t\t') # 10:::10.8:::Hyd<tab><tab><tab>
print(a , b , c) # 25<space>10.8<space>Hyd<space> (it will print after three tabs of above print function output)



#9. Find outputs  (Home  work)

print('Hyd') # Hyd
print() # Nothing will print
print('Sec') # Sec
print() # Nothing will print
print('Cyb') # Cyd



#10. Find  outputs  (Home  work)

l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10 , 20 , 30 , 40]<space>(10 , 20 , 30 , 40)<space>{10 , 20 , 30 , 40}



#11.  Find  outputs (Home  work)

a = 25 
b = '%f'  %a # Converts integer to string float
print(b) # 25.000000  ---> which is string float
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x # Converts float to string integer
print(y) # 10  ---> which is string integer
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18] 
n = '%s'  %m # Converts list to string list
print(n) # [10 , 20 , 15 , 18] ---> which is string list
print(type(n)) # <class 'str'>



#12. Find  Outputs  (Home  work)

a = 10.9274
print('%8.2f'  %a) # <3 spaces>10.93
print('%9.1f'  %a) # <5 spaces>10.9
print('%10.3f'  %a) # <4 spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # converts float to string float i.e. 10.927400



#13. Find  outputs (Home  work)

a = 'Hyd'
print('%7s'  %a) # <4 spaces>Hyd
print('%-7s'  %a) # Hyd<4 spaces>
print('%2s'  %a) # Hyd and ignores smaller width
print('%s'  %a) # Hyd
print('%s' , a) # %s<space>Hyd
print('%s'  a) # Error due to it should be a comma in between args or % should be with object a
print('%s' , %a) # Error due to comma
print(a) # Hyd



#14. Find  outputs  (Home  work)

a = [10 , 20 , 30 , 40]
print('%s'  %a) # Converts list to string list i.e. [10 , 20 , 30 , 40]
print('%s' , a) # %s [10 , 20 , 30 , 40]
print('%s'  a) # Error due to either comma should be there in betweet args or % with object a
print('%s' , %a) # Error due to comma
print('%l'  %a) # Error
print(a) # [10 , 20 , 30 , 40]



#15. Find outputs  (Home  work)

a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # Converts integer, float, and string to String integer, string float, and string i.e. 25<space>10.927400<space>Hyd
print('%i    %g    %s'    %(a , b , c)) # 25<space>10.9247<space>Hyd
print('%s    %s    %s'  %(a , b , c)) # 25<space>10.9247<space>Hyd
print('%d    %g    %s'  , a , b , c) # %d<space>%g<space>%s<space>25<space>10.9247<space>Hyd
print('%d    %g      %s'   a , b , c) # Error due to either comma or %
print('%d    %g    %s'  ,  %(a , b , c)) # Error due to comma
print('%d    %g    %s'    %a%b%c) # Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25<space>10.924700<space>Hyd
