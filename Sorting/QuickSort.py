def Qsort(arr,low,high):
    if low<high:
        pivot=Partition(arr,low,high)
        Qsort(arr,low,pivot-1)
        Qsort(arr,pivot+1,high)
    return arr

def Partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high

    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j


a = [65, 23, 45, 12, 11]
print(Qsort(a,0,len(a)-1))