graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],  # Added a new vertex '6'
    '4': ['8'],
    '8': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("The Depth-First Search")
dfs(visited, graph, '5')


#Case 2
"dfs(visited, graph, '3')"

#Case 3
"dfs(visited, graph, '4')"



