#O(n*k) time complexity
def swm(nums, k):
    ans = []
    for i in range(len(nums)):
        if i+k<len(nums):
            ans.append(max(nums[i:i+k]))
    ans.append(max(nums[len(nums)-k:len(nums)]))
    print(ans)

a = [1,3,-1,-3,5,3,6,7]
# swm(a,3)

# O(n) time complexity

class doubly_queue:
    def __init__(self):
        self.q = []
    
    def enqueue_back(self,value):
        self.q.append(value)
        
    def enqueue_front(self,value):
        self.q.insert(value,0)
    
    def dequeue_front(self):         #O(1)
        if len(self.q) == 0:
            return ('Empty queue')
        return (self.q.pop(0))
        
    def dequeue_back(self):
        if len(self.q) ==0:
            return ('Empty Queue')
        return (self.q.pop())

    def front(self):
        if len(self.q) == 0:
            print('Queue is empty')
        return self.q[0]

    def back(self):
        if len(self.q) == 0:
            print('Queue is empty')
        return self.q[-1]

    def print_queue(self):       #O(n)
        for i in self.q:
            print(self.q[i], end='-->')
        print(self.q[0])

    def is_empty(self):          #O(1)
        if len(self.q)==0:
            return True
        else:
            return False

def swmo(nums, k):
    Q = doubly_queue()
    ans = []
    for i in range(0,k):
        while (not Q.is_empty() and nums[Q.back()]<= nums[i]):
            Q.dequeue_back()
        Q.enqueue_back(i)
    
    for i in range(k,len(nums)):
        ans.append(nums[Q.front()])
    
        while not Q.is_empty() and Q.front() <= i-k:
            Q.dequeue_front()
    
        while not Q.is_empty() and nums[Q.back()] <= nums[i]:
            Q.dequeue_back()
    
        Q.enqueue_back(i)

    ans.append(nums[Q.front()])
    return ans

b = [1,3,1,2,0,5]
print(swmo(b,3))