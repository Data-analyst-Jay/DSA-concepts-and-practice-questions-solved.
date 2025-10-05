class graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)


def dfs(adj, node, vis, stack):
    vis.add(node)
    for neighbor in adj[node]:
        if neighbor not in vis:
            dfs(adj, neighbor, vis, stack)
    stack.append(node)

def topological_sorting(g):
    vis = set()
    stack = []
    for i in range(g.vertices):
        if i not in vis:
            dfs(g.graph, i, vis, stack)
        
    return stack[::-1]

g = graph(6)
g.add_edge(5,2)
g.add_edge(5,0)
g.add_edge(4,0)
g.add_edge(4,1)
g.add_edge(2,3)
g.add_edge(3,1)

print(topological_sorting(g.graph))