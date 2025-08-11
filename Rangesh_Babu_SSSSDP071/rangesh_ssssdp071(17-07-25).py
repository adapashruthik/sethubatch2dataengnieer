#Find outputs (HOMEWORK) 
a = range(10, 50, 5)   
print(type(a))         
# <class 'range'>   
print(a)               
print(*a)              
print(id(a))           
print(len(a))          
# range(10, 50, 5)   
# 10 15 20 25 30 35 40 45   
# Address of range object 'a'   
# Length is 8   
print(*a[2:7], sep=', ')  # 20, 25, 30, 35, 40   
print(*a[::-1])          
#45 40 35 30 25 20 15 10   
a[4] = 32               
print(a * 2)            
# TypeError: 'range' object does not support item assignment   
# can't multiply range object 
#Find outputs (HOMEWORK) 
a = range(10, 20)   
print(*a, sep=',')        
b = range(5)   
print(*b)                 
c = range(10, 1, -1)   
print(*c, sep='...')      
d = range(-10, 0)   
print(*d)                 
e = range(-10)   
print(*e)                 
f = range(2, 2)   
print(*f)                 
# 10,11,12,13,14,15,16,17,18,19   
# 0 1 2 3 4   
# 10...9...8...7...6...5...4...3...2 
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   
# Empty output (range from 0 to -10, no values)   
# Empty output   
g = range(10, 11, 0.1)    # 'float' object cannot be interpreted as an integer   
h = range('A', 'F')       
#string objects cannot be changed as integer 
#Find outputs (HOMEWORK) 
r = range(10, 17, 3)   
a, b, c = r   
print(a, b, c)            
r = range(3)              
x, y = r                
p, q, r, s = r        
a, b, c = *r         
# Output is 10 13 16   
# Values: 0, 1, 2   
# not enough values to unpack (expected 2, got 3)   
# too many values to unpack (expected 4, got 3)   
# can't use *r on LHS of assignment   