s = input("Enter string: ")
out = ""

for i in range(0, len(s), 2):
    out += s[i] + (chr(ord(s[i]) + int(s[i+1])) if ord(s[i]) + int(s[i+1]) <= ord('Z') else "_")

print(out)
