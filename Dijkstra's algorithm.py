


intmax = 9999999999  # assuming inf
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t\t ", dist[node], "\n")

    def minDistance(self, dist, sptSet):
        min_val = intmax
        min_index = -1

        for u in range(self.V):
            if dist[u] < min_val and not sptSet[u]:
                min_val = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        dist = [intmax] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if (
                    self.graph[x][y] > 0
                    and not sptSet[y]
                    and dist[y] > dist[x] + self.graph[x][y]
                ):
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)


# Updated example with 5 vertices
g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

# Perform Dijkstra's algorithm
source_vertex = 0
g.dijkstra(source_vertex)
"""graph = [
    [0, 2, 5, 0, 0],
    [2, 0, 1, 3, 0],
    [5, 1, 0, 4, 8],
    [0, 3, 4, 0, 2],
    [0, 0, 8, 2, 0]
]
    """
