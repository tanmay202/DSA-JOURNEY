def SelSort(arr):
    n=len(arr)
    for i in range(n-1):
        minIdx=i
        for j in range(i+1,n):
            if arr[j]<arr[minIdx]:
                minIdx=j
        if minIdx !=i:
            arr[i],arr[minIdx]=arr[minIdx],arr[i]
    return  arr

print(SelSort(arr=[1,4,5,34,21,12]))