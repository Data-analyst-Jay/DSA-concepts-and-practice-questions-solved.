def topological_sorting_kahn(graph):
    from collections import deque
    # calculating indegrees
    indegree = {u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    # queue for nodes with indegree 0
    queue = deque([u for u in graph if indegree[u] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    if len(topo_order) == len(graph):
        return topo_order
    else:
        return []  # Graph has a cycle, topological sorting not possible