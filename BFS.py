from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        self.graph.setdefault(node, []).append(neighbor)

    def bfs(self, start_node, goal_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)

                if current_node == goal_node:
                    print("Goal node reached!")
                    return

                neighbors = self.graph.get(current_node, [])
                queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

start_node = 1
goal_node = 6

print(f"BFS from {start_node} to {goal_node}:")
g.bfs(start_node, goal_node)
