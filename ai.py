graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2', '8'],
    '5': ['2', '8'],
    '6': ['3', '8'],
    '7': ['3', '8'],
    '8': ['4', '5', '6', '7']
}

def dfs_path_finder(graph, current_node, goal_node, visited, path):
    
    visited.add(current_node)
    path = path + [current_node]

    
    if current_node == goal_node:
        return path

    
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            
            result_path = dfs_path_finder(graph, neighbor, goal_node, visited, path)
            
            
            if result_path:
                return result_path

    
    return None

def main():
    start_node = '1'
    goal_node = '8'
    
    visited = set()
    initial_path = []

    print("--- Depth-First Search Path Finding ---")
    print(f"Start Node: {start_node}")
    print(f"Goal Node: {goal_node}")
    
    found_path = dfs_path_finder(graph, start_node, goal_node, visited, initial_path)

    if found_path:
        
        print("\nPath Found:")
        print(" -> ".join(found_path))
    else:
        print(f"\nNo path found from {start_node} to {goal_node}.")

if __name__ == '__main__':
    main()
