def Linear(arr,key):
    n=len(arr)

    for i in range(n):
        if key==arr[i]:
            return i
    return -1 

arr=[]
n=int(input("Enter the size of the array:"))
print(f"Enter {n} elements:")

for i in range(n):
    a=int(input(''))
    arr.append(a)

key=int(input('Enter the key you want to find:'))
srch=Linear(arr,key)
if srch!=-1:
    print(f'Element found at index {srch}')
else:
    print('Element not found')