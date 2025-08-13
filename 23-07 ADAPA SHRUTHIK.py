ADAPA SHRUTHIK
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a  =  25
print(a++)   #  (a+)+  =  a+ =  25+  throws   error
print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a) # -(-a)= +a= 25
print(a--) # Error
print(a--1) # (a-)-1 = a+1=26
print(-a) # -25
print(+-a)  #+(-25) = -25
print(-+a) #-(+25)= -25


#  Semicolon  demo  program
print('One'); #One 
print('Two'); #Two
print('Three'); #Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb') # Hyd <nextLine> Sec <nextLine> Cyb

 #  floor()  and  ceil()  functions  demo  program
import  math #math module import
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0)) #25
print(math . ceil(25.0)) #25
print(math . floor(-3.5)) #-4
print(math . ceil(-3.5)) #3
print(math . floor(-9.0)) #-9
print(math . ceil(-9.0)) #-9
print(math . floor(25.1)) #25
print(math . ceil(25.1)) #26
print(floor(3.5)) #Error there is no method floor in current program
print(ceil(3.5)) #Error there is no method ceil in current program


'''
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'
'''

 # gcd()  function  demo  program
import  math
print(math . gcd(12 , 15)) #    3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7)) #   1
print(math . gcd(7 , 7)) # 7
print(math . gcd(-18 , -27)) #9
print(math . gcd(-4 , 6)) # 2
print(math . gcd(0 , 7)) # 7
print(math . gcd(3 , 0)) # 3
print(math . gcd(0 , 0)) # 0
print(gcd(5 , 15)) #Error there is no gcd method method in current program

#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) #35.8
print(abs(-27)) #27
print(abs(29.5)) #29.5
print(abs(32)) #32

import  builtins
print(builtins . abs(-25)) #25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) #5.9
print(max(25 , 10.8)) #25

import  builtins
print(builtins . max(10 , 20 , 30)) #30
print(builtins . min(10 , 20 , 15 , 5 , 12)) #5

 # pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) #0.01
print(pow(4 , pow(3 , 2))) #262144

import  builtins
print(builtins . pow(2 , 3)) #8
print(builtins . pow(-2 , -3)) #0.125

 # Find  outputs
How  to  import   kw  list  # from keyword import kwlist
How  to  print  kwlist #Print(kwlist)
How  to  print  number  of  keywords  #Print(len(kwlist))
How  to  print  type  of kwlist #Print(type(kwlist))
print(keyword . kwlist)  #Error

 #  Find  outputs  (Home  work)
How  to  import   keyword  module # import keyword
How  to  print  kwlist #print(keyword.kwlist)
How  to  print  number  of  keywords #Print(len(keyword.kwlist))
How  to  print  type  of kwlist  #Print(type(keyword.kwlist))
print(kwlist) #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']