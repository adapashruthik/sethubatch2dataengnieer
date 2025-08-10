#  ++  and  --  operators  demo  program
a = 25
print(++a)# +(+a) = +a  =  25
#print(a++)# (a+)+  =  a+ =  25+  throws   error
print(a++1)# a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a)# -(-a)=+a=25
#print(a--)# (a-)- = a+=25+ : Error
print(a--1)# (a-)-1=a+1=26
print(-a) #-25
print(+-a) #+(-a)=-25
print(-+a)# -(+a)=-25

print()
print('One')#One
print('Two')#Two
print('Three')#Three
print('Hyd');print('Sec'),print('Cyb')# hyd (nextline) sec (nextline) Cyb  (; : curser goes nextline)

print()
#  floor()  and  ceil()  functions  demo  program
import math
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0))#25
print(math . ceil(25.0))#25
print(math . floor(-3.5))#-4: nearest previous value
print(math . ceil(-3.5))#-3: nearest next value
print(math . floor(-9.0))#-9
print(math . ceil(-9.0))#-9
print(math . floor(25.1))#25
print(math . ceil(25.1))#26
#print(floor(3.5))# error python checks for the function in the current program
#print(ceil(3.5))#error
print()

# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15)) #    3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7)) #   1
print(math . gcd(7 , 7))#7
print(math . gcd(-18 , -27))#9
print(math . gcd(-4 , 6))#2
print(math . gcd(0 , 7))#7
print(math . gcd(3 , 0))#3
print(math . gcd(0 , 0))#0
#print(gcd(5 , 15))#error python checks for the function in current program
print()
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))# 35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins . abs(-25))#25
print()
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))#20.6: prints maximum value
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9: prints minimum value
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30 
print(builtins . min(10 , 20 , 15 , 5 , 12))#5

print()
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#10^-2=0.01
print(pow(4 , pow(3 , 2)))#pow(3,2)=3^2=9,pow(4,9)=4^9=262144
import  builtins
print(builtins . pow(2 , 3))#2^3=8
print(builtins . pow(-2 , -3))#-2^-3=-0.125
print()

import keyword# imports list in the kwlist which is in keywords module
print(keyword.kwlist)# prints a list of all keywords in python
print(len(keyword.kwlist))#prints the length of the keywords
print(type(keyword.kwlist))# prints the type  of keyword object

print()

from keyword import kwlist# imports the keyword module
#from keyword import keylist
print(kwlist)# prints  all the keywords in python
print(len(kwlist))#prints the length of the keywords
print(type(kwlist))# prints the type  of keyword object

isis=25
print(isis)