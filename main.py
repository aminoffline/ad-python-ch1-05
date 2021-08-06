a = input()
a = a.split()
count = {}
#while True:
for i in a:
    if i.isupper() == True:
        c = a.index(i)
        count[c+1] = i
    else:
        continue
print(count)