def missing(Arr):
    n = len(Arr)+1
    ExSum = ((n+1)*n)//2
    actualSum = sum(Arr)
    ans = ExSum-actualSum
    return ans


nums = list(map(int, input().split()))
print(missing(nums))
