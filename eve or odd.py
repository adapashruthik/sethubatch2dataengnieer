
import sys
if len(sys.argv) < 2:
    print("enter any command line arguments")
else:
    try:
        num = int(sys.argv[1])
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
    except ValueError:
        print("Plz enter integers only")
        