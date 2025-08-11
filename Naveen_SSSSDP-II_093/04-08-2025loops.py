#fibonacci
'''
x=int(input('Enter value of x :'))
if x==0:
    print(0)
else:
    a=0
    b=1
    print('Fibonacci Series')
    print(a)
    print(b)
    c=a+b
    while c<=x:
        print(c)
        a=b
        b=c
        c=a+b
'''
#infinite loop
'''
while True: # if True loop is infinite if False it is not executed
    print('Hello')
print()
'''
#assignment
'''
for x in [10,20,15,18]:
    print(x)
print()
for ch in 'Hyd':
    print(ch)
for x in range(5):
    print(x)
'''
#assignment2
'''
for x in {10:20,30:40,50:60}.keys():
    print(x)
print()
for x in {10:20,30:40,50:60}.values():
    print(x)
print()
for x in {10:20,30:40,50:60}.items():
    print(x)
for x in {10:20,30:40,50:60}:
    print(x)
'''
#assignment3
'''
a={10:20,30:40,50:60}
for x,y,in a.items():
    print(x,y,sep='...')
'''
'''
for x,y in a:
    print(x,y)
for x,y in {10:20,30:40,50:60}:
    print(x,y,sep='...')
'''
#assignment4
'''
for x in 123:   # loop cannot be iterate throw non-sequence
    print(x)
'''
#assignment 5
'''
for x in ():
    print(x)
for x in []:
    print(x)
for x in {}:
    print(x)
for x in set():
    print(x)
for x in '':
    print(x)
for x in range(10,10):
    print(x)
'''
'''
for x in range():   # error range can be 0,2.. not 0
    print(x)
for x in (25):      # error loop cannot throw iterate
        print(x)
'''
#nested loop demo
'''
for i in range(1,4):
    for j in range(1,5):
        print(i,j)
    print('Hello')
print('Bye')
'''
#assignment
'''
a=[25,10.8,'Hyd',True]
print('Indexed based for loop')
for i in range(len(a)):
    print(i,a[i],sep='...')
'''
#reverse order 
'''
a=[25,10.8,'Hyd',True]
print('Indexed for loop')
for i in range(1,len(a)+1):
    print(a[-i])
'''
#add-list
'''
a=eval(input('Enter 1st list:'))
b=eval(input('Enter 2nd list:'))
c=[]
small=min(len(a),len(b))
for i in range(small):
    c.append(a[i]+b[i])
print('3rd list:',c)
'''
#part of list
'''
a=[25,10.8,'Hyd',True,3+4j,None,'Sec']
for i in range(2,5):
    print(a[i])
'''
#assignment
'''
a=[10,20,15,18]
for i in range(len(a)):
    a[i]+=1
print('a:',a)
b=[10,20,15,18]
for x in b:
    x+=1
print('b:',b)
'''
#pyramid
n=int(input('How many lines?:'))
s=n-1
for i in range(1,n+1):
    print(' '*s,end='')
    s-=1
    print('*'*(2*i-1))