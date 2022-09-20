from stacks.stack import Stack

def has_path_depth(graph, start, end):
    if start == end:
        return True
    
    for neighbor in graph[start]:
        if has_path_depth(graph, neighbor, end):
            return True
    return False
        

def has_path_breadth(graph, start, end):
    if start == end:
        return True
    
    # visited = set()
    queue = Stack()
    queue.push(start)
    
    while queue.stack_size > 0:
        current = queue.pop()
        if current == end:
            return True
        for neighbor in graph[current]:
            queue.push(neighbor)
    return False