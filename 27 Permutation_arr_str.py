# TC = O(n!*n) SC = O(n!)
def get_permu(arr,idx,ans = None):
    if ans is None:
        ans = []
    if idx == len(arr):
        ans.append(arr.copy())
        return 
    for i in range(idx,len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        get_permu(arr,idx+1,ans)
        arr[i], arr[idx] = arr[idx], arr[i]
    return ans

l = [1,2,3]
a = get_permu(l,0)
print(a)

# For string