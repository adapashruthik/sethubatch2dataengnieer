'''How  many  lines ?  :  4
      *
     ***
    *****
   *******'''
n = int(input("Enter the number of lines: "))
for i in  range(n):
    spaces = " "* (n-i-1)
    stars = '*' *(2*i-1)
    print(spaces+ stars)
    '''output:
     *
    ***
   *****
  *******'''
