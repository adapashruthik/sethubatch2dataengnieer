'''
Write  a  program  to  print  full  pyramid
	*
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
n = int(input("Enter the number of lines: "))
for i in  range(n):
    spaces = " "* (n-i-1)
    stars = '*' *(2*i-1)
    print(spaces+ stars)