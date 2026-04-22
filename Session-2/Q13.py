def findp(arr, target):
    seen = set()
    pair = set()

    for num in arr:
        complement = target- num
        if complement in seen:
            pair.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(pair)
nums = list(map(int, input().split()))
target = int(input())
print(findp(nums, target))