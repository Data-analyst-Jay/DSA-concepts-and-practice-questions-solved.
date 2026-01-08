class graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v,w))

    def print_graph(self):
        for i in range(self.vertices):
            print(f'vertex {i}:', end='')
            for j in range(len(self.graph[i])):
                print(f'-> {self.graph[i][j]}', end=' ')
            print('\n')
    
    def dijkhstra(self, src):
        import heapq
        distances = [float('inf')] * self.vertices
        distances[src] = 0
        priority_queue = [(0, src)]  # (distance, vertex)

        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)

            if current_distance > distances[u]:
                continue

            for v, weight in self.graph[u]:
                distance = current_distance + weight

                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(priority_queue, (distance, v))

        return distances
    
    def bellman_ford(self, src):
        import heapq
        dist = [float('inf')]*self.vertices
        dist[src] = 0
        for _ in range(self.vertices - 1):
            for u in range(self.vertices):
                for v, w in self.graph[u]:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        return dist
    
g = graph(5)
g.add_edge(0,1,2)
g.add_edge(0,2,4)
g.add_edge(1,2,-4)
g.add_edge(1,4,-1)
g.add_edge(2,3,2)
g.add_edge(3,4,4)
g.print_graph()
d = g.bellman_ford(0)
print(d)