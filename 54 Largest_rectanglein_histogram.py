def lrh(heights):
    ans = 0
    n = len(heights)
    l = lsn(heights)
    r = rsn(heights)
    for i in range(n):
        curr = heights[i] * (r[i] - l[i] - 1)
        ans = max(ans, curr)
    return ans

def rsn(arr):
    s = []
    right = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        while len(s)>0 and arr[s[-1]] >= arr[i]:
            s.pop()
        if len(s) == 0:
            right[i] = len(arr)
        else:
            right[i] = s[-1]
        s.append(i)
    return right

def lsn(arr):
    s = []
    left = [0] * len(arr)
    for i in range(len(arr)):
        while len(s)>0 and arr[s[-1]] >= arr[i]:
            s.pop()
        if len(s) == 0:
            left[i] = -1
        else:
            left[i] = s[-1]
        s.append(i)
    return left

h = [2,1,5,6,2,3]
print(lrh(h)) # 10