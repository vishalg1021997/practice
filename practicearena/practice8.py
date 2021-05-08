s = input()
# Write your code here
lenofs = len(s)
reverseofs = ""
if lenofs%4==0:
    print(s[lenofs::-1])
else:
    print(s)