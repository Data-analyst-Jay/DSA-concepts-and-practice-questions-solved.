# Two sum brute force O(n^2)
def two_sum_brute(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                return (arr[i],arr[j])
    return -1


def two_sum_better(arr,sum): # O(nlogn)
    s_arr = sorted(arr)
    s = 0
    st, end = 0, len(arr)-1
    while st < end:
        if arr[st] + arr[end] == sum:
            return (arr[st],arr[end])
        elif arr[st] + arr[end] < sum:
            st += 1
        else:
            end -= 1

def two_sum_best(arr,sum):      # Concept of hashing O(n)
    dic = {}
    for i in range(len(arr)):
        first = arr[i]
        sec = sum - first
        if sec in dic:
            return (i, arr.index(sec))
        dic[first] = i

# Repeating or missing values

def rep_mis(arr):
    l = len(arr)
    set = []
    ans = []
    actual_sum = 0
    for i in arr:
        for j in i:
            if j in set:
                ans.append(j)
            set.append(j)
            actual_sum += j
    exp_sum = ((l**2)*(l**2 + 1))/2
    b = exp_sum + ans[0] - actual_sum
    ans.append(b)
    return ans

# Repeating value in arr[1,n] size = n+1
# Not necessary for all the values to present
def r_repeat(arr):          #Slow and fast pointer approach(Linked list)
    slow, fast = arr[arr[0]], arr[arr[arr[0]]]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = arr[0]
    while slow!=fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

l = [3,1,4,4,2]
ans = r_repeat(l)
print(ans)