

a = "The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship."\
"This video was captured by one of our heroes who wishes peace."
a = a.split()
b =dict(enumerate(a))

pop_keys = []
for i , j in b.items():
    if j[-1]== '.':
        if i == len(b)-1:
            continue
        else:
            pop_keys.append(i+1)

for i in pop_keys:
    b.pop(i)


for i , j in b.items():
    #print(j[0] , type(j))
    if j[0].isupper() == True:
        if i==0:
            continue
        else:
            j = j.replace('.','')
            print(f'{i+1}:{j}')


"""
out = []

for i in a:
    c = a.index(i)
    b = a[c]
    print(i , c+1  , b)
    if b[0][0].isupper()== True:
        if c == 0 :
            continue
        else:
            i = i.replace(".", "")
            out.append(f'{c+1}:{i}')
    else:
        continue
for i in out:
    print(i , end="\n")
"""
"""
for i in b[0]:
    
    if b[0][0].isupper() == True :
        print(b[0])
    else :
        print (None)
"""