def dfs(node, vis, graph, reckstack, stack):
    vis[node] = True
    reckstack[node] = True
    for neighbor in graph[node]:
        if not vis[neighbor]:
            if not dfs(neighbor, vis, graph, reckstack, stack):
                return False
        elif reckstack[neighbor]:
            return False
    reckstack[node] = False
    stack.append(node)
    return True

def course_scheduling(numCourses, pre_requisites):
    graph = [[] for _ in range(numCourses)]
    for u, v in pre_requisites:
        graph[v].append(u)

    vis = [False] * numCourses
    reckstack = [False] * numCourses
    stack = []

    for node in range(numCourses):
        if not vis[node]:
            if not dfs(node, vis, graph, reckstack, stack):
                return []
    
    return stack[::-1]