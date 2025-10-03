# LC: 994

def rotting_orange(grid):
    if not grid or grid == [[1]]:
        return -1
    n, m = len(grid), len(grid[0])
    q = []
    vis = [[False for _ in range(m)] for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
                vis[i][j] = True
    
    while q:
        k = q.pop(0)
        i, j, t = k[0], k[1], k[2]
        ans = max(ans, t)
        if i-1 >= 0 and not vis[i-1][j] and grid[i-1][j] ==1:
            q.append((i-1, j, t+1))
            vis[i-1][j] = True
        if j+1 < m and not vis[i][j+1] and grid[i][j+1] == 1:
            q.append((i, j+1, t+1))
            vis[i][j+1] = True
        if i+1 < n and not vis[i+1][j] and grid[i+1][j] == 1:
            q.append((i+1, j, t+1))
            vis[i+1][j] = True
        if j-1 >= 0 and not vis[i][j-1] and grid[i][j-1] == 1:
            q.append((i, j-1, t+1))
            vis[i][j-1] = True

    for i in range(n):
        for j in range(m):
            if grid[i][j] ==1 and not vis[i][j]:
                return -1
    return ans 

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(rotting_orange(grid))