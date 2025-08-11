try:
    num=int(input('Enter a number from[0-9]: '))
    if num==0:
        print('zero')
    elif num==1:
        print('one')
    elif num==2:
        print('two')
    elif num==3:
        print('three')  
    elif num==4:
        print('four')
    elif num==5:
        print('five')
    elif num==6:
        print('six')    
    elif num==7:
        print('seven')
    elif num==8:
        print('eight')
    elif num==9:
        print('nine')
    else:
        print('Invalid input, please enter a number between 0 and 9.')
except:
    print('An error occurred. Please enter a valid number.')