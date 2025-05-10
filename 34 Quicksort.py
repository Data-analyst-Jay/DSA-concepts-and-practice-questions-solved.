# Avg TC = O(nlogn) 
# Worst TC = O(n^2) When pivot == largest/smallest element
# SC = O(1)
def partition(arr,st,end):
    pivot = arr[end]
    idx = st-1
    for j in range(st,end):
        if arr[j] < pivot:
            idx += 1
            arr[idx],arr[j] = arr[j],arr[idx]
    arr[idx+1],arr[end] = arr[end],arr[idx+1]
    return idx+1

def quicksort(arr,st,end):
    if st < end:
        pi = partition(arr,st,end)
        quicksort(arr,st,pi-1)
        quicksort(arr,pi+1,end)
        return arr
    
arr = [10, 7, 8, 9, 1, 5]
ans = quicksort(arr,0,len(arr)-1)
print(ans)