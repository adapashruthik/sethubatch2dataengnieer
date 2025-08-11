# Command line arguments demo program
from sys import argv
print(argv) # ['progla.py', '25', 'Rama Rao', '10000.0', 'm', 'True']
print(type(argv)) # <class 'list'>
for i in range(len(argv)): # Each element of argv list along with index
    print(f'argv[ {i} ] : {argv[i]}')
print('argv list without filename : ', argv[1:]) # ['25', 'Rama Rao', '10000.0', 'm', 'True']
print('Number of inputs : ', len(argv) - 1) # 5