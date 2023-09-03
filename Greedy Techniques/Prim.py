import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        min_cost = 0
        min_heap = [(0, 0)]  # (weight, vertex)
        visited = [False] * self.V

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += weight

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))

        return min_cost


# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst_cost = g.prim_mst()
print("Minimum Spanning Tree Cost:", mst_cost)
