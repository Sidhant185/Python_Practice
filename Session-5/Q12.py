def findCeil(arr, x):
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= x:
            ans = mid           # store answer
            right = mid - 1     # left side jao
        else:
            left = mid + 1      # right side jao

    return ans