#88
# Merge 2 sorted arrays #O(m+n) / O(1)
def merge(arr,m,brr,n):
    indx, i, j = m + n - 1, m-1, n-1
    while i>=0 and j>=0:
        if arr[i] > brr[j]:
            arr[indx] = arr[i] 
            indx-=1
            i-=1
        else:
            arr[indx] = brr[j]
            j-=1
            indx-=1
    while j>=0:
        arr[indx] = brr[j]
        j -= 1
        indx -= 1
    print(arr)      

# a = [1,2,3,0,0,0]
# b = [2,5,6]
# merge(a,3,b,3)

#31 #O(n) / O(1)
# Lexicographic arrangement = Arrangment of different permutations of numbers or strings in ascending order
def next_permu(arr):
    p=-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] < arr[i+1]:
            p = i
            break
    if p==-1:
        return sorted(arr)
    for i in range(len(arr)-1,p,-1):
        if arr[i] > arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
            break
    i, j = p+1, len(arr)-1
    while i <j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr

L = [3,2,1]
ans = next_permu(L)
print(ans)