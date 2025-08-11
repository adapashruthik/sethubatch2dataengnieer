#Find outputs (HOMEWORK)
 a = [25, 10.8, 'Hyd', True, 3+4j, None, 'Hyd', 25]   
print(a)                 
# Prints the list as is  [25, 10.8, 'Hyd', True, 3+4j, None, 'Hyd', 25] 
print(*a)                
print(type(a))           
print(id(a))             
print(len(a))            
a[2] = 'Sec'   
print(a)                 
print(a[2:5])            
# Unpacks and prints all elements  25 10.8 Hyd True 3+4j None Hyd 25 
# <class 'list'>   
# address of list   
# Output is 8   
# [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25] 
# ['Sec', True, (3+4j)]   
#append() and remove() methods (HOMEWORK) 
a = []   
print(a)                 
a.append(25)   
a.append(10.8)   
a.append('Hyd')   
a.append(True)   
print(a)                 
a.remove('Hyd')   
print(a)                 
a.remove('25')           
# Empty list []   
# [25, 10.8, 'Hyd', True]   
# 'Hyd' is removed → [25, 10.8, True] 
# '25' (as string) not found in list 
#Find outputs (HOMEWORK) 
a = [25, 10.8, 'Hyd']   
print(a)                 
# [25, 10.8, 'Hyd']   
print(id(a))             
print(a * 3)             
print(a * 2)             
print(a * 1)             
print(a * 0)             
print(a * -1)            
print(a * 4.0)           
a = a * 3   
print(a)                 
# Address of object a  
# [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']   
# [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']  
# [25, 10.8, 'Hyd']   
# []   
# []   
# can't multiply list by float   
# [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd'] 
# Addrees New id → new object   
print(id(a))             
a = [25]   
print(a * a)             
# can't multiply list by list   
#list() function demo (HOMEWORK) 
a = list('Hyd')   
print(a)                 
print(type(a))           
print(len(a))            
# ['H', 'y', 'd']   
# <class 'list'>   
# 3   
b = (10, 20, 15, 18)   
print(list(b))           
# [10, 20, 15, 18]   
print(list(range(5)))    # [0, 1, 2, 3, 4]   
print(list(25))          
# 'int' object is not iterable   
#Find outputs (HOMEWORK) 
a = []   
print(type(a))           
print(a)                 
print(len(a))            
b = list()   
print(b)                 
print(len(b))            
# <class 'list'>   
# []   
# 0   
# []   
# 0   
#Slice demo program (HOMEWORK) 
list = [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd']   
# Indexes: 0 1 2 3 4 5 6 7 
print(list[2:7])         
# [(3+4j), 'Hyd', True, None, 10.8]   
print(list[::])          
print(list[:])           
print(list[::-1])        
print(list[::2])         
print(list[1::2])        
print(list[::-2])        
print(list[-2::-2])      
print(list[1:4])         
print(list[-4:-1])       
print(list[3:-3])        
print(list[2:-5])        
# [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd'] 
# [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd'] 
# Reversed list   
# [25, 3+4j, True, 10.8]   
# [10.8, 'Hyd', None, 'Hyd']   
# ['Hyd', None, 'Hyd', 10.8]   
# [10.8, True, 3+4j, 10.8]   
# [10.8, 3+4j, 'Hyd']   
# [True, None, 10.8]   
# ['Hyd', True]   
# [(3+4j)]   
print(list[-1:-5])       # []    
 
#Find outputs (HOMEWORK) 
list = [25, 10.8, 3+4j, 'Hyd', True, None, 10.8, 'Hyd']   
x, y = list[3:5]   
print('x : ', x)         # x : Hyd   
print('y : ', y)         # y : True   
for x in list[2:7]:   
    print(x)             # 3+4j 
                                  'Hyd' 
                                   True 
                                    None 
                                    10.8 
 
#Find outputs (HOMEWORK) 
a = [10, 20, 30, 40, 50]   
print(a, id(a))          # [10, 20, 30, 40, 50] address of a 
 
a[1:4] = [60, 70]   
print(a, id(a))          # [10, 60, 70, 50] Same address of a 
 
a[2:4] = [100, 200, 300]   
print(a, id(a))          # [10, 60, 100, 200, 300] Same id 
 
#Find outputs (HOMEWORK) 
a = [25]   
print(a[1])              # list index out of range   
print(a[1:])             # []   
 
#Find outputs (HOMEWORK) 
a = (25)                 # Treated as int → no comma   
b = 25,                  # Tuple → trailing comma   
c = 25                   # Int   
d = (25,)                # Tuple → one element   
print(type(a))           # <class 'int'>   
print(type(b))           # <class 'tuple'>   
print(type(c))           # <class 'int'>   
print(type(d))           # <class 'tuple'>   
print(a * 4)             
print(b * 4)             
print(c * 4)             
print(d * 4)             
# 100   
# (25, 25, 25, 25)   
# 100   
# (25, 25, 25, 25)   
#tuple() function demo (HOMEWORK) 
a = tuple('Hyd')   
print(a)                 
print(type(a))           
print(len(a))            
# ('H', 'y', 'd')   
# <class 'tuple'>   
# 3   
b = [10, 20, 15, 18]   
print(tuple(b))          
# (10, 20, 15, 18)   
print(tuple(range(5)))   # (0, 1, 2, 3, 4)   
print(tuple(25))         
# 'int' object is not iterable   
#Find outputs (HOMEWORK) 
a = ()   
print(type(a))           
print(a)                 
print(len(a))            
b = tuple()   
print(b)                 
print(len(b))            
# <class 'tuple'>   
# ()   
# 0   
# ()   
# 0   
#Tricky program - Find outputs (HOMEWORK) 
a = (10, 20, 30)   
print(a)                 
print(id(a))             
a = a * 2   
print(a)                 
print(id(a))             
# (10, 20, 30)   
# address of object a 
# (10, 20, 30, 10, 20, 30)   
# address of a(New id) 
#set object demo program (HOMEWORK) 
a = {25, 10.8, 'Hyd', True, 3+4j, None, 25, 'Hyd'}   
print(a)                 
# {True, 3+4j, 10.8, 'Hyd', 25, None}  → Duplicates removed 
print(type(a))           
print(len(a))            
print(a[2])              
print(a[1:4])            
a[2] = 'Sec'             
print(a * 2)             
print(a * a)             
# <class 'set'>   
# Output is 6   
# 'set' object is not indexed   
# 'set' object is not indexed  
# 'set' object does not support item assignment   
# can't multiply set   
# unsupported operand type(s)   
#Tricky program – Find outputs (HOMEWORK) 
a = {1, 'Hyd', False, True, 0.0, '', 1.0, 0}   
print(a)                 
# {'Hyd', 1, False, ''} 
print(len(a))            
print(type(a))           
# Output is 4   
# <class 'set'>   
#set() function demo program (HOMEWORK) 
a = set('Rama rAo')   
print(a)                 
# Unique characters → {'a', ' ', 'R', 'A', 'm', 'o', 'r'} 
print(len(a))            
# 7  
print(set([10, 20, 15, 20]))        
# {10, 20, 15}   
print(set((25, 10.8, 'Hyd', 10.8))) #  {25, 10.8, 'Hyd'}   
print(set(range(10, 20, 3)))        
#  {10, 13, 16, 19}   
print(set(25))                     
# 'int' object is not iterable   
print(set([25, 10.8, [], 'Hyd']))  # In set list is not allowed 
#Find outputs (HOMEWORK) 
a = []   
b = ()   
c = {}   
d = set()   
print(type(a))           
print(type(b))           
print(type(c))           
# <class 'list'>   
# <class 'tuple'>   
# <class 'dict'>   
print(type(d))           
print(a)                 
print(b)                 
print(c)                 
print(d)                 
# <class 'set'>   
# []   
# ()   
# {}   
# set()   
#Tricky program – add() and remove() methods (HOMEWORK) 
a = set()   
a.add(25)   
a.add(10.8)   
a.add('Hyd')   
a.add(True)   
a.add(None)   
a.add('Hyd')      
a.add(1)          
print(a)          
print(len(a))     
a.remove(25)      
# Duplicate → Ignored   
# 1 == True → Treated as same   
# {None, True, 10.8, 25, 'Hyd'} 
# 5 
# Removes 25   
print(a)   #{None, True, 10.8,'Hyd'} 
a.append(100)     # append() used for list and add() is used for set  
a.add(set())      
a.add(())          
a.add([])         
print(a)          
a.add({})         
# nested sets are not allowed 
# list is not added to the set 
# {None, True, 10.8, 'Hyd', ()} 
# nested sets are not allowed 
#How to print set in two different ways (HOMEWORK) 
a = {25, True, 'Hyd', 10.8}   
1.print('set with print function')   
print(a)                        
2.print('Iterate thru set with for loop')   
for x in a:                     
print(x)   