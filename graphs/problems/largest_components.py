def largestComponents(graph):
    longest = 0
    visited = {}

    for node in list(graph.keys()):
        size = explore_size(graph, node, visited)

        if size > longest:
            longest = size
    return longest
        


def explore_size(graph, current, visited):
    # node_count = 0
    if current in visited:
        return 0
    
    visited[current] = True
    size = 1


    for neighbor in graph[current]:
        size += explore_size(graph, neighbor, visited)

    return size

if __name__ == '__main__':
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]

    }
    print(largestComponents(graph))

