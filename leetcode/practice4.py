# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.

arr = [1,0,2,3,0,4,5,0]
#arr = [1,2,3]
#a = len(arr)
i = 0
j = len(arr)
while i < len(arr):
    if arr[i] == 0:
        arr.insert(i + 1, 0)
        i = i + 1
    i = i + 1
for i in range(j, len(arr)):
    arr.pop(j)
print(arr)
