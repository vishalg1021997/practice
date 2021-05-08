#Given an array nums of integers, return how many of them contain an even number of digits.

nums = [12,345,2,6,7896]
count1 = 0
for i in nums:
    if len(str(i))%2 == 0:
        count1 = count1 + 1

print(count1)