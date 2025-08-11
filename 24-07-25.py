#first program
# eval()  function  demo  program
print(eval('25'))
print(eval('10.8'))
print(eval('False'))
print(eval('3+4j'))
print(eval('Hyd'))
print(eval("    'Hyd'   "))
print(eval('3 + 4 * 5'))
print(eval('[10 , 20 , 15 , 18]'))
print(eval('{10,20,15,18,20,12,18}'))
print(eval('(10 , 20 , 30)'))
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))
#print(eval(4 + 5))

#second program
print(eval("    'hyd'   "))
hyd = 'Sec'
print(eval('hyd'))
sec = '25'
print(eval('sec'))
print(eval(sec))
cyb = 10.8
print(eval('cyb'))
#print(eval(cyb))

#third program
print(eval('print("Hyd")'))

#fourth program
print(bool('False'))
print(eval('False'))
print(bool(''))
print(eval('  ""  '))
#print(eval(''))
print(eval('  " "   '))
#print(eval(' '))

#fifth program
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)

#sixth program
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)

#seventh program
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')
print(a , b , c , sep = '---')
print(a , b , c , sep = '\n')
print(a , b , c)
#print(a , b , c , separator = ':')

#eighth program
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a,b,c)
      
# ninth program
# Find outputs  (Home  work)
print('Hyd')
print()
print('Sec')
print()
print('Cyb')

#tenth program
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l,t,s)

#eleventh program
a = 25
b = '%f'  %a
print(b)
print(type(b))
x = 10.8
y = '%d'  %x
print(y)
print(type(y))
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)
print(type(n))

# twelfth program
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)

# thirteenth program
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) 
print('%s' , a)
#print('%s'  a)
#print('%s' , %a)
#print(a)

#fourteenth program
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
#print('%s'  a)
#print('%s' , %a)
#print('%l'  %a)
print(a)

# fifteenth program
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
#print('%d    %g      %s'   a , b , c)
#print('%d    %g    %s'  ,  %(a , b , c))
print('%d    %g    %s'    %a%b%c)
#print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)

