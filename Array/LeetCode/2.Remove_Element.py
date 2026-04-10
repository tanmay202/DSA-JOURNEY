a=[1,2,3,3,3,4]

b=3

c=set(a)
print(c)
for i in range(len(a)):
    if c[i]==b:
        del a[i]

print(a)