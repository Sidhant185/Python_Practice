nums = list(map(int, input().split()))
frequency = {}

for i in nums:
    frequency[i] = frequency.get(i,0)+1

for num, count in frequency.items():
    print(f"{num}: {count} times")
