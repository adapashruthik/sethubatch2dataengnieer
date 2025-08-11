import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send number inputs")
else:
    inputs = argv[1:]
    a = []
    try:
        for item in inputs:
            if item == 'True':
                a.append(True)
            elif item == 'False':
                a.append(False)
            else:
                a.append(float(item))
        print("argv =", argv)
        print("List 'a' =", a)
        average = sum(a) / len(a)
        print("Average is:", round(average, 2))
    except ValueError:
        print("Pls send number inputs")
