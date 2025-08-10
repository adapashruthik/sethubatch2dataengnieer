
s1=input("enter first string: ")
s2=input("enter second string: ")
new_s1=s2[:2]+s1[2:]
new_s2=s1[:2]+s2[2:]
result=new_s1+" "+new_s2
print("result:", result)