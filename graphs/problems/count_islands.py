def island_count(grid):
    visited = {}
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count

def explore(grid, r, c, visited):
    rowInbounds = 0 <= r < len(grid)
    columnInbounds = 0 <= c < len(grid[0])

    if not rowInbounds or not columnInbounds:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    pos = f'{r},{c}'
    if pos in visited:
        return False
    
    visited[pos] = True
    explore(grid, r - 1, c, visited) # up
    explore(grid, r + 1, c, visited) # down
    explore(grid, r, c - 1, visited) # left
    explore(grid, r, c + 1, visited) # right 

    return True

if __name__ == '__main__':
    matrix = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'L', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W'],
        
        ]
    print(island_count(matrix))