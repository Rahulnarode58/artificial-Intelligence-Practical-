class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        self.graph.setdefault(node, []).append(neighbor)

    def dfs(self, start_node, goal_node, visited=None):
        visited = visited or set()
        print(start_node)
        visited.add(start_node)

        if start_node == goal_node:
            print("Goal node reached!")
            return

        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, goal_node, visited)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

start_node = 1
goal_node = 6

print(f"DFS from {start_node} to {goal_node}:")
g.dfs(start_node, goal_node)
