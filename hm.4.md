\######## home work solved 29/07/2025######################

\########## Question ##################



\# Find  outputs  (Home  work)

m = 4

match  m:

&nbsp;	case  1:

&nbsp;		print('One')

&nbsp;	case  2:

&nbsp;		print('Two')

&nbsp;	case  3:

&nbsp;		print('Three')

print('Bye')   **## it only prints bye , because the given condition for m = 4 is not equal to cases in given program code**  







\#################################################################################################################################################################################





\########## Question ##################



\# Identify  Error

i = 2

match  i:

&nbsp;	case  1:

&nbsp;		print('One')

&nbsp;	case  \_:

&nbsp;		print('None of   the  above')

&nbsp;	case  2:

&nbsp;		print('Two')

print('Bye')                      ## error due to case \_ in between 



\#################################################################################################################################################################################





\########## Question ##################



\# Find  outputs  (Home  work)

m = 2

match  m:

&nbsp;	case  1:

&nbsp;		print('One')

&nbsp;	case  \_:

&nbsp;		print('Hello')

&nbsp;	case  \_:

&nbsp;		print('Bye')

print('End')          ##  error





\#################################################################################################################################################################################





\########## Question ################## ????????????????????????????????????????????????????



\#  Find  outputs  (Home  work)

m = 1

match  m:

&nbsp;	case  1:

&nbsp;		print('Hyd')

&nbsp;	case  1:

&nbsp;		print('Sec')

&nbsp;	case  1:

&nbsp;		print('Cyb')

print('Bye')                    ## nothing will be printed because case 1 : is repeated multiple times ,  





\#################################################################################################################################################################################





\########## Question ##################



\# Find  outputs  (Home  work)

ch = 'B'

match  ch:

&nbsp;	case   'A':

&nbsp;		print('Apple')

&nbsp;	case  'B':

&nbsp;		print('Book')

&nbsp;	case  'C':

&nbsp;		print('Cafe')

&nbsp;	case  \_:

&nbsp;		print('None of  the  above')

print('Bye')                                   ## Book and Bye is printed 









\#################################################################################################################################################################################





\########## Question ################## ???????????????????????





'''

1\) What  is  the  output  when  input  is  (-10 , -20) ?  ---> quadrant

2\) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis 

3\) What  is  the  output  when  input  is  (0 , -20) ?  ---> y -axis

4\) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin 

5\) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> not a point

6\) What  is  the  output  when  input  is  \[10 , 20]  ?  ---> quadrant

7\) What  is  the  output  when  input  is  \[0 , -25]  ?  ---> y -axis 

8\) What  is  the  output  when  input  is  ()  ?  ---> not a point

9\) What  is  the  output  when  input  is  {10 , 20} ?  ---> not a point 

10\) What  is  the  output  when  input  is  (25,) ?  ---> not a point 

11\) What  is  the  output  when  input  is  {10 : 20} ?  ---> not a point 

'''

tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))

match  tpl:

&nbsp;	case  (0 , 0):

&nbsp;		print('Origin')

&nbsp;	case   (0 , y):

&nbsp;		print('y - axis')

&nbsp;	case   (x , 0):

&nbsp;		print('x - axis')

&nbsp;	case   (x , y):

&nbsp;		print('Quadrant')

&nbsp;	case  \_:

&nbsp;		print('Not  a  point')















\#################################################################################################################################################################################





\########## Question ##################





\#  Find  outputs

while  True:

&nbsp;	print('Hello')

print('Bye')                  ## prints Hello 

&nbsp;                                       Bye 





\#################################################################################################################################################################################





\########## Question ##################





\#  Find  outputs

while  False:

&nbsp;	print('Hello')

print('Bye')             ## prints Bye 







\#################################################################################################################################################################################





\########## Question ##################



\# Find  outputs  (Home  work)

How  to  print  each  element  of  list  \[10 , 20 , 15 , 18]  with  for  loop

print()



\#### answere ###########

list = \[10 , 20 , 15 , 18]

for x in list:

&nbsp;	print(x)



\#### question #########



How  to  print  each  character  of   string  'Hyd'  with  for  loop

print()



\##### answere ####



a = 'hyd'

for i in a:

&nbsp;	print(i)



\##### question #####



How  to  print  each  element  of   range(5)  with  for  loop



\#### answere #####



x = int(input('Enter the value of range:')) 

for i in range(x):

&nbsp;	print(i)





\#################################################################################################################################################################################





\########## Question ##################



\# Find  outputs  (Home  work)

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():

&nbsp;	print(x)

print()      # prints 10 30 50 



\########## 

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():

&nbsp;	print(x)

print()  ## prints 20 40 60



\#########

for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():

&nbsp;	print(x)

print()       

&nbsp;	# prints 

(10, 20)

(30, 40)

(50, 60)



\########

for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:

&nbsp;	print(x)

\## prints 
10

30

50



\#################################################################################################################################################################################





\########## Question ##################

\# Find outputs  (Home  work)

a = {10 : 20 , 30 : 40 , 50 : 60}

for  x , y  in   a . items():

&nbsp;	print(x , y , sep = '...') 

\######## prints 

10...20

30...40

50...60



for  x ,  y  in   a:

&nbsp;	print(x , y)  # error 

for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:

&nbsp;	print(x , y , sep = '...') # error 









\#################################################################################################################################################################################





\########## Question ##################

\# Identify  error  (Home  work)

for  x  in   123:

&nbsp;       print(x) # non - sequence objects can't be given 





\#################################################################################################################################################################################





\########## Question ##################



\# Find  outputs  (Home  work)

for  x   in   ():

&nbsp;       print(x)  ## no output 

for  x   in  \[]:

&nbsp;       print(x)  ## no output

for  x   in   {}:

&nbsp;       print(x)   ## no output

for  x   in   set():

&nbsp;       print(x)   ## no output

for  x   in   '':

&nbsp;       print(x)   ## no output

for  x  in  range(10 , 10):

&nbsp;	print(x)    ## no output it should be range(10,0)

for  x  in   range():

&nbsp;	print(x)  ## no output , range should be 1 argument to decide end of the sequence

for  x  in   (25):

&nbsp;	print(x)    ## 'int' can't be used due to non-sequence objects







\#################################################################################################################################################################################





\########## Question ##################



\#  Nested  Loop  demo  program

for  i  in  range(1 , 4):

&nbsp;	for  j  in  range(1 , 5):

&nbsp;			print(i ,  j)  # prints range of elements 1 2 3 with j in range 1 2 3 4 and for every i,j it prints hello 

&nbsp;	print('Hello') 						and after range for both i ,j completes it prints bye 

print('Bye')

&nbsp;

\## outputs like these 



1 1

1 2

1 3

1 4

Hello

2 1

2 2

2 3

2 4

Hello

3 1

3 2

3 3

3 4

Hello

4 1

4 2

4 3

4 4

Hello

5 1

5 2

5 3

5 4

Hello

Bye



\#################################################################################################################################################################################





\########## Question ##################????????????????????????????????????????????????????????



\# How  to  print  each  element  and  the  corresponding  index

a = \[25 , 10.8 , 'Hyd' , True]

print('Indexed  based  for loop')



\##### answere ####









\### question ##



How  to  print  each  element  and  the  corresponding  index  with  index  based  for  loop

print('For each loop')





\### question ##



How  to  print  each  element  and  the  corresponding  index  with  for  ...  each  loop (Do  not  use  2nd  variable)







\#################################################################################################################################################################################





\########## Question ##################





How   to  print  each  element  of  list  in  reverse  order  with  indexed  based  for  loop





a = \[25 , 10.8 , 'Hyd' , True]

for x in a\[::-1]:

    print(x)



















