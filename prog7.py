a=input("Enter first string: ")
b=input("Enter second string: ")
if len(a) or len(b) <2:
    print("Input should be a min of 2-char string")
else:
    print("Result: ",b[0:2]+a[2:]+" "+a[0:2]+b[2:])