# Find outputs (Home work)
 for i in range(1 , 8):
 print(i)
 if i % 3 ==0:
 continue
 else:
 print('Sec')
 print('Hello')
 # Endof loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 4
 Sec
 Hello
 5
 Sec
 Hello
 6
 7
 Sec
 Hello
 Outside loop
 # Identify Error (Home work)
 if ():
print('Hyd')
 continue
 print('Sec')
 Error:
 Continue is used in for and while loops only. Not in if statements.
 # Find outputs (Home work)
 for i in range(1 , 8):
 print(i)
 if i %3==0:
 break
 else:
 print('Sec')
 print('Hello')
 # End of the loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 Outside loop
 # Identify Error (Home work)
 if(10 , 20 , 30):
 print('Hyd')
 break
 print('Sec')
 Error:
 Break is used in for and while loops only. Not in if statements.
 # Find outputs (Home work)
 for i in range(1 , 8):
print(i)
 if i %3==0:
 pass
 print('Hyd')
 else:
 print('Sec')
 print('Hello')
 # End of the loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 Hyd
 Hello
 4
 Sec
 Hello
 5
 Sec
 Hello
 6
 Hyd
 Hello
 7
 Sec
 Hello
 Outside loop
 # Find outputs (Home work)
 for i in range(1 , 8):
print(i)
 if i %3==0:
 exit()
 else:
 print('Sec')
 print('Hello')
 # End of the loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 # Find outputs (Home work)
 for i in range(1 , 8):
 print(i)
 if i %3==0:
 continue
 else:
 print('Sec')
 print('Hello')
 else:
 print('else suite')
 # End of the loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 4
Sec
 Hello
 5
 Sec
 Hello
 6
 7
 Sec
 Hello
 Else suite
 Outside loop
 # Find outputs (Home work)
 for i in range(1 , 8):
 print(i)
 if i % 3==0:
 break
 else:
 print('Sec')
 print('Hello')
 else:
 print('else suite')
 #End of the loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 Outside loop
 # Find outputs (Home work)
 for i in range(1 , 8):
print(i)
 if i == 8:
 break
 else:
 print('Sec')
 print('Hello')
 else:
 print('else suite')
 # End of the loop
 print('Outside loop')
 Output:
 1
 Sec
 Hello
 2
 Sec
 Hello
 3
 Sec
 Hello
 4
 Sec
 Hello
 5
 Sec
 Hello
 6
 Sec
 Hello
 7
 Sec
 Hello
 Else suite
 Outside loop
 1)Write a program to search for an element in the list without using in operator and
 print Found or Not Found message (Assume that there are no duplicates)
Let list be [10 , 20 , 15 , 12 , 18]
 1) What is the output if 15 is seacrhed?---> Found at index 2
 2) What is the output if 19 is seacrhed?---> Not found
 3) What action to be made when 'x' does not match with the current element of list ?--->
 Compare 'x' with next
 element of list
 4) What action to be made when 'x' matches with list element?--->
 Print found message along with index
 and
 do not search for 'x' in rest of the list
 5) What action to be made when 'x' does not match with all the elements of list?--->
 Print not found message
 6) Hint: Use for loop
 Code:
 lst = [10, 20, 15, 12, 18]
 x =int(input("Enter element to search: "))
 found = False
 for i in range(len(lst)):
 if x == lst[i]:
 print(f"{x} is found at index {i}")
 found = True
 break # Stop after first match since no duplicates
 if not found:
 print("Not found")
2) Write a program to search for an element in the list and print index of each element
 and also number of times it is found(Assume that list may contain duplicate elements)
 List : [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
 Search for 15
 Outputs : 15 is found at index 2
 15 is found at index 5
 15 is found at index 8
 15 is found 3 times
 Code:
 lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
 x =int(input("Enter element to search: "))
 count = 0
 for i in range(len(lst)):
 if x == lst[i]:
 print(f"{x} is found at index {i}")
 count += 1
 if count > 0:
 print(f"{x} is found {count} times")
 else:
 print("Not found")
 # Walrus operator (:=) demo program
 print(a := 25) #25
 print(a = 25) #Error
 print(a) #25
 print(a := 6 + 7) #13
 print(a) #13
 print((a := 6) + 7) #6+7=13
 print(a) #6
 print((a = 6) + 7) #Error
 # Find outputs (Home work)
 a =0
 if a == 0:
 print('Hyd')
else:
 print('Sec')
 if b := 0:
 print('Hyd')
 else:
 print('Sec : ' , b)
 if c = 0: #error:==
 print('Hyd')
 else:
 print('Sec')
 Output:
 Hyd
 Sec: 0
 3)Write a program to determine average of inputs which are terminated with ctrl + z
 (without walrus operator)
 Let inputs be 25 , 10.8 , True , ctrl + z
 sum=0+25+10.8+True=36.8
 ctr = 0 + 1 +1+1=3
 1) What is ctrl + z ?---> End of inputs i.e. No more inputs
 2) What does input() function do when input is ctrl + z ?---> Throws EOFError
 3) How is end of inputs denoted in unix?---> ctrl + d
 Code:
 sum_ =0
 count = 0
 print("Enter values one by one (Ctrl+Z to end on Windows, Ctrl+D on Linux/Mac):")
 try:
 while True:
 val = input() # Take input
 val = eval(val) # Convert string input to number or boolean
 sum_ +=val
count += 1
 except EOFError:
 if count > 0:
 avg = sum_/count
 print("Average:", avg)
 else:
 print("No valid inputs entered.")
 a =25
 print(a)
 del a
 print(a)
 # Assigns 25 to variable `a`
 # Prints 25
 # Deletes the variable `a` from memory
 # ERROR:`a` is no longer defined
 a =b=c=25 #Allvariablespoint tothe samevalue 25
 print(a, b, c)
 # Line 1
 del a
 print(b, c)
 print(a)
 del b
 print(c)
 print(b)
 del c
 print(c)
 # Line 2: deletes only 'a', not the value 25 or other variables
 # Line 3
 # Line 4: 'a' is deleted → NameError
 # Line 5: Not executed because of error in Line 4
 # Line 6: Not executed
 # Line 7: Not executed
 # Line 8: Not executed
 # Line 9: Not executed
 a , b, c =25,10.8 , 'Hyd' #Variables a, b, and c are created
 print(a , b , c)
 # Output: 25 10.8 Hyd
 del a , b , c
 print(a)
 print(b)
 print(c)
 # All three variables are deleted from memory
 # ERROR:name'a' is not defined
 # Notexecuted due to previous error
 # Notexecuted
 a =[10, 20 , 15, 18] #List is created
print(a)
 # Prints the entire list: [10, 20, 15, 18]
 del a[2]
 print(a)
 del a
 print(a)
 print(a[0])
 # Deletes the element at index 2 (value 15)
 # Nowthelist becomes: [10, 20, 18]
 # Deletes the variable `a` entirely from memory
 # ERROR:'a' is no longer defined
 # Notexecuted because of the error above
 a =(10 , 20 , 15,18)
 print(a)
 # Prints the whole tuple: (10, 20, 15, 18)
 print(a[0])
 del a[2]
 del a
 print(a)
 print(a[0])
 # Prints the first element: 10
 # ERROR!Tuples are immutable — you cannotdelete individual elements.
 # This line will never run due to previous error.
 # Not executed.
 # Notexecuted.