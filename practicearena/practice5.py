s = input()
s_new=""
for i in range(len(s)):
    if((s[i].lower() not in s_new) and (s[i].upper() not in s_new)):
        s_new=s_new+s[i]
print(s_new)