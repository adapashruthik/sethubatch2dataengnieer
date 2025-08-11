#assignment1
'''
for i in range(1,8):
    print(i)
    if i%3==0:
        continue
    else:
        print('Sec')
    print('Hello')

print('Outside loop')
'''
#assignment2
'''
if():
    print('Hyd')
    continue      # continue cannot be used without loop
    print('Sec')
'''
#Break program
'''
for i in range(1,8):
    print(i)
    if i%3==0:
        break
    else:
        print('Sec')
    print('Hello')
print('Outside loop')
'''
#assignment
'''
if(10,20,30):
    print('Hyd')
    break           # break cannot be used without loop
    print('Sec')
'''
#pass function
'''
for i in range(1,8):
    print(i)
    if i %3==0:
        pass
        print('Hyd')
    else:
        print('Sec')
    print('Hello')
print('Outside loop')
'''
#exit function
'''
for i in range(1,8):
    print(i)
    if i%3==0:
        exit()      # stops execution
    else:
        print('Sec')
    print('Hello')
print('Outside loop')
'''
#for-else 1
'''
for i in range(1,8):
    print(i)
    if i%3==0:
        continue
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')
'''
#for-else 2
'''
for i in range(1,8):
    print(i)
    if i%3==0:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')
'''
#for else 3
'''
for i in range(1,8):
    print(i)
    if i==8:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')
'''
#assignment
'''
a=eval(input('Enter any list :'))
x=eval(input('Enter the element to be searched:'))
for i in range(len(a)):
    if a[i]==x:
        print('Found at index:',i)
        break
        print('Not found')
'''
#assignment duplicate numbers
a=eval(input('Enter any list:'))
x=eval(input('Enter the element to be searched:'))
ctr=0
for i in range(len(a)):
    if a[i]==x:
        print('Found at index:',i)
        ctr+=1
print(F'{x} is found {ctr} times')