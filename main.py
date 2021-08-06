a = input()
a = a.split()
print(a , len(a))
out = []

for i in a:
    b = a[a.index(i)]
    c = a.index(i)
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
for i in b[0]:
    
    if b[0][0].isupper() == True :
        print(b[0])
    else :
        print (None)
 """