'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7   and   8  to a  single  line  with   walrus  operator
'''
# try:
# 	sum =  ctr = 0
# 	while  True:
# 		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))
# 		sum += x
# 		ctr +=1
# except  EOFError:
# 	try:
# 		print(F'Average :   {sum / ctr}')
# 	except  ZeroDivisionError:
# 		print('Enter  at  least  one  input')
# except  (NameError , TypeError):
# 	print('Input  can  not  be  string')
	
try:
    sum = ctr = 0
    while (x := eval(input('Enter input (ctrl + z to stop): '))):
        sum += x
        ctr += 1
except EOFError:
    try:
        print(f'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input cannot be string')
'''
output:
Enter input (ctrl + z to stop): 10
Enter input (ctrl + z to stop): 20
Enter input (ctrl + z to stop): 30
Enter input (ctrl + z to stop): ^Z
Average : 20.0
'''