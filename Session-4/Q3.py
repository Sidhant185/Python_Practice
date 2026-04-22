def canPlaceFlowers(flowerbed, k):
    count = 0
    f = [0] + flowerbed + [0] 
    for i in range(1, len(f) - 1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            count += 1
    return count >= k