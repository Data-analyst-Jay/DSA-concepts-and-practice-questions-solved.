# Better (prefix array approach)
# TC: O(n)
# SC: O(n)
def max_rw(height):
    lmax = [0] * len(height)
    rmax = [0] * len(height)
    lmax[0] = height[0]
    rmax[-1] = height[-1]
    for i in range(1, len(height)):
        lmax[i] = max(lmax[i-1], height[i])
    for i in range(len(height)-2, -1, -1):
        rmax[i] = max(rmax[i+1], height[i])
    ans = 0
    for i in range(len(height)):
        ans += min(lmax[i], rmax[i]) - height[i]
    return ans

h = [4,2,0,3,2,5]
print(max_rw(h)) # Output: 9

# Optimized (Two pointer approach)
# TC: O(n)
# SC: O(1)

def max_rw2(height):
    ans = 0
    lmax = 0
    rmax = 0
    l = 0
    r = len(height) - 1
    while l<r:
        lmax = max(lmax, height[l])
        rmax = max(rmax, height[r])
        if lmax < rmax:
            ans += lmax - height[l]
            l += 1
        else:
            ans += rmax - height[r]
            r -= 1
    return ans