import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send number inputs")
else:
    inputs = argv[1:]
    a = []
    all_numbers = True
    for item in inputs:
        try:
            num = float(item)
            a.append(num)
        except ValueError:
            all_numbers = False
            break
    if not all_numbers:
        print("Pls don't send number and string inputs together")
    else:
        print("argv =", argv)
        print("List 'a' =", a)
        print("Sorted list (ascending):", sorted(a))
        print("Sorted list (descending):", sorted(a, reverse=True))
