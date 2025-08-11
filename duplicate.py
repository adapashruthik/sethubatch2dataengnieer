# Input string from user
s = input("Enter any string : ")

out = ""  # To store characters without duplicates

for char in s:
    if char not in out:
        out += char  # Concatenate if char not already in out

print("String without duplicates : ", out)
