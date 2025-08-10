
a=input("enter any string:")
print("charecters at even index are:", end=" ")
for i in range(len(a)):
    if i%2==0:
        print(a[i],end="")
print()
print("charecters at odd index are:", end=" ")
for i in range(len(a)):
    if i%2!=0:
        print(a[i],end="")
print()