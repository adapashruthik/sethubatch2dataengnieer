# Input string from user
s = input("Enter any string : ")

even_chars = ""  # to hold chars at even indexes
odd_chars = ""   # to hold chars at odd indexes

# Loop over all indexes and characters
for i in range(len(s)):
    if i % 2 == 0:
        even_chars += s[i]
    else:
        odd_chars += s[i]

print("String at even indexes : " + even_chars)
print("String at odd indexes : " + odd_chars)
