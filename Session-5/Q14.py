def searchAlmostSorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # check mid
        if arr[mid] == target:
            return mid

        # check left neighbor
        if mid - 1 >= left and arr[mid - 1] == target:
            return mid - 1

        # check right neighbor
        if mid + 1 <= right and arr[mid + 1] == target:
            return mid + 1

        # move search space
        if arr[mid] < target:
            left = mid + 2
        else:
            right = mid - 2

    return -1