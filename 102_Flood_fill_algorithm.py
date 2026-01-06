# LC 733

def dfs(graph, i, j, n, m, original_color, new_color):
    if i<0 or j<0 or i>=n or j>=m or graph[i][j] != original_color:
        return
    graph[i][j] = new_color
    dfs(graph, i-1, j, n, m, original_color, new_color)
    dfs(graph, i, j+1, n, m, original_color, new_color)
    dfs(graph, i+1, j, n, m, original_color, new_color)
    dfs(graph, i, j-1, n, m, original_color, new_color)

def flood_fill(graph, sr, sc, new_color):
    if not graph:
        return graph
    original_color = graph[sr][sc]

    if original_color == new_color:
        return graph

    n,m = len(graph), len(graph[0])

    dfs(graph, sr, sc, n, m, original_color, new_color)
    
    return graph