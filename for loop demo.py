#for loop
# for loop
lst = input("Enter list elements separated by space: ").split()
search = input("Enter element to search: ")
found = True
for item in lst:
    if item == search:
        found = False
        break
if found:
    print("Found")
else:
    print("Not found")