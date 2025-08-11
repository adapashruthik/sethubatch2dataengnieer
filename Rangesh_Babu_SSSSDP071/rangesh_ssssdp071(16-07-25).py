#Find outputs (HOMEWORK) 
a = "Rama Rao"   
print(a)           # Value of object 'a' is Rama Rao   
print(type(a))     # Type is <class 'str'>   
print(id(a))       # Address of object 'a'   
 
b = 'Hyd'   
print(b)           # Value of object 'b' is Hyd   
 
c = '''Hyd is green city.   
         Hyd is hitec city.   
         Hyd is beautiful city.'''   
print(c)           # Multiline string is printed as it is i.e; Hyd is green city.   
                                                                                            Hyd is hitec city.   
                                                                                            Hyd is beautiful city. 
 
#Index demo program (HOMEWORK) 
a = 'Hyd'   
print(a[0])        # 'H' is at index 0   
print(a[1])        # 'y' is at index 1   
print(a[2])        # 'd' is at index 2   
 
print(a[3])        #  IndexError: string index out of range   
 
print(a[2])        # 'd' from object 'a'   
print(a[1])        # 'y' from object 'a'   
print(a[0])        # 'H' from object 'a'   
 
print(a[-4])       # IndexError: string index out of range   
 
print(a[0] == a[-3])  # True because 'H' == 'H'   
 
a[2] = 'c'         # TypeError: 'str' object does not support item assignment   
 
print(25[0])       # TypeError: 'int' object is not subscriptable   
print('25'[0])     
# Output is '2'   
print(True[1])     # TypeError: 'bool' object is not subscriptable   
print('True'[1])   # Output is 'r'   
#Find outputs (HOMEWORK) 
a = 'Hyd'   
print(a * 3)       
print(a * 2)       
print(a * 1)       
print(a * 0)       
print(a * -1)      
print(25 * 3)      
# Output is HydHydHyd   
# Output is HydHyd   
# Output is Hyd   
# Output is empty string   
# Output is empty string   
# Output is 75   
print('25' * 3)    # Output is 252525   
print('25' * 4.0)  # TypeError: can't multiply sequence by non-int   
print(3 * 'Hyd')   # Output is HydHydHyd   
print('25' * True) # Output is '25'   
#Find outputs (HOMEWORK) 
a = 'Hyd'   
print(a, id(a))       
a = a * 3   
print(a, id(a))       
# Value is Hyd, address shown   
# Value is HydHydHyd, different address   
#len() function (HOMEWORK) 
print(len('Hyd'))        
# Output is 3   
print(len('Rama Rao'))   # Output is 8   
print(len('9247'))       
# Output is 4   
print(len(''))           
print(len(' '))          
print(len(689))          
# Output is 0   
# Output is 1   
# TypeError: object of type 'int' has no len()   
#Find outputs (HOMEWORK) 
a = """"Hyd"""   
print(a)             
print(len(a))        
print(a[0])          
# Output is "Hyd   
# Output is 4   
# Output is "   
print("""Hyd"""")    # SyntaxError: unterminated string literal   
b = """""Hyd"""   
print(b)             
# Output is empty string   
print(len(b))        
# Output is 0   
#Find outputs (HOMEWORK) 
a = 'Sankar Dayal Sarma'   
print(a[7:12])        
print(a[7:])          
print(a[:6])          
print(a[:])           
print(a[::])          
print(a[1:10:2])      
print(a[0::2])        
print(a[1::2])        
print(a[-5:-1])       
print(a[::-1])        
# Output is Dayal   
# Output is Dayal Sarma   
# Output is Sankar   
# Output is full string   
# Output is full string   
# Output is aka a   
# Output is SnkrDylSra   
# Output is a a a aa   
# Output is Sarm   
# Output is amraS lay aD raknaS   
print(a[-1:-5:-1])    # Output is amra   
print(a[::-2])        
# Output is arSlyDrka   
print(a[3:-3])        
print(a[2:-5])        
print(a[-1:-5])       
print(a[3:3])         
# Output is kar Dayal Sa   
# Output is nkar Dayal   
# Output is empty (invalid slice)   
# Output is empty (same start and end index)   
#Find outputs (HOMEWORK) 
a = 'A'   
print(a[1])          
# IndexError: string index out of range   
print(a[1:])         
# Output is empty string   
#int() function demo program (HOMEWORK) 
print(int(10.8))         
print(int(True))         
print(int(False))        
print(int('25'))         
print(int('0075'))       
print(int(0B11010))      
print(0B11010)           
print(int(0O6247))       
print(0O6247)            
print(int(0xA7B9))       
print(0xA7B9)            
print(int(3 + 4j))       
print(int('25.4'))       
print(int('Ten'))        
# Converts 10.8 to 10   
# Converts True to 1   
# Converts False to 0   
# Converts string '25' to int 25   
# Converts string '0075' to int 75   
# Binary 11010 → 26   
# Output is 26   
# Octal → 3255   
# Output is 3255   
# Hex → 42937   
# Output is 42937   
# TypeError: can't convert complex to int   
# ValueError: invalid literal (has .)   
# ValueError: invalid literal   
#float() function demo program (HOMEWORK) 
print(float(25))         
print(float(True))       
print(float(False))      
print(float('92'))       
print(float('36.4'))     
print(float('0075'))     
# Converts 25 to 25.0   
# Converts True to 1.0   
# Converts False to 0.0   
# String '92' → 92.0   
# String '36.4' → 36.4   
# String '0075' → 75.0   
print(float(0B1010101))  # Binary → 85 → 85.0   
print(float(0O6247))     # Octal → 3255.0   
print(float(0xA7B9))     # Hex → 42937.0   
print(float(3 + 4j))     # TypeError: can't convert complex to float   
print(float('Ten'))      
# ValueError: invalid literal   
#complex() function demo program (HOMEWORK) 
print(complex(3, 4))         
print(complex(0, 4))         
print(complex(3))            
# Output is (3+4j)   
# Output is 4j   
# Output is (3+0j)   
print(complex(3.8, 4.6))     # Output is (3.8+4.6j)   
print(complex(3.8))          
print(complex(3, 4.5))       
# Output is (3.8+0j)   
# Output is (3+4.5j)   
print(complex(True, False)) # Output is (1+0j)   
print(complex(True))        
# Output is (1+0j)   
print(complex(False))       
# Output is 0j   
print(complex(True, 4))     # Output is (1+4j)   
print(complex('3'))         
# Output is (3+0j)   
print(complex('3.8'))       
print(complex(3, '4'))       
print(complex('3', 4))       
print(complex('3', '4'))     
print(complex('Ten'))        
# Output is (3.8+0j)   
#  TypeError: second arg can't be string   
#  TypeError: first arg is string, second must not be   
# Output is (3+4j)   
# ValueError: invalid literal   
#bool() function demo program (HOMEWORK) 
print(bool(0))             
print(bool(10))            
print(bool(-25))           
print(bool(0.0))           
print(bool(0.1))           
print(bool(0 + 0j))        
print(bool(10 + 20j))      
print(bool(-15j))          
print(bool('False'))       
print(bool(''))            
print(bool('Hyd'))         
print(bool(' '))           
print(bool('True'))        
# Output is False   
# Output is True   
# Output is True   
# Output is False   
# Output is True   
# Output is False   
# Output is True   
# Output is True   
# Output is True (non-empty string)   
# Output is False   
# Output is True   
# Output is True   
# Output is True   
#str() function demo program (HOMEWORK) 
print(str(25))             
print(str(10.8))           
print(str(3 + 4j))         
print(str(True))           
print(str(False))          
print(str(None))           
# Output is '25'   
# Output is '10.8'   
# Output is '(3+4j)'   
# Output is 'True'   
# Output is 'False'   
# Output is 'None'   
#oct() function demo program (HOMEWORK) 
print(oct(195))            
# Output is '0o303'   
print(oct(0B10101110010))  # Binary → 1394 → Octal = '0o2622'   
print(oct(0xA7B9))         
# Hex → 42937 → Octal = '0o123671'   
#hex() function demo program (HOMEWORK) 
print(hex(25))             
# Output is '0x19'   
print(hex(0B10101111010111))  # Binary → 5615 → Hex = '0x15d7'   
print(hex(0O6247))         
# Octal → 3255 → Hex = '0xcb7'  