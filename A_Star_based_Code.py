import time

# A* algorithm implementation
def a_star(graph, start, goal):
    # Initialize dictionaries to store distances, visited nodes, and parent nodes
    distances = {node: float("inf") for node in graph}  # Distance from start to each node (initialized to infinity)
    distances[start] = 0  # Distance from start to start is 0
    visited = {node: False for node in graph}  # Keeps track of visited nodes
    parent = {node: None for node in graph}  # Stores the parent node for each node in the optimal path

    while True:
        # Find the node with the lowest distance that has not been visited
        lowest_distance = float("inf")
        lowest_distance_node = None
        for node in graph:
            if distances[node] < lowest_distance and not visited[node]:
                lowest_distance = distances[node]
                lowest_distance_node = node

        # If there are no more unvisited nodes or the goal is reached, exit the loop
        if lowest_distance_node is None or lowest_distance_node == goal:
            break

        visited[lowest_distance_node] = True  # Mark the current node as visited

        # Update the distances of neighboring nodes
        for neighbor in graph[lowest_distance_node]:
            if graph[lowest_distance_node][neighbor] > 0 and not visited[neighbor]:
                distance = graph[lowest_distance_node][neighbor]
                new_distance = distances[lowest_distance_node] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parent[neighbor] = lowest_distance_node

    # If no path to the goal is found, return an error code and None
    if distances[goal] == float("inf"):
        return 3, None

    # Reconstruct the optimal path from start to goal
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()

    # Return success code, distance to the goal, and the optimal path
    return 0, distances[goal], path


# Read the map file and create an accessible map
def read_text_file(file_path):
    accessible_map = {}  # Dictionary to store the accessible map

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # Process each line in the file
            for line in lines:
                data = line.strip().split()

                if len(data) == 3:
                    city = data[0].strip()
                    x = int(data[1])
                    y = int(data[2])
                    accessible_map[city] = {"x": x, "y": y, "connections": {}}
                elif len(data) == 2:
                    connection = data[0].strip()
                    distance = int(data[1])
                    accessible_map[city]["connections"][connection] = distance

    except FileNotFoundError:
        return 2, None  # Return error code and None if file not found

    # Return success code and the accessible map
    return 0, accessible_map


# Get input for departure and arrival cities
def get_city_input(accessible_map):
    while True:
        start = input("Enter the departure city: ").strip()
        goal = input("Enter the arrival city: ").strip()

        # Check if the input cities are valid
        if start not in accessible_map:
            print(f"Error: '{start}' is not a valid city.")
            return 1, None, None
        elif goal not in accessible_map:
            print(f"Error: '{goal}' is not a valid city.")
            return 1, None, None
        else:
            return 0, start, goal


# Get the map file from the user
def get_map_file():
    # Prompt the user for the map file
    map_file = input("Enter the map file (default: FRANCE.MAP): ").strip()
    if map_file == "":
        map_file = "FRANCE.MAP"
    return map_file


# Print the shortest path and corresponding distances
def print_path_distance(distances, path):
    # Print the shortest path and the corresponding distances for each city
    print("Shortest path:")
    for i, city in enumerate(path):
        print(city, ":", "(" + str(distances[i]) + " km)")


# Get user input for the map file
file_path = get_map_file()

# Call the function to read the text file and get the accessible map
status, accessible_map = read_text_file(file_path)

# Check if the map file is valid
if status == 2:
    print("Error: Map file not found.")
    exit(2)

# Get user input for departure and arrival cities
status, start, goal = get_city_input(accessible_map)

if status == 1:
    print("Error: Invalid city names.")
    exit(1)

# Define the adjacency dictionary representation of the graph
graph = {}
locations = list(accessible_map.keys())
for location in locations:
    graph[location] = {}
    connections = accessible_map[location]['connections']
    for connection, distance in connections.items():
        graph[location][connection] = distance

# Test the A* algorithm and measure execution time
start_time = time.time()
status, distance, path = a_star(graph, start, goal)
execution_time = time.time() - start_time

if status == 3:
    print("Error: No path found.")
    exit(3)

# Calculate the distances for each city in the path
distances = {}
current_distance = 0
for i in range(len(path)):
    distances[i] = current_distance
    if i < len(path) - 1:
        current_distance += graph[path[i]][path[i + 1]]

# Calculate the space complexity
branching_factor = len(accessible_map)  # Average number of unexplored, adjoining vertices
solution_depth = len(path) - 1  # Depth of the shortest path to a solution
space_complexity = branching_factor * solution_depth

# Display the shortest path and corresponding distances
print_path_distance(distances, path)

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
