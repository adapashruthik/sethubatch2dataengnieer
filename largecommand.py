import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send inputs")
else:
    inputs = argv[1:]
    # Try to convert all inputs to float
    all_numbers = True
    all_strings = True
    a = []
    for item in inputs:
        try:
            num = float(item)
            a.append(num)
            all_strings = False
        except ValueError:
            a.append(item)
            all_numbers = False

    if all_numbers:
        print(f"argv = {argv}")
        print(f"List 'a' = {a}")
        print(f"Largest command line input is: {max(a)}")
        print(f"max(argv[1:]) = {max(argv[1:])}")  # Shows string comparison
        print("Issue with max(argv[1:])? ---> Largest string is obtained but not largest number")
    elif all_strings:
        print(f"Largest command line input is: '{max(a)}'")
    else:
        print("Inputs can not be number and string mixed")
