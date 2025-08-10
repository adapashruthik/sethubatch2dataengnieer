
from sys import argv
print("enter any command line inputs")
if len(argv)<2:
    print("plz enter more than one command line arguments")
else:
    [num:= [float(arg) for arg in argv[1:]]]
num.sort()
print("Ascending order:", num)
num.reverse()
print("Descending order:", num)