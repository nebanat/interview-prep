# grid like graphs 
# 1. look at the grid position as nodes of a graph
# 2. A grid position has at most four neighbors : up, down, left and right neighbor 
#    - up : (r - 1, c)
#    - down: (r + 1, c)
#    - left: (r, c - 1)
#    - right: (r, c + 1)
# 3 . island count algorithms:
#    - at each position do a depth first traversal of its neighbors, 
#      make sure you keep track of the visited nodes 
#          * if node is already visited there is no need to traverse 
#          * also if a node is water there is no need to traverse that node 
# 4. make sure to keep a count of the explored islands (land surrounded by water)
# 5. return the count


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