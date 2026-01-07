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
    
g = graph(6)
g.add_edge(0,1,2)
g.add_edge(0,2,4)
g.add_edge(1,2,1)
g.add_edge(1,3,7)
g.add_edge(2,4,3)
g.add_edge(3,5,1)
g.add_edge(4,3,2)
g.add_edge(4,5,5)
g.print_graph()
d = g.dijkhstra(0)
print(d)