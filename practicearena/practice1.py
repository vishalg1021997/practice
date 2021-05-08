# You will have number or elements and next n lines containing list elements. You have to create list
# from that given string. Write a program to count the number of strings where the string length is
# 2 or more and the first and last character are same from a given list of strings.¶

n = int(input())
# Write your code here
count = 0
for i in range(0,n):
    s = input()
    if s[0] == s[len(s) -1]:
        count = count + 1
print(count)
