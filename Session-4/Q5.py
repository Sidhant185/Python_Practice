def getmin(arr, k):
    arr.sort()
    n = len(arr)
    ans = arr[-1]-arr[0]
    for i in range(n-1):
        if arr[i+1]<0: continue
        mini = min(arr[0]+k,arr[i+1]-k)
        maxi = max(arr[-1]-k,arr[i]+k)
        ans = min(ans,maxi-mini)
    return ans

nums = list(map(int, input()))
target = int(input())
print(getmin(nums,target))