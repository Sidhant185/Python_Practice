def findExtra(arr1, arr2):
    left = 0
    right = len(arr2) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr1[mid] == arr2[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left