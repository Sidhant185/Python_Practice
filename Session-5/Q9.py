def countOccurrences(arr, target):

    def findFirst():
        left, right = 0, len(arr) - 1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                ans = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans


    def findLast():
        left, right = 0, len(arr) - 1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                ans = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans


    first = findFirst()
    if first == -1:
        return 0

    last = findLast()
    return last - first + 1