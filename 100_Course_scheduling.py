#LC 207
def dfs(curr, vis, adj, reckstack):
    vis[curr] = True
    reckstack[curr] = True
    for neighbor in adj[curr]:
        if not vis[neighbor]:
            if dfs(neighbor, vis, adj, reckstack):
                return True
        elif reckstack[neighbor]:
            return True
    reckstack[curr] = False
    return False

def course_scheduling(numCourses, pre_requisites):
    adj = [[] for _ in range(numCourses)]
    for u, v in pre_requisites:
        adj[v].append(u)

    vis = [False] * numCourses
    reckstack = [False] * numCourses

    for node in range(numCourses):
        if not vis[node]:
            if dfs(node, vis, adj, reckstack):
                return False
    return True