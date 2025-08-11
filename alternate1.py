s = input("Enter any string with alternate character and digit : ")

# Check length of input is even (pairs of char & digit)
if len(s) % 2 != 0:
    print("String should have alternate character and digit")
else:
    result = ""
    valid = True
    for i in range(0, len(s), 2):
        char = s[i]
        digit = s[i+1]

        # Check char is alphabetic or symbol (not digit), and digit is numeric
        if not char.isalpha() and not (33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126):
            # char is neither alphabet nor common symbols (just a generic check for symbol range)
            valid = False
            break
        if not digit.isdigit():
            valid = False
            break

        result += char * int(digit)
    
    if valid:
        print("Result :  ", result)
    else:
        print("String should have alternate character and digit")
