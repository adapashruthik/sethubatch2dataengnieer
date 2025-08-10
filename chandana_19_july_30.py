'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
x=int(input('How many lines ? :'))
for i in range(x):
    a=x-i-1
    b=2*i+1
    print(' '*a,'*'*b)

