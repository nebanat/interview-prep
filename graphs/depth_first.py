# depth first - uses a stack to keep track of the nodes to visit
from stacks.stack import Stack

def depth_first_traversal(graph, start):
    """_summary_

    Args:
        graph (_type_): _description_
        start (_type_): _description_

    Returns:
        _type_: _description_
    """
    visited = ""
    stack = Stack()
    stack.push(start)
   
    while stack.stack_size > 0:
        current = stack.pop()
        visited += (str(current) + '-') 
        for neighbor in graph[current]:
            stack.push(neighbor)
    return visited

def depth_first_traversal_recursive(graph, start, visited=""):
    """_summary_

    Args:
        graph (_type_): _description_
        start (_type_): _description_
        visited (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    visited += (str(start) + '-')
    for neighbor in graph[start]:
        visited = depth_first_traversal_recursive(graph, neighbor, visited)
    return visited

if __name__ == '__main__':
    graph = {
        "a": ["c", "b"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    print(depth_first_traversal(graph, "a"))
    print(depth_first_traversal_recursive(graph, "a"))

