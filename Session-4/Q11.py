def exitPoint(matrix):
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, 0
    dir = 0 # 0: East, 1: South, 2: West, 3: North
    
    while True:
        if matrix[r][c] == 1:
            dir = (dir + 1) % 4
            matrix[r][c] = 0
            
        # Try moving
        prev_r, prev_c = r, c
        if dir == 0: c += 1
        elif dir == 1: r += 1
        elif dir == 2: c -= 1
        elif dir == 3: r -= 1
        
        # Check exit
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return f"{prev_r} {prev_c}"