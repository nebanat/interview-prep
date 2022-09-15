### Dijkstra's algorithms

- It is optimal
- Used to find the shortest path between two nodes in a graph
- Uses greedy approach 
- Weights must be positive to guarantee correct results
- It finds the shortest path to every node from the starting node

### Algorithm workthrough

- Create a set of nodes that have been visited
- Create a set of nodes that have not been visited
- Assign a distance of 0 to the starting node
- Assign a distance of infinity to all other nodes
- While there are nodes that have not been visited
    - Select the unvisited node with the smallest distance
    - For the current node, consider all of its unvisited neighbours
    - Calculate the distance to each neighbour
    - If the distance to the neighbour is less than the current distance, update the distance
    - When we are done considering all of the neighbours, mark the current node as visited