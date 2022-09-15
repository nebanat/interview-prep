def dijsktra(graph, current_vertex):
    INF = float('infinity')
    unvisited_min_distance = {vertex: INF for vertex in graph}
    visited_vertices = {}
    # current_vertex = "U"
    unvisited_min_distance[current_vertex] = 0

    while len(unvisited_min_distance) > 0:
        # get the vertex with the minimum distance
        current_vertex = min(unvisited_min_distance, key=unvisited_min_distance.get)
        # get the distance of the current vertex
        for neighbour, distance in graph[current_vertex].items():
            if neighbour not in visited_vertices:
                new_distance = unvisited_min_distance[current_vertex] + distance
                if unvisited_min_distance[neighbour] > new_distance:
                    unvisited_min_distance[neighbour] = new_distance
        visited_vertices[current_vertex] = unvisited_min_distance[current_vertex]
        unvisited_min_distance.pop(current_vertex)
    return visited_vertices

if __name__ == "__main__":
    graph = {
        "U": {"V": 6, "W": 7},
        "V": {"U": 6, "X": 10 },
        "W": {"U": 7, "X": 1},
        "X": {"W": 1, "V": 10},
    }
    print(dijsktra(graph, "U"))
