from sys import argv
try:
   a=[]
   for x in argv[1:]:
    a.append(float(x))
   s=sum(a)
   print("Average : ",(s/len(a)))
except:
  print("Pls send number Inputs")