def riverSizes(matrix):
    sizes = []
    visited = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            size = exploreRivers(matrix, r, c, visited)

            if size:
                sizes.append(size)
    return sorted(sizes)


def exploreRivers(matrix, r, c , visited):
    node = str(r) + ',' + str(c)
    rowBound = 0 <= r < len(matrix)
    columnBond = 0 <= c < len(matrix[0])

    if not rowBound or not columnBond:
        return 0
    
    if matrix[r][c] == 0:
        return 0
    
    if node in visited:
        return 0
    
    visited[node] = True

    size = 1
    size += exploreRivers(matrix, r - 1, c, visited)
    size += exploreRivers(matrix, r + 1, c, visited) # down
    size += exploreRivers(matrix, r, c - 1, visited) # left
    size += exploreRivers(matrix, r, c + 1, visited) # right

    return size


if __name__ == '__main__':
    grid = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1], 
        [1, 0, 1, 1, 0]
    ]
    print(riverSizes(grid))