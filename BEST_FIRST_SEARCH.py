from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        self.graph.setdefault(node, []).append((neighbor, cost))

    def best_first_search(self, start_node, goal_node, heuristic):
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((heuristic(start_node, goal_node), start_node))

        while not priority_queue.empty():
            current_cost, current_node = priority_queue.get()

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)

                if current_node == goal_node:
                    print("Goal node reached!")
                    return

                neighbors = self.graph.get(current_node, [])
                for neighbor, cost in neighbors:
                    if neighbor not in visited:
                        priority_queue.put((heuristic(neighbor, goal_node), neighbor))

# Example usage:
g = Graph()
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(2, 5, 5)
g.add_edge(3, 6, 8)

start_node = 1
goal_node = 6

# A simple heuristic function (straight-line distance between nodes)
def heuristic(node, goal_node):
    # Replace this with a more appropriate heuristic for your problem
    return abs(node - goal_node)

print(f"Best-First Search from {start_node} to {goal_node}:")
g.best_first_search(start_node, goal_node, heuristic)
