# Q11: Exit Point from Matrix
# Simulate movement through matrix with obstacles

def exitPoint(matrix):
    """
    Find exit point when moving through matrix
    1 = obstacle (turn), 0 = empty (continue)
    Directions: 0=East, 1=South, 2=West, 3=North
    """
    rows, cols = len(matrix), len(matrix[0])
    
    # Start position and direction (East)
    r, c = 0, 0
    dir = 0  # 0: East, 1: South, 2: West, 3: North
    
    # Continue movement until exit
    while True:
        # Check for obstacle
        if matrix[r][c] == 1:
            # Turn right (clockwise)
            dir = (dir + 1) % 4
            # Mark as visited
            matrix[r][c] = 0
        
        # Save previous position
        prev_r, prev_c = r, c
        
        # Move in current direction
        if dir == 0: c += 1       # East: move right
        elif dir == 1: r += 1     # South: move down
        elif dir == 2: c -= 1     # West: move left
        elif dir == 3: r -= 1     # North: move up
        
        # Check if we've exited the matrix
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return f"{prev_r} {prev_c}"