# Program to concatenate two strings swapping their first two characters

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) < 2 or len(str2) < 2:
    print("Input should be a min of 2-char string")
else:
    # Swap first two characters
    # New first string = first two chars of str2 + rest of str1 from index 2
    new_str1 = str2[:2] + str1[2:]
    # New second string = first two chars of str1 + rest of str2 from index 2
    new_str2 = str1[:2] + str2[2:]
    
    # Concatenate with a space
    result = new_str1 + " " + new_str2
    
    print("Result  :  ", result)
