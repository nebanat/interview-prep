import pprint

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

def hasPath(graph, src, dst, visited=set()):
    if src in visited:
        return False

    if src == dst:
        return True
    
    visited.append(src)
    
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited):
            return True
    return False

def hasPathIterative(graph, src, dst):
    # initialize our stack with the src node
    stack = [ src ]
    visited = {}

    while len(stack) > 0:
        cur_node = stack.pop()

        if dst == cur_node:
            return True
        else:
            visited[cur_node] = True 
        
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False 


if __name__ == '__main__':
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']]
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(buildGraph(edges))
    print(hasPathIterative(buildGraph(edges), 'i', 'o'))