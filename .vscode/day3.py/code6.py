#linear search
a=[]
for i in range(1,100):
    a.append(i)
target=99

b=list(range(1,100))
for i in b:
    if i==target:
        print('found')