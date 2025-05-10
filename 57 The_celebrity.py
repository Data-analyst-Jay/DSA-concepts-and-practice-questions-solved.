# TC : O(n) SC : O(n)
def celebrity(arr):
    n = len(arr)
    stack = []
    for i in range(n):
        stack.append(i)
    while len(stack) > 1:
        i = stack.pop()
        j = stack.pop()
        if arr[i][j] == 1:
            stack.append(j)
        else:
            stack.append(i)
    celeb = stack.pop()
    for i in range(n):
        if i != celeb and (arr[celeb][i] == 1 or arr[i][celeb] == 0):
            return -1
    return celeb

a = [[0,0,0],[1,0,0],[1,0,0]]
print(celebrity(a)) # 1