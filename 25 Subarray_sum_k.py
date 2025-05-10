# Brute force approach (Sum of all subarrays) TC = O(n^2) | SC = O(1)
def sum_brute(arr,k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum == k:
                count+=1
    return count

# Optimised approach TC = O(n) & SC = O(n) # Prefix sum
def sum_opt(arr,k):
    pref_sum = [0 for _ in range(len(arr))]
    pref_sum[0] = arr[0]
    freq = dict()                               # {Pref_sum, freq}
    count = 0
    for i in range(1,len(arr)):
        pref_sum[i] = pref_sum[i-1] + arr[i]
    for j in range(len(arr)):
        if pref_sum[j] == k:
            count += 1
        val = pref_sum[j] - k
        if val in freq:
            count += freq[val]
        if val not in freq:
            freq[pref_sum[j]] = 0
            freq[pref_sum[j]] += 1
    return count

l = [1,2,1,2,1]
ans = sum_brute(l,3)
print(ans)