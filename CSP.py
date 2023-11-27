def is_safe(graph, vertex, color, c):
    return all(color[neighbor] != c for neighbor in graph[vertex])

def color_graph(graph, num_colors, color, vertex):
    if vertex == len(graph):
        return True

    for c in range(1, num_colors + 1):
        if is_safe(graph, vertex, color, c):
            color[vertex] = c
            if color_graph(graph, num_colors, color, vertex + 1):
                return True
            color[vertex] = 0  # Backtrack

    return False

def map_coloring(graph, num_colors):
    color = [0] * len(graph)

    if not color_graph(graph, num_colors, color, 0):
        print("Solution does not exist.")
        return

    print("Map Coloring Solution:")
    for i, c in enumerate(color, 1):
        print(f"Region {i}: Color {c}")

# Example usage:
graph = {0: [1, 4], 1: [0, 2, 4], 2: [1, 3], 3: [2, 4], 4: [0, 1, 3]}
num_colors = 3

map_coloring(graph, num_colors)
