# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters,
# digits, lowercase and uppercase characters.
#
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

s = input()

#l = list[s]
for i in s:
    if (i.isalnum()):
        print(True)
    if (i.isalpha()):
        print(True)
    if (i.isdigit()):
        print(True)
    if (i.islower()):
        print(True)
    if (i.isupper()):
        print(True)
    else:
        print(False)


#
# print(s.isalnum())
# # print(s.isalpha())
# # print(s.isdigit())
# # print(s.islower())
# # print(s.isupper())