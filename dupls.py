a=input("enter any string:")
res=""
for i in a:
    if i not in res:
        res += i
print("string after removing duplicates:", res)        