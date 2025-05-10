class stack_l:
    def __init__(self):
        self.list = []
    
    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list[-1]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.list)
    
def nge(arr):
    s = stack_l()
    ans = []
    for i in range(len(arr)-1, -1, -1):
        while s.is_empty() == False and s.peek() <= arr[i]:
            s.pop()
        if s.is_empty():
            ans.append(-1)
        else:
            ans.append(s.peek())
        s.push(arr[i])
    return ans[::-1]
# Time complexity: O(2n)
# Space complexity: O(n)

def nge2(arr1,arr2):
    s = stack_l()
    d = dict()
    ans = []
    for i in range(len(arr2)-1, -1, -1):
        while s.is_empty() == False and s.peek() <= arr2[i]:
            s.pop()
        if s.is_empty():
            d[arr2[i]] = -1
        else:
            d[arr2[i]] = s.peek()
        s.push(arr2[i])
    
    for i in arr1:
        ans.append(d[i])

    return ans

a = [4,1,2]
b = [1,3,4,2]
print(nge2(a,b)) # [-1, 3, -1]