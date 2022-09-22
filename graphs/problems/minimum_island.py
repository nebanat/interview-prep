from math import inf
def minimumIsland(grid):
    visited = {}
    min_size = inf
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSize(grid, r, c, visited)

            if size < min_size:
                min_size = size
    return min_size

def exploreSize(grid, r, c, visited):
    rowInbounds = 0 <= r < len(grid)
    columnInbounds = 0 <= c < len(grid[0])

    if not rowInbounds or not columnInbounds:
        return 0
    
    if grid[r][c] == 'W':
        return 0
    
    pos = f'{r},{c}'
    if pos in visited:
        return 0
    visited[pos] = True

    size = 1
    size += exploreSize(grid, r - 1, c, visited) # up
    size += exploreSize(grid, r + 1, c, visited) # down
    size += exploreSize(grid, r, c - 1, visited) # left
    size += exploreSize(grid, r, c + 1, visited) # right

    return size 
