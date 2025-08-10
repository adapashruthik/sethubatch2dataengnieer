from sys import argv
a=input("enter any string:")
if len(a) < 4:
 print("")
else:
 print(a[:2]+a[-2:])