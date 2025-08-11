try:
    x=int(input("Enter the x value: "))
    y=int(input("Enter the y value: "))
    print(f'Before swap: {x} \t {y}')
    x=x*y
    y=x//y
    x=x//y          
    print(f'After swap: {x} \t {y}')
except ValueError:
    print('Invalid input, please enter valid integers.')    