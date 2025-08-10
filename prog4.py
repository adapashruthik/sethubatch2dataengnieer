from sys import argv
try:
    a=[]
    for x in argv[1:]:
        a.append(float(x))
    print('Ascending Order : ',sorted(a))
    print('Descending Order : ',sorted(a,reverse=True))
except:
    print("Pls don't send number and string inputs together")