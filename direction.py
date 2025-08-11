# Input string
s = input("Enter a string: ")

# Print characters in forward direction with positive indices
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

print()  # Blank line

# Print characters in reverse direction with negative indices
for i in range(1, len(s) + 1):
    print(f"Character at index {-i} : {s[-i]}")
