def getmin(arr, k):
    arr.sort()
    n = len(arr)
    ans = arr[-1]-arr[0]
    for i in range(1, n-1):
        mini = min(arr[0]+k,arr[i+1]-k)
        maxi = max(arr[-1]-k,arr[i]+k)
        ans = min(ans, maxi-mini)
    return ans

nums = list(map(int, input().split()))
target = int(input())
print(getmin(nums, target))