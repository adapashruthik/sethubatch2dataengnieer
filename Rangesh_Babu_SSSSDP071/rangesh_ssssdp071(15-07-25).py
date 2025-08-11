# Float object HOMEWORK 
a = 10.8   
print(a)         
# Value of object 'a' is 10.8   
print(type(a))   # Type of object 'a' is <class 'float'>   
print(id(a))     
# Address of object 'a'   
b = 25.   
print(b)         
# Value of object 'b' is 25.0   
print(type(b))   # Type of object 'b' is <class 'float'>   
c = .689   
print(c)         
d = 3.4E2        
print(d)         
# Value of object 'c' is 0.689   
# [Mantissa Exponent Number]   
# Value of object 'd' is 3.4 × 10^2 = 340.0   
print(type(d))   # Type of object 'd' is <class 'float'>   
e = 9.62e-2      
print(e)         
print(9.8.2)     
# [Mantissa Exponent Number]   
# Value of object 'e' is 9.62 × 10^-2 = 0.0962   
#  Invalid syntax: multiple decimal points not allowed   
# Complex object demo program HOMEWORK 
a = 3 + 4j   
print(a)           
print(type(a))     
print(id(a))       
print(a.real)      
print(a.imag)      
# Value of object 'a' is (3+4j)   
# Type of object 'a' is <class 'complex'>   
# Address of object 'a'   
# Real part of 'a' is 3.0   
# Imaginary part of 'a' is 4.0   
print(type(a.real))# Type of real part is <class 'float'>   
print(type(a.imag))# Type of imag part is <class 'float'>  
# Find outputs HOMEWORK (Complex) 
a = 6j   
print(a)           
print(type(a))     
print(a.real)      
print(a.imag)      
print(5 + j6)      
print(3 + 4i)      
print(4 + j)       
print(4 + 1j)      
print(4 + 0j)      
# Value is 6j   
# Type is <class 'complex'>   
# Real part is 0.0   
# Imaginary part is 6.0   
# Invalid syntax: 'j6' is not valid   
# Invalid syntax: use 'j' not 'i'   
# Invalid syntax: 'j' must follow a number   
# Value is (4+1j)   
# Value is (4+0j)   
# Bool object demo program HOMEWORK 
a = True   
print(a)           
print(type(a))     
print(id(a))       
b = False   
print(b)           
# Value is True   
# Type is <class 'bool'>   
# Address of object 'a'   
# Value is False   
print(type(b))     # Type is <class 'bool'>   
print(True + True)         
print(True + False)        
print(False + True)        
print(False + False)       
# Output is 2 (1+1) 
# Output is 1 (1+0) 
# Output is 1 (0+1) 
# Output is 0 (0+0) 
print(True + True + True)  # Output is 3 (1+1+1) 
print(25 + 10.8 + True)    # Output is 36.8(35.8+1) 
print(True > False)        
# Output is True(1>0) 
print(True)                
print(False)               
print(true)                
print(false)               
# Output is True because keyword 
# Output is False because keyword 
#  NameError: name 'true' is not defined it should be T   
#  NameError: name 'false' is not defined  it should be F 
# Find outputs HOMEWORK (Octal) 
a = 0O6247   
print(a)           
print(type(a))     
print(id(a))       
b = 0o6247   
print(id(b))       
print(b)           
c = 3239   
print(c)           
print(id(c))       
# Value is 3255   
# Type is <class 'int'>  i.e, Decimal Equivalent 
# Address of object 'a'   
# Address of object 'b' (same as 'a')   
# Value is 3255   
# Value is 3239   
# Address of object 'c'   
print(0o9248)      
#  Invalid digit '9' in octal (base 8)   
# Find outputs HOMEWORK (Hexadecimal) 
a = 0xA7B9   
print(a)           
print(type(a))     
b = 0xBEEF   
print(b)           
print(A7B9)        
print('A7B9')      
# Value is 42937   
# Type is <class 'int'>  i.e, Decimal Equivalent 
# Value is 48879   
#  NameError: A7B9 not defined   
# Output is string 'A7B9'   
print(0XBEER)      
print(0XHYD)       
#  Invalid hexadecimal: 'R' is not allowed   
#  Invalid hexadecimal: 'H', 'Y', 'D' not allowed   
print(0xA7G9B)     #  Invalid hexadecimal: 'G' is not allowed   
# Find outputs HOMEWORK (Decimal) 
a = 9248   
print(a)           
print(type(a))     
# Value is 9248   
# Type is <class 'int'>  