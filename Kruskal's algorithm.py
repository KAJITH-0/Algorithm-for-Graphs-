def kruskal(graph):
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        parent[root_u] = root_v

    mst = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u, v))

    return mst

# Test Case 1:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 5, 'C': 3}
}

result = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm) - Test Case 3:", result)
"""
test cases
graph1 = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 4},
    'C': {'A': 2, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}
"""
