# Find outputs (Home work) 
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
print(a)                
print(type(a))          
print(a[10])            
print(a[20])            
print(a[15])            
print(a[18])            
print(a[19])            
print(a[0])             
# {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'} 
# <class 'dict'> 
# Ramesh 
# Kiran 
# Amar 
# Sita 
# KeyError: 19 
# KeyError: 0 
print(a['Amar'])        
a[15] = 'Krishna'       
a.pop(20)               
a[25] = 'Vamsi'         
print(a)                
# KeyError: 'Amar' 
# Modify key 15 to 'Krishna' 
# Remove 20 : 'Kiran' from dict 
# Append 25 : 'Vamsi' to dict 
# {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'} 
print(len(a))           
print(a * 2)            
# 4 
# TypeError: unsupported operand type(s) for *: 'dict' and 'int’ 
# Find outputs (Home work) 
a = {10 : 'Hyd' , 10 : 'Sec'} 
print(a)                
print(len(a))           
# {10: 'Sec'} 
# 1 
b = {'R': 'Red', 'G': 'Green', 'B': 'Blue', 'Y': 'Yellow', 'G': 'Gray', 'B': 'Black'} 
print(b)                
# {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'} 
print(len(b))           
# 4 
# Tricky program (Home work) 
a = {True: 'Yes', 1: 'No', 1.0: 'May be'} 
print(a)                
print(len(a))           
# Find outputs 
a = { [ ] : 25}         
b = { ( ) : 25}         
print(b)                
c = { { } : 25}         
# {True: 'May be'} 
# 1 
# TypeError: unhashable type: 'list' 
# Valid, prints: {( ): 25} 
# {( ): 25} 
# TypeError: unhashable type: 'dict' 
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} 
print(d)                
print(len(d))           
# {'Ramesh': [9948250500, 9848565090, 9440250404]} 
# 1 
e = {set() : 10.8}      # TypeError: unhashable type: 'set' 
# Find outputs 
a = {} 
print(type(a))          
print(len(a))           
print(a)                
b = dict() 
print(type(b))          
print(len(b))           
# <class 'dict'> 
# 0 
# {} 
# <class 'dict'> 
# 0 
print(b)                
# {} 