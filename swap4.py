try:
    x=int(input("Enter the x value: "))
    y=int(input("Enter the y value: "))         
    print('values before swap:', x, y)
    temp=x
    x=y
    y=temp
    print('values after swap:', x, y)
except ValueError:
    print('Invalid input, please enter valid integers.')
    