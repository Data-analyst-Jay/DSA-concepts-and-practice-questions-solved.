# LC = 200

def dfs(i, j, vis, grid, n, m):
    if i < 0 or j<0 or i>=n or j>=m or vis[i][j] or grid[i][j] == '0':
        return
    vis[i][j] = True
    dfs(i, j-1, vis, grid, n, m)
    dfs(i-1, j, vis, grid, n, m)
    dfs(i, j+1, vis, grid, n, m)
    dfs(i+1, j, vis, grid, n, m)

def numIslands(grid):
    if not grid:
        return 0
    n,m = len(grid), len(grid[0])
    num = 0
    vis = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not vis[i][j] and grid[i][j] == '1':
                dfs(i, j, vis, grid, n, m)
                num += 1
    return num

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(numIslands(grid))