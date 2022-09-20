# breadth first - uses a queue to keep track of the nodes to visit

from queue.queue import Queue

def breadth_first_traversal(graph, start):
    # only possible iteratively
    q = Queue()
    q.enqueue(start)
    visited = ""
    while q.queue_size > 0:
        current = q.dequeue()
        visited += (str(current) + '-')
        for neighbor in graph[current]:
            q.enqueue(neighbor)
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
    print(breadth_first_traversal(graph, "a"))