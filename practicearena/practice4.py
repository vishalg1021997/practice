s = input()
list1 = list(s)
for i in range(len(list1)):
    if i % 2 != 0:
         list1[i] = 'A'
print("".join(list1))


s = input()
l=list(s)
for i in range(1,len(s),2):
    l.insert(i,"A")
    l.pop(i+1)
print("".join(l))