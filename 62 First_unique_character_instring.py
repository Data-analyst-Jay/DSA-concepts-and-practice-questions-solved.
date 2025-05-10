class queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self,value):    #O(1)
        self.q.append(value)
    
    def dequeue(self):         #O(1)
        if len(self.q) == 0:
            print('Queue is empty')
        else:
            return(self.q.pop(0))

    def front(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            return(self.q[0])

    def print_queue(self):       #O(n)
        if len(self.q) == 0:
            print('Empty')
            return
        for i in self.q:
            print(i, end=' ')

    def is_empty(self):          #O(1)
        if len(self.q) == 0:
            return True
        else:
            return False

def firstUniqChar(s):
    q = queue()
    m = dict()
    for i in range(len(s)):
        if s[i] not in m:
            m[s[i]] = 1
            q.enqueue(i)
        else:
            m[s[i]] += 1
        while not q.is_empty() and m[s[q.front()]] > 1:
            q.dequeue()
    if q.is_empty():
        return -1
    else:
        return q.front()
    
str = 'level'
print(firstUniqChar(str))