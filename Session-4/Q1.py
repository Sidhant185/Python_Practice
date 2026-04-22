def pairSumChecker(arr, x):
    seen = set()
    for num in arr:
        if x - num in seen:
            return "Yes"
        seen.add(num)
    return "No"