'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])#Rm a
print(a [ : 7])#Rama Ra
print(a [2 : 4])#ma
print(a [2 : ])#ma Rao
print(a [ : 4 ])#Rama
print(a [ : : 2])#Rm a
print(a [-6 : -1])#ma Ra
print(a [-6 : ])#ma rao
print(a [: -4 : -1])#oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])#Rao
print(a [ : : ])#Rama  Rao
print(a [ : ])#Rama  Rao
print(a [ : : -1])#oaR amaR
print(a [ : : -2])#oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])#ma Rao
print(a [2 : 8 : -1])#BLANK
print(a [ : -6 : -1])#oaR a
print(a [2 : -3])#ma
print(a [1 : 6 : 2])#aaR
print(a [ : -5 : -5])#o
