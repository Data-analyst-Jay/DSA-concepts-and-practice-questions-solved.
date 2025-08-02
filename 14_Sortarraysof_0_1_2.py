# Optimal approach
def sorting(l):
    count = [0 for _ in range(max(l)+1)]
    sorted_array = []
    for i in range(len(l)):
        count[l[i]] += 1
    for i in range(len(count)):
        while count[i] != 0:
            sorted_array.append(count.index(count[i]))
            count[i] -= 1
    # return count
    return sorted_array
arr = [0,0,2,1,2,0,1,0,1,0,2,0]
# ans = sorting(arr)
# print(ans)

# Dutch national flag algorithm O(n) O(1) Vision algorithm
def DNFA(arr):
    low, mid, high = 0, 0, len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        if arr[mid] == arr[mid-1] and mid != 0:
            mid += 1
    return arr
l = [0,0,1,1,2,2]
ans = DNFA(l)
print(ans)

# My way
def sort_arr(arr):
    z, o, t = 0, 0, 0
    for i in arr:
        if i==0:
            z += 1
        elif i==1:
            o += 1
        else:
            t += 1
    for i in range(z):
            arr[i] = 0
    for j in range(o):
        arr[j+z] = 1
    for k in range(t):
        arr[k+z+o] = 2
    return arr