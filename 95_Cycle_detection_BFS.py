# Keep going to all unvisited neighbors at the present depth prior to moving on to nodes at the next depth level.

class graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if u not in self.graph[v]:
            self.graph[v].append(u)
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def print_graph(self):
        for i in range(self.vertices):
            print(f'vertex {i}:', end='')
            for j in range(len(self.graph[i])):
                print(f'-> {self.graph[i][j]}', end=' ')
            print('\n')
    
    def BFS_cycle(self, start):                                          #TC=O(V+E), SC=O(V)
        par = [None]*self.vertices
        visited = [False] * self.vertices
        qu = []
        qu.append(start)
        visited[start] = True
        while qu:
            u = qu.pop(0)
            # print(u, end=' ')
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    par[v] = u
                    qu.append(v)
                elif par[u] != v:
                    return True
        return False

g = graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,0)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,1)
g.add_edge(3,0)
g.add_edge(3,4)
g.add_edge(4,3)

# g.print_graph()
print(g.BFS_cycle(0))