#  Find  outputs (Home  work)
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
print()
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)
print()
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   
print('%-7s'  %a)  
print('%2s'  %a)   
print('%s'  %a) 
print('%s' , a)
#print('%s'  a)         # error due to comma between s and a (or) % is missing before object a
#print('%s' , %a)    # error due to comma
print(a)
print()
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
#print('%s'  a)
#print('%s' , %a)
#print('%l'  %a)
print(a)
print()
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
#print('%d    %g      %s'   a , b , c)
#print('%d    %g    %s'  ,  %(a , b , c))
#print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)
print()