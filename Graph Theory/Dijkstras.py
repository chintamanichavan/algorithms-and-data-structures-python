def dijkstra(graph, source):
  """
  Dijkstra's algorithm for finding the shortest paths between nodes in a graph.

  Args:
    graph: The graph to be searched.
    source: The node to start the search from.

  Returns:
    A dictionary mapping each node to its shortest distance from the source node.
  """

  # Initialize the distance to each node to infinity.
  distances = {node: float("inf") for node in graph}
  distances[source] = 0

  # Initialize a set of visited nodes.
  visited = set()

  # Iterate over the nodes in the graph.
  for node in graph:
    # If the node has not been visited, add it to the set of visited nodes and update its distance.
    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        distances[neighbor] = min(distances[neighbor], distances[node] + 1)

  # Return the dictionary mapping each node to its shortest distance from the source node.
  return distances
