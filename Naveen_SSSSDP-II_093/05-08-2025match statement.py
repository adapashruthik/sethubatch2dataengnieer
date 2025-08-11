#day of the week with match..case
'''
try:
    m=int(input('Enter anty day number(1-7):'))
    match m:
        case 1:
            print('Monday')
        case 2:
            print('Tueday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
        case _:
            print('Invalid day number')
    print('Bye')
except:
    print('Input should be an integer')
'''
#assignmet
'''
m=4
match m:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
print('Bye')
'''
#assignment2
'''
m=2
match m:
    case 1:
        print('One')
    case _:              # case _ cannot br in middle of the match
        print('Hello')
    case _:                # valid
        print('Bye')
print('End')
'''
#assignment3
'''
m=1
match m:
    case 1:
        print('Hyd')
    case 1:
        print('Sec')
    case 1:
        print('Cyb')
print('Bye')
'''
#assignment4
'''
ch='B'
match ch:
    case 'A':
        print('Apple')
    case 'B':
        print('Book')
    case 'C':
        print('Cafe')
    case _:
        print('None of the above')
print('Bye')
'''
#assignment5
'''
x=eval(input('Enter any number:'))
match x:
    case 7 | -6 | 0:
        print('Hyd')
        print('Sec')
        print('Cyb')
    case -10 | 15:
        print('One')
        print('Two')
        print('Three')
    case _:
        print('India')
        print('China')
        print('Usa')
print('Bye')
'''
#assignment6
'''
a=[10,20,15,18]
for i in range(len(a)):
    a[i] += 1
print('a:',a)
b=[10,20,15,18]
for x in b:
    x += 1
print('b:',b)
'''
#electricity bill
'''
try:
    units=int(input('Enter units:'))
    match units // 100:
        case 0: 
            cost = units*3.00
        case 1:
            cost = 100*3.00+(units-100)*3.50
        case 2 | 3:
            cost = 100*3.00+100*3.50+75*4.00
        case 4 | 5 |6:
            cost = 100*3.00+100*3.50+200*4.00+(units-400)*4.50
        case _:
            print('Hello')
            cost = 100*3.00*100*3.50+200*4.00+300*4.50+(units-700)*5.00
    print('Bill amount :',cost)
except ValueError:
    print('Invalid input,please enter a vaild integer')
'''