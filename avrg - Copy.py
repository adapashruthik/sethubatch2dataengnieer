from sys import argv
print("enter any command line inputs")
if len(argv)<2:
    print("plz enter more than one command line arguments")
else:
    num=[float(arg) for arg in argv[1:]]
    avrg=sum(num)/len(num)
    print("average is:",avrg)
         
    

