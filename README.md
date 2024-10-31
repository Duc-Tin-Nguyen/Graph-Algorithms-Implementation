# Graph Algorithms Implementation

This repository contains implementations of two popular graph search algorithms: A* and Dijkstra's algorithm. These implementations are designed to find the shortest path between nodes in a graph, which is represented as a map of cities with distances between them.

## Contents

1. [A* Algorithm Implementation](#a-star-algorithm-implementation)
2. [Dijkstra's Algorithm Implementation](#dijkstras-algorithm-implementation)
3. [Complexity Analysis](#complexity-analysis)
4. [Usage](#usage)
5. [File Structure](#file-structure)

## A* Algorithm Implementation

The A* algorithm is implemented in Python and is designed to find the shortest path from a start node to a goal node in a graph. The implementation uses heuristics based on the distance to the goal to optimize the pathfinding process.

- **Source Code**: `A_Star_based_Code.py`
- **Main Function**: `a_star`
- **Complexity Analysis**: Refer to the document [Complexity of A_Star.txt](#complexity-analysis)

## Dijkstra's Algorithm Implementation

Dijkstra's algorithm is also implemented in Python. Unlike A*, it does not use heuristics and is generally used for finding the shortest paths from a single source node to all other nodes in the graph.

- **Source Code**: `Dijkstra_based_Code.py`
- **Main Function**: `dijkstra`
- **Complexity Analysis**: Refer to the document [Complexity of Dijkstra.txt](#complexity-analysis)

## Complexity Analysis

Detailed complexity analysis for both algorithms is provided in separate documents. These analyses include both time complexity and space complexity evaluations.

- **A* Algorithm**: [Complexity of A_Star.txt](Complexity%20of%20A_Star.txt)
- **Dijkstra's Algorithm**: [Complexity of Dijkstra.txt](Complexity%20of%20Dijkstra.txt)

## Usage

To use the implementations, you need to provide a map file in a specific format as detailed in the `FRANCE.MAP` file. The programs will prompt you for the start and goal cities, and then compute the shortest path using the selected algorithm.

### Running the Programs

1. **A* Algorithm**:
   ```bash
   python A_Star_based_Code.py
   ```
2. **Dijkstra's Algorithm**:
   ```bash
   python Dijkstra_based_Code.py
   ```

## File Structure

- **A_Star_based_Code.py**: Contains the implementation of the A* algorithm.
- **Dijkstra_based_Code.py**: Contains the implementation of Dijkstra's algorithm.
- **FRANCE.MAP**: Sample map file used by both algorithms to represent the graph.
- **Complexity of A_Star.txt**: Complexity analysis for the A* algorithm.
- **Complexity of Dijkstra.txt**: Complexity analysis for Dijkstra's algorithm.

For more details on the implementation and complexity analysis, refer to the respective source files and documentation.
