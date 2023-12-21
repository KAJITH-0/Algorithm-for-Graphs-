# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:22:09 2023

@author: kajit
"""

v = 5
INF = 999999

def floyd_warshall(G):
    distance = [list(map(lambda j: j, i)) for i in G]

    # Adding vertices individually
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

# Printing the solution
def print_solution(distance):
    for i in range(v):
        for j in range(v):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

print("The shortest distances between every pair of vertices ")

# Example 1
G1 = [
    [0, 2, INF, 6, INF],
    [2, 0, 3, 8, 5],
    [INF, 3, 0, INF, 7],
    [6, 8, INF, 0, 9],
    [INF, 5, 7, 9, 0]
]

floyd_warshall(G1)

"""# Example 2
G2 = [
    [0, 4, INF, 6, INF],
    [4, 0, INF, 8, 5],
    [INF, 7, 0, INF, 2],
    [6, 8, INF, 0, 9],
    [INF, 5, 2, 9, 0]
]

floyd_warshall(G2)
"""
