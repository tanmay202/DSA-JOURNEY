def Binary_It(arr,key):
    n=len(arr)
    first=0
    last=n-1
    while first<=last:
        mid=(first+last)//2

        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            last=mid-1
        else:
            first=mid+1
    return -1


def Search():
    arr=[]
    n=int(input("Enter the size of the array:"))
    if n == 0:
        print("Array is empty")
        return
    
    print(f"Enter {n} elements:")

    for i in range(n):
        a=int(input(''))
        arr.append(a)
    arr.sort() 

    key=int(input('Enter the key you want to find:'))
    srch=Binary_It(arr,key)
    if srch!=-1:
        print(f'Element found at index {srch}')
    else:
        print('Element not found')

Search()