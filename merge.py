a=input("enter first string: ")
b=input("enter second string: ")
result=""
i=j=0
while i < len(a) or j < len(b):
    if i < len(a):
        result += a[i]
        i += 1
    if j < len(b):
        result += b[j]
        j += 1
        print("merged string:",result)