from sys import argv
try:
    l=[]
    for i in argv[1:]:
        l.append(eval(i))
    print("largest is: ",max(l))
except ValueError:
    print("Enter atleast one input")
except NameError:
     print("Inputs cannot be a number and string")