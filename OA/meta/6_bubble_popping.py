# diagonal neighbors
# bubble-popping
# 模拟题，每次点完计算左中右三列的变化
def pop_bubbles(board, i, j):
    # Get the size of the board
    rows, cols = len(board), len(board[0])
    
    # Color of the clicked cell
    color = board[i][j]
    
    # Directions for diagonal neighbors: (row_offset, col_offset)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Helper function for the DFS recursive flood fill
    def dfs(x, y):
        # Base case: If out of bounds or the cell does not match the color, return
        if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] != color:
            return
        
        # Pop the current bubble (mark it as empty, e.g., with -1)
        board[x][y] = -1
        
        # Explore all diagonal neighbors
        for dx, dy in directions:
            dfs(x + dx, y + dy)
    
    # Start the DFS from the clicked cell
    dfs(i, j)
    
    return board

# Example usage
board = [
    [1, 2, 1, 1],
    [2, 1, 2, 1],
    [1, 2, 1, 2],
    [2, 1, 1, 2]
]

# Click on the cell at (1, 1) with color 1
new_board = pop_bubbles(board, 1, 1)

for row in new_board:
    print(row)
