
a = input()
#a = "The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship."\
#"This video was captured by one of our heroes who wishes peace."
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

c = {}
for i , j in b.items():
    #print(j[0] , type(j))
    if j[0].isupper() == True:
        if i==0:
            continue
        else:
            j = j.replace('.','')
            j = j.replace(',','')
            c[i+1] = j


if c == {}:
    print('None')
else:
    for i, j in c.items():
        print(f'{i}:{j}')
