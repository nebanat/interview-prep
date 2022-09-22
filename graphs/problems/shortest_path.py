from xml.etree.ElementTree import TreeBuilder


def buildGraph(edges):
    graph = {}

    for edge in edges:
        # check if we have add the edge to the graph 
        e1, e2 = edge 
        if not e1 in graph:
            graph[e1] = []
        if not e2 in graph:
            graph[e2] = []
        graph[e1].append(e2)
        graph[e2].append(e1)
    return graph

def shortestPath(edges, start, end):
    graph = buildGraph(edges)
    visited = {start: True}
    queue = [(start, 0)]

    while len(queue) > 0:
        cur_node, distance = queue.pop(0)

        if cur_node == end:
            return distance
        
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    return - 1