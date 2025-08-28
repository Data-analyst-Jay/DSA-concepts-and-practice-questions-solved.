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
    
    def BFS(self, start):                                          #TC=O(V+E), SC=O(V)
        visited = [False] * self.vertices
        qu = []
        qu.append(start)
        visited[start] = True
        while qu:
            u = qu.pop(0)
            print(u, end=' ')
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    qu.append(v)

g = graph(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,2)

g.print_graph()
g.BFS(0)