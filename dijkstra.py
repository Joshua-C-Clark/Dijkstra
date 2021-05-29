from collections import defaultdict 
import heapq

class Graph:
    
    
    def __init__(self, V):
        '''
        Instantiate the Graph with the number of vertices of the graph.
        '''
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, w):
        '''
        The Graph will be undirected and assumed to have positive weights.
        Dijkstra's algorithm fails when negative weights are introduced.
        '''
        self.graph[u].append([v, w])
        self.graph[v].append([u,w])

    def minDistance(self, dist, seen):
        min_d = float('inf')

        for v in range(self.V):
            if v not in seen and dist[v] < min_d:
                min_d = dist[v]
                min_vertex = v
        return min_vertex
    
    def slow_dijkstra(self,source):
        dist = [float('inf')] * self.V
        seen = set()
        dist[source] = 0

        for _ in range(self.V):
            u = self.minDistance(dist, seen)
            seen.add(u)

            for node, weight in self.graph[u]:
                if node not in seen and dist[node] > dist[u] + weight:
                    dist[node] = dist[u] + weight

        self.printSolution(dist)


    def dijkstra(self, source):
        dist = [float('inf')] * self.V
        seen = set()
        heap = []
        dist[source] = 0

        heapq.heappush(heap, (source, dist[source]))

        while len(heap) > 0:
            node, weight = heapq.heappop(heap)
            seen.add(weight)

            for conn, w in self.graph[node]:
                if conn not in seen:
                    d = weight + w
                    if d < dist[conn]:
                        dist[conn] = d
                        heapq.heappush(heap, (conn, d))

        self.printSolution(dist)
    
    def printGraph(self):
        print(self.graph)

    def printSolution(self, dist):
        print('Vertex: \tDistance:')
        for node in range(self.V):
            print(node+1, '\t\t\t', dist[node])

G = Graph(6)
G.addEdge(0,1,7)
G.addEdge(0,2,9)
G.addEdge(0,5,14)
G.addEdge(1,2,10)
G.addEdge(2,5,2)
G.addEdge(3,2,11)
G.addEdge(1,3,15)
G.addEdge(5,4,9)
G.addEdge(3,4,6)
G.dijkstra(0)
# G.slow_dijkstra(0)
# G.printGraph()