from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

def main():
    start_node = 'A' 
    print("Depth-First Search Traversal:")
    visited = set()
    dfs(graph, start_node, visited)
    print() 

if __name__ == '__main__':
    main()
