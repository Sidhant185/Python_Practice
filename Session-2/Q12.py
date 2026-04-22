nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

inter = list(set(nums1)& set(nums2))
print(inter)