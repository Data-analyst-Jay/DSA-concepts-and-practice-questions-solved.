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
    
    def _dfs_util(self, u, vis, par):
        par = u
        vis[u] = True
        # print(u, end=' ')
        for v in self.graph[u]:
            if not vis[v]:
                if self._dfs_util(v, vis, par):
                    return True
            elif v != par:
                return True
        return False


    def dfs_cycle(self):
        start = 0
        par = None
        vis = [False] * self.vertices
        for i in range(self.vertices):
            if not vis[i]:
                return (self._dfs_util(start, vis, par))

g = graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,2)
g.add_edge(3,4)
# g.print_graph()
print(g.dfs_cycle())