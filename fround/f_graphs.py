# depth first traversal ---> stack LIFO
# breadth first traversal ---> queue FIFO 


def depth_first_print(graph, source):
    stack = [ source ]

    while len(stack) > 0:
        cur_node = stack.pop()
        print(cur_node)

        for neighbor in graph[cur_node]:
            stack.append(neighbor)

def depth_first_print_recursive(graph, source):
    print(source)

    for neighbor in graph[source]:
        depth_first_print_recursive(graph, neighbor)


def breadth_first_print(graph, source):
    queue = [ source ]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node)

        for neighbor in graph[cur_node]:
            queue.append(neighbor)

def has_path(graph, start, end):
    # Time complexity: O(e)
    # space complexity: 0(n)
    stack = [ start ]

    while len(stack) > 0:
        cur_node = stack.pop()
        if cur_node == end:
            return True
        else:
            for neighbor in graph[cur_node]:
                stack.append(neighbor)
    return False

if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
    }

    graph_two = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': [],
    }
    # print(depth_first_print(graph, 'a'))
    # print(depth_first_print_recursive(graph, 'a'))
    # print(breadth_first_print(graph, 'a'))
    print(has_path(graph_two, 'f', 'k'))


