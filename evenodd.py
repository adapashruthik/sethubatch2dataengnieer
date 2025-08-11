import sys

argv = sys.argv

if len(argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(argv[1])
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")
