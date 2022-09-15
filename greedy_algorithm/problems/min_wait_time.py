# [3, 2, 1, 2, 6]
# - [1, 2, 2, 3, 6]
# [0, 1, 3, 5, 8]
# amount of time query must wait before it starts executing

def minimum_waiting_time(queries):
    # time: O(nlogn) | space: O(1)
    cum_waiting_time = 0

    queries.sort()

    for i, e_time in enumerate(queries, 1):
        queries_left = len(queries) - i
        cum_waiting_time += (e_time * queries_left)
    return cum_waiting_time


if __name__ == '__main__':
    print(minimum_waiting_time([3, 2, 1, 2, 6]))