try:
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    print(f'Before swap: {a} \t {b}')
    a=a+b
    b=a-b   
    a=a-b
    print(f'After swap: {a} \t {b}')
except ValueError:
    print('Invalid input, please enter valid integers.')