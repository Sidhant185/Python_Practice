def maxSum(arr):
    max_Sum = current_Sum = arr[0]
    for i in range(1, len(arr)):
        current_Sum = max(arr[i], current_Sum+arr[i])
        max_Sum = max(current_Sum, max_Sum)
    return max_Sum

num1 = list(map(int, input().split()))
print(maxSum(num1))