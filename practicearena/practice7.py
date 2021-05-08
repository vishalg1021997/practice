s1 = input()
s2 = input()
listofs1 = list(s1)
listofs2= list(s2)
print("".join(listofs2[0:2] + listofs1[2:]),"".join(listofs1[0:2] + listofs2[2:]))
#print(listofs1, listofs2)
# newlist1 = listofs1[0:2] + listofs2[2:]
# newlist2 = listofs2[0:2] + listofs1[2:]
# print("".join(newlist2),"".join(newlist1))
