from collections import deque

class graph_bfs():
    def bfs(self,graph, start_node):
        queue = deque([start_node])
        visited = set([start_node])

        while queue:
            current_node = queue.popleft()
            print(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
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
    b = graph_bfs()
    b.bfs(graph, start_node)

if __name__ == '__main__':
    main()



