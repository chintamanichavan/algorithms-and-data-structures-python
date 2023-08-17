class graph_dfs():
    def dfs(self, graph, start_node):
        stack = [start_node]
        visited = set([start_node])

        while stack:
            current_node = stack.pop()
            print(current_node)

            for neighbor in graph[start_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    b = graph_dfs()
    b.dfs(graph, start_node)

if __name__ == '__main__':
    main()
