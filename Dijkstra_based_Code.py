import time

# Define a Hashtable class to store key-value pairs
class Hashtable:
    def __init__(self):
        self.table = []

    def add(self, key, value):
        # Append the key-value pair as a list to the table
        self.table.append([key, value])

    def get(self, key):
        # Iterate through the table to find the value associated with the given key
        for item in self.table:
            if item[0] == key:
                return item[1]
        # Return None if the key is not found in the table
        return None

    def remove(self, key):
        # Iterate through the table to find and remove the key-value pair with the given key
        for item in self.table:
            if item[0] == key:
                self.table.remove(item)

# Define a Graph class that uses the Hashtable class to represent a graph
class Graph:
    def __init__(self):
        # Create a Hashtable instance to store the graph data
        self.graph = Hashtable()

    def add_node(self, node):
        # Add a node to the graph if it doesn't already exist
        if not self.graph.get(node):
            self.graph.add(node, [])

    def add_edge(self, source, target, weight):
        # Add an edge between the source and target nodes with the given weight
        self.graph.get(source).append([target, weight])

    def get_neighbors(self, node):
        # Get the neighbors of a given node by retrieving its associated values from the hashtable
        for item in self.graph.table:
            if item[0] == node:
                return item[1]
        # Return an empty list if the node is not found in the graph
        return []

    def get_nodes(self):
        # Get all the nodes in the graph by extracting the keys from the hashtable
        nodes = []
        for item in self.graph.table:
            nodes.append(item[0])
        return nodes

# Define a Dijkstra class to perform Dijkstra's algorithm on a given graph
class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.dist = {}  # Store the shortest distance from the start node to each node
        self.back = {}  # Store the previous node in the shortest path

    def dijkstra(self, start, goal):
        inf = float('inf')
        open_list = [start]
        self.dist[start] = 0

        while open_list:
            # Find the node with the minimum distance from the start node
            cur = min(open_list, key=lambda x: self.dist.get(x, inf))
            open_list.remove(cur)
            if cur == goal:
                # If the current node is the goal, exit the loop
                break
            for n, d in self.graph.get_neighbors(cur):
                # Update the distances and previous nodes for the neighbors of the current node
                if self.dist.get(n, inf) > self.dist[cur] + d:
                    self.dist[n] = self.dist[cur] + d
                    open_list.append(n)
                    self.back[n] = cur

    def display_path(self, start, goal):
        path = []
        current = goal
        while current != start:
            # Reconstruct the shortest path by following the previous nodes
            path.append(current)
            current = self.back[current]
        path.append(start)
        path.reverse()

        # Display the shortest path and the distances
        print("Shortest path:")
        for city in path:
            distance = self.dist[city]
            print(f"{city}: ({distance} km)")

# Define a function to read the text file containing the map data
def read_text_file(file_path):
    accessible_map = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split()

                if len(data) == 3:
                    # If the line contains city data, add it to the accessible map
                    city, x, y = data
                    accessible_map.append([city, int(x), int(y), []])
                elif len(data) == 2:
                    # If the line contains connection data, add it to the last city in the accessible map
                    connection, distance = data
                    accessible_map[-1][-1].append([connection, int(distance)])

    except FileNotFoundError:
        # Return an error status and None if the file is not found
        return 2, None

    # Return a success status and the accessible map
    return 0, accessible_map

# Define a function to get user input for the departure and arrival cities
def get_city_input(accessible_map):
    while True:
        start = input("Enter the departure city: ").strip()
        goal = input("Enter the arrival city: ").strip()

        if not any(city[0] == start for city in accessible_map):
            # If the start city is not found in the accessible map, return an error status
            print(f"Error: '{start}' is not a valid city.")
            return 1, None, None
        elif not any(city[0] == goal for city in accessible_map):
            # If the goal city is not found in the accessible map, return an error status
            print(f"Error: '{goal}' is not a valid city.")
            return 1, None, None
        else:
            # Return a success status and the start and goal cities
            return 0, start, goal

# Define a function to get the map file from the user
def get_map_file():
    map_file = input("Enter the map file (default: FRANCE.MAP): ").strip() or "FRANCE.MAP"
    return map_file

# Get user input for the map file
file_path = get_map_file()

# Call the function to read the text file and get the accessible map
status, accessible_map = read_text_file(file_path)

# Check if the map file is valid
if status == 2:
    print("Error: Map file not found.")
    exit(2)

# Get user input for city names
status, start, goal = get_city_input(accessible_map)

if status == 1:
    print("Error: Invalid city names.")
    exit(1)

# Create a Graph instance
graph = Graph()

# Add nodes and edges to the graph
for city_data in accessible_map:
    city = city_data[0]
    graph.add_node(city)
    for connection, distance in city_data[3]:
        graph.add_edge(city, connection, distance)

# Create a Dijkstra instance
dijkstra = Dijkstra(graph)

# Calculate the time complexity
start_time = time.time()
dijkstra.dijkstra(start, goal)
end_time = time.time()
execution_time = end_time - start_time

# Check if there is a path between the start and goal cities
if goal not in dijkstra.back:
    print("Error: No path found between the cities.")
    exit(3)

# Calculate the space complexity
branching_factor = len(accessible_map)  # Average number of unexplored, adjoining vertices
solution_depth = dijkstra.dist[goal]  # Depth of the shortest path to a solution
space_complexity = branching_factor * solution_depth

# Display the shortest path
dijkstra.display_path(start, goal)

# Display the time and space complexity
print("Time complexity: O(bd)")
print(f"  - Branching factor (b): {branching_factor}")
print(f"  - Solution depth (d): {solution_depth}")
print(f"  - Execution time: {execution_time} seconds")
print("Space complexity: O(bd)")
print(f"  - Branching factor (b): {branching_factor}")
print(f"  - Solution depth (d): {solution_depth}")
print(f"  - Space complexity: {space_complexity} units")

exit(0)
