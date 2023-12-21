# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:24:59 2023

@author: kajit
"""

def bfs(graph, start_node):
    visited = set()  
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph1 = {
    'L': ['M', 'N'],
    'M': ['L', 'N', 'O'],
    'N': ['L', 'M', 'O'],
    'O': ['M', 'N']
}




bfs(graph1, 'N') 
  



