#relational operator
print(9>=5)
print(9>=9)
print(9>=12)
print(6<=8)
print(6<=6)
print(6<=4)
print(9!=7)
print(6==8)
print(True>False)
print(3+4j==3+4j)
print(3+4j==5+6j)
print(3+4j!=5+6j)
print(10==10.0)
#print(3+4j>3+4j)     # complex numbers cannot be compared with >
print()
#string-comp
print('Rama'>'Rajesh')    # True 'm'>'j'
print('Rama'<'Sita')      # True  'R'<'S'
print('Hyd'=='Hyd')        # True same strings
print('Rama'<='Ramana')     # True ''>='n'
print('Rama Rao'>='Rama')    # True ' '>=''
print('Hyd'!='Sec')          # True
print('Hyd'<'hyd')           # True 'H'<'h'
print()
#chaining
print(10<20<30)            # True
print(10>=20<30)           # False
print(10<20>30)            # False
print(1<2>3>1)              # False
print(1<2<3<4)              # True
print(4>3>=3>2)             # True