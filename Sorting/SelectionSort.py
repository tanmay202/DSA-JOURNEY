def selection_Sort(arr):
    n=len(arr)
    for i in range(n-2):
        min_idx=i
        for j in range(i+1,n):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr





a = [65, 23, 45, 12, 11]
print(selection_Sort(a))
    