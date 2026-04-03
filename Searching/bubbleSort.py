def BSort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

a=[]
l=int(input("Enter the size of the array:"))
print(f"Enter the {l} array elements:")
for i in range(l):
    b=int(input(""))
    a.append(b)


print(BSort(a))