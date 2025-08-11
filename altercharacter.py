s = input("Enter any string with alternate character and digit : ")

# Validate that input length is even (pairs of char and digit)
if len(s) % 2 != 0:
    print("Pls enter string with alternate char and digit")
else:
    result = ""
    valid = True  # Flag to check validity

    for i in range(0, len(s), 2):
        char = s[i]
        digit = s[i+1]

        # Validate char is a letter or allowed symbol (not digit)
        if not char.isalpha():
            valid = False
            break

        # Validate digit is numeric
        if not digit.isdigit():
            valid = False
            break

        # Calculate shifted character code
        # ord(char) + int(digit)
        shifted_code = ord(char) + int(digit)

        # If shifted_code goes beyond 'Z' (assuming uppercase letters),
        # you may want to wrap or just keep as is - your example leaves 'Z' + 5 as '_'
        # chr(90 + 5) = chr(95) = '_', so this fits the example.

        result += char + chr(shifted_code)

    if valid:
        print("Result  :  ", result)
    else:
        print("Pls enter string with alternate char and digit")
