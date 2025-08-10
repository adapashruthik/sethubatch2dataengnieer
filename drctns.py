
a=input("enter any string:")
print("forword:",end=" ")
for i in a:
    print(i,end="")
print()
print("reverse:",end=" ")
for i in a[::-1]:
    print(i,end="")
    print()
