#               (2, 3)
#       1  /              \2
#      (1, 3)                 (2, 2)
#      /   \            /   1         \1
#   (0,3)   (1,2)       (1, 2)        (2, 1)
#          /     \       /     \       /    \
#        (0, 2)  (1,1) (0,2)  (1, 1) (1,1)  (2, 0) 

def gridTraveler(m, n, memo={}):
    node = str(m) + ',' + str(n)
    
    if node in memo: return memo[node]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    
    memo[node] = gridTraveler( m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[node]

if __name__ == '__main__':
    print(gridTraveler(1, 1))
    print(gridTraveler(2, 3))
    print(gridTraveler(3, 2))
    print(gridTraveler(3, 3))
    print(gridTraveler(18, 18))