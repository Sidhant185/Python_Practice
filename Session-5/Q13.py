def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1
    ans = None

    while left <= right:
        mid = left + (right - left) // 2

        if letters[mid] > target:
            ans = letters[mid]     # store
            right = mid - 1        # left side jao
        else:
            left = mid + 1         # right side jao

    return ans if ans else letters[0]