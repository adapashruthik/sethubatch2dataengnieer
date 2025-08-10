from sys import argv
try:
    a=int(argv[1])
    if(a%2==0):
        print("Even Number")
    else:
        print('Odd Number')
except :
    print("pls send an integer input")