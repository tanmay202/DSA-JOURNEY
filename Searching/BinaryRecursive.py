def BinaryRecursive(arr,key,left=0,right=None):
    if right is None:
        right=len(arr)-1
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return BinaryRecursive(arr,key,left,mid-1)
    else:
        return BinaryRecursive(arr,key,mid+1,right)
    
def Search():
    arr = []
    n = int(input("Enter the size of the array: "))

    if n == 0:
        print("Array is empty")
        return

    print(f"Enter {n} elements:")

    for i in range(n):
        a = int(input())
        arr.append(a)

    arr.sort() 
    key = int(input("Enter the key you want to find: "))

    srch = BinaryRecursive(arr, key)

    if srch != -1:
        print(f"Element found at index {srch}")
    else:
        print("Element not found")


Search()

Search()