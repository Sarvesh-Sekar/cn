import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance
        self.routing_table[neighbor.name] = distance

    def update_distance_vector(self):
        for neighbor, distance in self.neighbors.items():
            for destination, neighbor_dist in neighbor.routing_table.items():
                new_distance = distance + neighbor_dist
                if destination not in self.routing_table or new_distance < self.routing_table[destination]:
                    self.routing_table[destination] = new_distance

    def display_routing_table(self, algorithm):
        print(f"Routing table for {self.name} ({algorithm}):")
        for destination, distance in self.routing_table.items():
            print(f"Destination: {destination}, Distance: {distance}")
        print()

class Network:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)
        self.nodes[u].add_neighbor(self.nodes[v], weight)
        self.nodes[v].add_neighbor(self.nodes[u], weight)

    def distance_vector_routing(self, iterations=3):
        # Simulate routing table updates for final result
        for _ in range(iterations):
            for node in self.nodes.values():
                node.update_distance_vector()

        # Display final routing tables
        for node in self.nodes.values():
            node.display_routing_table("Distance Vector")

    def link_state_routing(self):
        for start in self.nodes:
            distances = self.dijkstra(start)
            print(f"Routing table for {start} (Link State):")
            for destination, distance in distances.items():
                print(f"Destination: {destination}, Distance: {distance}")
            print()

    def dijkstra(self, start):
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node].neighbors.items():
                distance = current_distance + weight
                if distance < distances[neighbor.name]:
                    distances[neighbor.name] = distance
                    heapq.heappush(priority_queue, (distance, neighbor.name))

        return distances

# Example usage
network = Network()
network.add_edge('A', 'B', 1)
network.add_edge('A', 'C', 4)
network.add_edge('B', 'C', 2)
network.add_edge('B', 'D', 5)
network.add_edge('C', 'D', 1)

print("Final Distance Vector Routing Table:")
network.distance_vector_routing()

print("\nFinal Link State Routing Table:")
network.link_state_routing()
