import heapq

def prims(graph, vertices):
    pq = []
    inMST = [False]*vertices
    min_cost = 0

    heapq.heappush(pq, (0,0))

    while pq:
        wt, u = heapq.heappop(pq)

        if inMST[u] == False:
            inMST[u] = True
            min_cost += wt

            for i in graph[u]:
                heapq.heappush(pq, i)
    return min_cost