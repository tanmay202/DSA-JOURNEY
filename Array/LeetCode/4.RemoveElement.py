list=list()

size=int(input("Enter size of the array:"))

list=[]

print(f"Enter{size} elements:")

for i in range(size):
    l=int(input())
    list.append(l)

print(f"List:{list}")

ele=int(input("Enter an element to remove:"))

new=[]
for i in list:
    if i!=ele:
        new.append(i)
print(f"Removed element list:{new}")



