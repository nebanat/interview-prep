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

# constraints
# 1. make sure the node you are within the array bounds
# 2. make sure you have not visited that node already
# 3. make sure the node is not water

def island_count(grid):
    # time complexity: O(r*c)
    # space complexity: O(r*C)
    count = 0
    visited = {}

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore_island(grid, r, c, visited):
                count += 1
    return count 

def explore_island(grid, r, c, visited):
    cur_node = str(r) + ',' + str(c)
    rowBound = 0 <= r < len(grid)
    columnBound = 0 <= c < len(grid[0])

    if not rowBound or not columnBound:
        return False 

    if cur_node in visited:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    visited[cur_node] = True

    # top neighbor (r-1, c)
    explore_island(grid, r - 1, c , visited)
    # bottom neighbor 
    explore_island(grid, r + 1, c, visited)
    # right neighbor
    explore_island(grid, r, c + 1, visited)
    # left neighbor 
    explore_island(grid, r, c - 1, visited)

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