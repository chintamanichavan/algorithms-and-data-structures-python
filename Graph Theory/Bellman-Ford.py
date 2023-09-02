def bellman_ford(graph, source):
  """
  Computes shortest paths from the source vertex to all of the other vertices in the graph.

  Args:
    graph: The graph.
    source: The source vertex.

  Returns:
    A list of shortest paths from the source vertex to all of the other vertices.
  """

  # Initialize the distances to infinity.
  distances = [float("inf")] * len(graph)
  distances[source] = 0

  # Relax edges repeatedly.
  for _ in range(len(graph) - 1):
    for u, v, w in graph.edges:
      if distances[u] + w < distances[v]:
        distances[v] = distances[u] + w

  # Check for negative weight cycles.
  for u, v, w in graph.edges:
    if distances[u] + w < distances[v]:
      raise ValueError("Graph contains a negative weight cycle.")

  return distances
