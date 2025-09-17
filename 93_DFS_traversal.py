# Keep going to 1st unvisited neighbor until you reach a dead end.
# TC = O(V+E), SC=O(V)

# This will work for disconnected graph as well.

class graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(v)
    
    def _dfs_util(self, u, vis):
        vis[u] = True
        print(u, end=' ')
        for v in self.graph[u]:
            if not vis[v]:
                self._dfs_util(v, vis)


    def dfs(self):
        vis = [False] * self.vertices
        for i in range(self.vertices):
            if not vis[i]:
                self._dfs_util(0, vis)

g = graph(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,2)

# g.print_graph()
g.dfs()