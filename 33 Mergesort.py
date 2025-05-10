# O(n) space complexity
def merge(arr,st,mid,end):         # O(n) time complexity
    temp = []
    i, j = st, mid+1
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    if i<=mid:
        temp.extend(arr[i:mid+1])
    if j<=end:
        temp.extend(arr[j:end+1])
    return temp

def mergesort(arr,st,end):         # O(nlogn) time complexity
    if st<end:
        mid = st + (end-st)//2
        mergesort(arr,st,mid)
        mergesort(arr,mid+1,end)
        arr[st:end+1] = merge(arr,st,mid,end)
    return arr

arr = [9,8,7,6,5,4,3,2,1]
ans = mergesort(arr,0,len(arr)-1)
print(ans)