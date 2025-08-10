import sys 
if len(sys.argv)<2:
    print("enter command line arguments")
else:
     larg=eval(sys.argv[1])
     for i in sys.argv[2:]:
        num=float(i)
        if num>larg:
            larg=num
            print("largest number is:",larg)
