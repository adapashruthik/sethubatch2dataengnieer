a=input("Enter any string: ")
Even=[]
Odd=[]
for i in range(len(a)):
    if i%2==0:
        Even.append(a[i])
    else:
        Odd.append(a[i])
print("String at Even indexes : ",*Even)
print("String at odd indexes : ",*Odd)