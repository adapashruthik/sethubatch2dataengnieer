'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''

n=int(input("Enter a number"))
for i in range(1,n+1):
    spaces=' '*(n-i)
    stars='*'*(2*i-1)
print(spaces+stars)
