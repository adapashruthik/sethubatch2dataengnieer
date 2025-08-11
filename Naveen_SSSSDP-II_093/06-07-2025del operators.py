#del assignment1
a=25
print(a)
del a
#print(a)
print()
#del assignment2
a=b=c=25
print(a,b,c)
del a
print(b,c)
#print(a)     # ref 'a' does not exist
del b
print(c)
#print(b)      # ref 'b' does not exist
del c
#print(c)       # ref 'c' does not exist
print()
#del assignment 3
a,b,c=25,10.8,'Hyd'
print(a,b,c)
del a,b,c
#print(a)     # ref 'a' does not exist
#print(b)      # ref 'b' does not exist 
#print(c)     # ref 'c' does not exist
print()
#del assignment4
a=[10,20,15,18]
print(a)
del a[2]
print(a)
del a
#print(a)        # ref 'a' does not exist
#print(a[0])      # ref 'a' does not exist
print()
#del assignment5
a=(10,20,15,18)
print(a)
print(a[0])
#del a[2]     #tuple is immutable cannot be deleted
del a
#print(a)       # ref 'a' does not exist
#print(a[0])     # ref 'a' does not exist