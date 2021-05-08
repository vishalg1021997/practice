# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements
# from nums2.

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
l  = [1,2,3,0,0,0]
a = 0
for i in nums1:
    print(i)
    if i == 0:
        a = 0
        nums1.update(nums2[a])