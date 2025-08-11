#  ++  and  --  operators  demo  program
a = 25
print(++a)                                         # +(+a) = +a  =  25                             
print(a++)                                         #  (a+)+  =  a+ =  25+  throws   error
print(a++1)                                        #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a)                                         # -(-a) = +a = 25
print(a--1)                                        #  a-(-1) = a+1 = 25+1 =26
print(-a)                                          #  (-a) = -25
print(+-a)                                         #  +(-a)= -25  
print(-+a)                                         #  -(+a)= -25

#  Semicolon  demo  program
print('One');                                       # one  
print('Two');                                       # Two
print('Three');                                     # Three
print('Hyd')  ;  print('Sec') ; print('Cyb')
    # Hyd
    # Sec
    # Cyb



 #  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))			# 10
print(math . ceil(10.8)				# 11
print(math . floor(25.0))			# 25
print(math . ceil(25.0))			# 25
print(math . floor(-3.5))			# -4                                           
print(math . ceil(-3.5))			# -3
print(math . floor(-9.0))                       # -9
print(math . ceil(-9.0))                        # -9
print(math . floor(25.1))                       # 25                      
print(math . ceil(25.1))			# 26
print(floor(3.5))				# Throws error
print(ceil(3.5))				# Throws error
'''
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'
'''

 # gcd()  function  demo  program
import  math
print(math . gcd(12 , 15))			 # 3
print(math . gcd(12 , 18))			 # 6
print(math . gcd(4 , 7))			 # 1
print(math . gcd(7 , 7))			 # 7
print(math . gcd(-18 , -27))			 # 9
print(math . gcd(-4 , 6))			 # 2
print(math . gcd(0 , 7))			 # 7			 
print(math . gcd(3 , 0))			 # 3
print(math . gcd(0 , 0))			 # 0
print(gcd(5 , 15)) 				 # Throws error


  #  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))                                # 35.8
print(abs(-27))					 # 27
print(abs(29.5))				 # 29.5
print(abs(32))					 # 32
import  builtins
print(builtins . abs(-25))			 # 25


# Find outputs 

a = 9248              
print(a)         # Prints the value of a, which is 9248
print(type(a))   # Prints the data type of 'a', which is <class 'int'>

                      
# float object demo program (Homework)

a = 10.8                         
print(a)                         # Prints the value of a, which is 10.8
print(type(a))                   # Prints the data type of a, which is <class 'float'>
print(id(a))                     # Prints the address of the object a
b = 25.                          # A float value with no digits after decimal 25.00
print(b)                         # Prints the value of b, which is 25.00
print(type(b))                   # Prints the data type of b, which is <class 'float'>
c = .689                         # A float value with digits only after the decimal point
print(c)                         # Prints the value of c, which is 0.689
d = 3.4E2                        # Mantissa exponent format 3.4 * 10^2 
print(d)                         # Prints the value of d, which is 340.00
print(type(d))                   # Prints the data type of d, which is  <class 'float'>
e = 9.62e-2                      # Mantissa exponent format 9.62 x 10^-2 
print(e)                         # Prints the value of e, which is 0.0962
print(9.8.2)                     # This is not a valid float in Python. Only one decimal point is allowed in a float.
print(9.8)                       # Prints the value 9.8
print(8.2)                       # Prints the value 8.2


# complex object demo program

a = 3 + 4j                      
print(a)                        # Prints the value of a, which is (3+4j)
print(type(a))                  # Prints the data type of a, which is <class 'complex'>
print(id(a))                    # Prints the address of the object a
print(a.real)                   # Prints the real part of a, which is 3.0
print(a.imag)                   # Prints the imaginary part of a, which is 4.0
print(type(a.real))             # Prints the data type of the real part, which is <class 'float'>
print(type(a.imag))             # Prints the data type of the imaginary part, which is <class 'float'>

# Find outputs (Homework)

a = 6j                           
print(a)                         # Prints 6j
print(type(a))                   # Prints the data type of a, which is <class 'complex'>
print(a.real)                    # Prints the real part of a, which is 0.0
print(a.imag)                    # Prints the imaginary part of a, which is 6.0
print(5 + j6)                    # Error due to 'j6'
print(3 + 4i)                    # Python uses 'j' not 'i' for imaginary part
print(4 + j)                     # Error due to 'j' is used without any number
print(4 + 1j)                    # Prints (4+1j)
print(4 + 0j)                    # Prints (4+0j)


# bool object demo program  (Home work)

a = True                         
print(a)                         # Prints True
print(type(a))                   # Prints the data type as <class 'bool'>
print(id(a))                     # Prints the address of the object 'a'
b = False                        
print(b)                         # Prints False
print(type(b))                   # Prints the data type as <class 'bool'>
print(True + True)               #  1 → 1 + 1 = 2
print(True + False)              # 1 + 0 = 1
print(False + True)              # 0 + 1 = 1
print(False + False)             # 0 + 0 = 0
print(True + True + True)        # 1 + 1 + 1 = 3
print(25 + 10.8 + True)          # 25 + 10.8 + 1 = 36.8 
print(True > False)              # True (1) > False (0) → True
print(True)                      # Prints True
print(False)                     # Prints False
print(true)                      #  'T' must be capital
print(false)                     #  'F' must be capital 'F')


# Find outputs (Home work)

a = 0O6247                      # Assigning an octal number 
print(a)                        # Prints 3247
print(type(a))                  # Prints <class 'int'>
print(id(a))                    # Prints the address of 'a'
b = 0o6247                       
print(id(b))                    # Will be same as 'a' since value is the same
print(b)                        # Prints 3247
c = 3239                        # A decimal number
print(c)                        # Prints: 3239
print(id(c))                    # Prints the address of 'c'
print(0o9248)                   # Error because Octal numbers only use digits from 0 to 7

# Find outputs (Home work)

a = 0xA7B9                    
print(a)                       # Prints 42937
print(type(a))                 # Prints <class 'int'>
b = 0xBEEF                     
print(b)                       # Prints 48879
print(A7B9)                    # Error  'A7B9' is consider as reference variable of a object
print('A7B9')                  # This prints the string 'A7B9'
print(0XBEER)                # Error because 'R' is not a valid hexadecimal digit
print(0XHYD)                 # Error because 'H', 'Y', and 'D' are invalid in hexadecimal
print(0xA7G9B)               # Error because 'G' is not valid in hexadecimal