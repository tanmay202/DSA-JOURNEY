a=[]
l=int(input("Enter array size:"))
print("Enter array values:")
for i in range(l):
    i=int(input(""))
    a.append(i)


sum=int(input("Enter sum:"))

for i in range(l):
    for j in range(i+1,l):  # see note below
        if a[i]+a[j]==sum:
            print(f'{a[i]}, {a[j]}')

# IMPORTANT:
# j should start from i+1 (not 0) to avoid:
# 1. Using the same element twice (i == j)
# 2. Getting duplicate pairs like (2,3) and (3,2)
# This ensures each pair is checked only once and previously i used l in both loop hich is not right
            

