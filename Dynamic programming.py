# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:15:24 2023

@author: kajit
"""

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        # Step 1: Initialize distances and predecessors
        distances = {vertex: float('inf') for vertex in range(self.vertices)}
        predecessors = {vertex: None for vertex in range(self.vertices)}
        distances[source] = 0

        # Step 2: Relax edges repeatedly
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

        # Step 3: Check for negative cycles
        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

        return distances, predecessors


# Modified Example usage:
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 1)
g.add_edge(1, 3, -2)
g.add_edge(2, 1, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 5, 3)
g.add_edge(4, 3, 6)
g.add_edge(5, 0, 7)
g.add_edge(5, 4, -1)

# Change the source vertex for testing
source_vertex = 2
distances, predecessors = g.bellman_ford(source_vertex)

print("Shortest distances from source vertex", source_vertex)
for vertex in range(g.vertices):
    print(f"Vertex {vertex}: Distance = {distances[vertex]}, Predecessor = {predecessors[vertex]}")
