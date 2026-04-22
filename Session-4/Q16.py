def maxConveyorShifts(s):
    res, ones = 0, 0
    for i in range(len(s)):
        if s[i] == '1':
            ones += 1
        elif i > 0 and s[i-1] == '1':
            res += ones
    return res