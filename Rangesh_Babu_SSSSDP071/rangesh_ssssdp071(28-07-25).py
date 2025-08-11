 
1)Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers 
First  complex  number   --->  3 + 4j 
2nd   complex  number   --->  5 + 6j 
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j 
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j 
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j 
What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j) 
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36) 
                                                                         = 39 / 61 + 2j / 61''' 
Code: 
a=complex(input("Enter first complex number: ")) 
b=complex(input("Enter second complex number: ")) 
print(f'sum: {a+b}') 
print(f'difference: {a-b}') 
print(f'product: {a*b}') 
print(f'division: {a/b:.2f}') 
 
# Identify  error 
else: 
  print('else  suite')  
print('Outside')  
Error: 
     We can’t use else without if suite. 
 
# Identify  error 
if  9 > 5 
 print('Hello') 
print('Bye') 
Error:  there is no colon after if  ‘if cond :’ like this 
 
# Identify  error 
if  9 > 12: 
 print('Hyd') 
else 
print('Sec') 
Error: there is no colon after else statement “else :” 
if  (10,20,15): 
print('Hyd') 
else: 
print('Sec') 
Error: Indentation error 
if  (): 
else: 
print('Bye')   
print('Hyd') 
print('Sec') 
Error: if and else should be in same indentation 
if  { }: 
{ 
} 
else: 
{ 
} 
print('One') 
print('Two') 
print('Three') 
print('Four') 
print('Five') 
print('Six') 
print('Bye') 
Error: Braces are not allowed in python after if and else 
if  (): 
else: 
if  []: 
print('One') 
print('Two') 
print('Three') 
print('Four') 
print('Five') 
 print('Six') 
else: 
if  {}: 
 print('Seven') 
 print('Eight') 
 print('Nine') 
else: 
 print('Hyd') 
 print('Sec') 
 print('Cyb') 
print('Bye') 
Error: Indentation errors 
 
2) Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement 
Code: 
a=int(input("Enter a number: ")) 
if a % 2 == 0: 
    print(f"{a} is an even number.") 
else: 
    print(f"{a} is an odd number.") 
 
# Find outputs  (Home  work) 
if(): 
        print('Hyd') 
        print('Sec') 
        print('Cyb') 
else: 
        print('One') 
        print('Two') 
        print('Three') 
print('Bye')  #One<next line> Two<next line>Three<next line>Bye 
 
# Find  outputs  (Home  work) 
if{10 : 20 , 30 : 40}: 
        print('Hyd') 
        print('Sec') 
        print('Cyb') 
print('Bye') #Hyd<nextLine>Sec<nextLine>Cyb<nextLine>Bye 
 
# Find outputs  (Home  work) 
if { }: 
 print('Hyd') 
 print('Sec') 
 print('Cyb') 
print('Bye') #Bye 
 
3)Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  
Code: 
try: 
    a=int(input("Enter month number (1-12): ")) 
    if a == 1: 
        print("January") 
    elif a == 2: 
        print("February") 
    elif a == 3: 
        print("March") 
    elif a == 4: 
        print("April") 
    elif a == 5: 
        print("May") 
    elif a == 6: 
        print("June") 
    elif a == 7: 
        print("July") 
    elif a == 8: 
        print("August") 
    elif a == 9:   
        print("September") 
    elif a==10: 
        print("October") 
    elif a==11: 
        print("November") 
    elif a==12: 
        print("December") 
 
    else: 
        print("Input should be (1 - 12).") 
except: 
    print(f"Input should be a integer.")     
 
4)Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif) 
0 - Zero 
1 - One 
2 - Two 
.... 
9 - Nine 
10 – Invalid 
Code: 
a=int(input("Enter a digit: ")) 
dic={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'eight',9:'Nine'} 
if a in dic: 
    print(dic[a]) 
else: 
    print('Invalid') 
Second code: 
a=int(input("Enter a digit: ")) 
if a == 0: 
    print("Zero") 
else: 
    if a == 1: 
        print("One") 
    else: 
        if a == 2: 
            print("Two") 
        else: 
            if a == 3: 
                print("Three") 
            else: 
                if a == 4: 
                    print("Four") 
                else: 
                    if a == 5: 
                        print("Five") 
                    else: 
                        if a == 6: 
                            print("Six") 
                        else: 
                            if a == 7: 
                                print("Seven") 
                            else: 
                                if a == 8: 
                                    print("Eight") 
                                else: 
                                    if a == 9: 
                                        print("Nine") 
                                    else: 
                                        print("Invalid")  