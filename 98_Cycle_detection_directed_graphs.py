def dfs(curr, vis, adj, recStack):
    vis[curr] = True
    recStack[curr] = True

    for neighbor in adj[curr]:
        if not vis[neighbor]:
            if dfs(neighbor, vis, adj, recStack):
                return True
        elif recStack[neighbor]:
            return True

    recStack[curr] = False
    return False

def iscycle(veritices, adj):
    vis = [False] * veritices
    recStack = [False] * veritices

    for node in range(veritices):
        if not vis[node]:
            if dfs(node, vis, adj, recStack):
                return True
    return False
