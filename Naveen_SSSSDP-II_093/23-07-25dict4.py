a={10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(a)
for x in a.keys():
    print(x)
for x in a.values():
    print(x)
for x in a.items():
    print(x)
for x,y in a.items():
    print(x,y,sep='...')
for x in a.keys():
    print(x,a[x],sep=':')
    