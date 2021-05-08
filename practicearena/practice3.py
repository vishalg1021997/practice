#You will be given 2 different list of same length. you have to print common elements.

list_1, list_2 = input().split() , input().split()
# Write your code here
l = []
for i in list_1:
    for j in list_2:
        if i == j:
            l.append(i)
b = set(l)
c = list(b)
d = sorted(c)
l1 = " ".join(d)
print(l1)


