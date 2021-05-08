#Given a binary array nums, return the maximum number of consecutive 1's in the array.
l =[1,1,0,1,1,1]

count1 = 0
maxi = []
for i in l:
    count2 = 0
    if i == 1:
        count1 = count1 + i
    maxi.append(count1)
    if i == 0:
        count1 = 0
        continue
print(max(maxi))
print()

# if count1 > maxi:
#     print(count1)m
# else:
#     print(maxi)
