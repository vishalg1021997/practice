#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

nums = [-7,-3,2,3,11]

new = []
for i in nums:
    new.append((i)**2)
print(sorted(new))