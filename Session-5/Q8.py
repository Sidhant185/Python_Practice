def searchRange(nums, target):

    # First occurrence
    def findFirst():
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                ans = mid
                right = mid - 1   # left side search
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    # Last occurrence
    def findLast():
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1   # right side search
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    return [findFirst(), findLast()]