# Brute force = Find all triplets and then return those whose sum is = provided O(n^3 * log(triplets) )
# Better = Using concept of 2 sum approach O(n^2 * log(triplets)) O(unique triplets + n)

# Best optimised (Two pointers approach)     TC = O(n^2) SC = O(unique triplets)
def three_sum(arr,tar): 
    trip = []
    arr.sort()
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue

        st, end = i+1, len(arr)-1
        while st < end:
            sum = arr[i] + arr[st] + arr[end]
            if sum < tar:
                st += 1
            if sum > tar:
                end -= 1
            if sum == tar:
                trip.append([arr[i],arr[st],arr[end]])
                st += 1
                end -= 1
                while st < end and arr[st] == arr[st-1]:
                    st += 1
    return trip
    
L = [-1,0,1,2,-1,-4]
ans = three_sum(L,0)
print(ans)