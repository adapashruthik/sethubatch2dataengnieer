import sys

n = sys.argv[1:]  # Skip the script name

if not n:
    print("Please provide numbers as command-line arguments.")
else:
    for i in n:
        try:
            num = int(i)
            if num % 2 == 0:
                print(f"{num} is Even")
            else:
                print(f"{num} is Odd")
        except ValueError:
            print(f"{i} is not a valid integer.")
