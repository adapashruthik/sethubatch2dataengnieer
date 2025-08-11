s = input("Enter a string: ")

if len(s) < 4:
    print("")  # empty string
else:
    result = s[:2] + s[-2:]
    print(result)
