# SC = O(n)
def merge(arr,st,mid,end):         # O(n) time complexity
    temp = []
    i, j = st, mid+1
    inv_count = 0
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            inv_count += (mid-i+1)
            j+=1
    if i<=mid:
        temp.extend(arr[i:mid+1])
    if j<=end:
        temp.extend(arr[j:end+1])

    for i in range(len(temp)):
        arr[st + i] = temp[i]
        
    return inv_count

def mergesort(arr,st,end):         # O(nlogn) time complexity
    left_invcount, right_invcount, inv_count = 0, 0, 0
    if st<end:
        mid = st + (end-st)//2
        left_invcount = mergesort(arr,st,mid)
        right_invcount = mergesort(arr,mid+1,end)
        inv_count= merge(arr,st,mid,end)
    return (left_invcount + right_invcount + inv_count)

def count_inversions(arr):
    return mergesort(arr,0,len(arr)-1)

ans = count_inversions([6,3,5,2,7])
print(ans)