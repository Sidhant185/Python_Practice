def maxDiff(s):
    freq = {}

    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    max_odd = 0
    min_even = float('inf')

    for count in freq.values():
        if count % 2 == 1:   
            max_odd = max(max_odd, count)
        else:                
            min_even = min(min_even, count)

    return max_odd - min_even