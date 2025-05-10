# T.C = O(nlogn + n^3)
# S.C = O(unique groups)
def four_sum(nums,tar):
    arr = sorted(nums)
    trip = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        while j < len(arr):
            p, q = j+1, len(arr)-1
            while p < q:
                sum = arr[i] + arr[j] + arr[p] + arr[q]
                if sum < tar:
                    p += 1
                elif sum > tar:
                    q -= 1
                else:
                    trip.append([arr[i], arr[j], arr[p], arr[q]])
                    p+=1
                    q-=1
                    while p < q and arr[p] == arr[p-1]:
                        p+=1
            j += 1
            while j < len(arr) and arr[j] == arr[j-1]:
                j+=1
    
    return trip

L = [2,2,2,2,2]
ans = four_sum(L,8)
print(ans)

# New way
def four_sum(arr,tar):
    arr.sort()
    trip = set()
    n = len(arr)
    for i in range(len(arr)):
        for j in range(i+1,n):
            p, q = j+1, len(arr)-1
            while p < q:
                sum = arr[i] + arr[j] + arr[p] + arr[q]
                if sum < tar:
                    p += 1
                elif sum > tar:
                    q -= 1
                else:
                    trip.add((arr[i], arr[j], arr[p], arr[q]))
                    p+=1
                    q-=1
    
    return list(trip)