def solution(board):
    rows = len(board)
    cols = len(board[0])
    
    # Step 1: Identify the cells occupied by the figure.
    figure_positions = []
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '*':
                figure_positions.append((r, c))
    
    # Step 2: Determine obstacles in each column occupied by the figure.
    min_obstacles_to_remove = float('inf')  # Start with a large number
    
    # Step 3: Check each column for obstacles.
    columns_to_check = set(c for _, c in figure_positions)  # Columns where the figure is present
    
    for col in columns_to_check:
        obstacles_count = 0
        
        # Check all rows in the current column from the bottom up
        for r in range(rows - 1, -1, -1):
            if board[r][col] == '#':
                obstacles_count += 1  # Count the obstacle
            elif board[r][col] == '*':
                # If we hit a part of the figure, we can stop counting
                break
        
        # Keep track of the minimum obstacles across the columns of the figure
        min_obstacles_to_remove = min(min_obstacles_to_remove, obstacles_count)

    return min_obstacles_to_remove if min_obstacles_to_remove != float('inf') else 0

# Example usage
board = [
    ["*", "*", "*"],
    ["#", "*", "*"],
    ["*", "*", "-"],
    ["-", "-", "-"],
    ["-", "#", "#"],
]
print(solution(board))  # Output: 2
