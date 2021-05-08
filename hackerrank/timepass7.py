# Consider a list (list = []). You can perform the following commands:
#
# 1)insert i e: Insert integer e at i position .
# 2)print: Print the list.
# 3)remove e: Delete the first occurrence of integer e.
# 4)append e: Insert integer e at the end of the list.
# 5)sort: Sort the list.
# 6)pop: Pop the last element from the list.
# 7)reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command
# will be of the 7 types listed above. Iterate through each command in order and perform the corresponding
# operation on your list.


N = int(input())
li = []
n = 0
while N != n:
    n = n + 1
    command = input().split(" ")
    if command[0] == 'insert':
        li.insert(int(command[1]), int(command[2]))
    if command[0] == 'print':
        print(li)
    if command[0] == 'remove':
        if command[1] not in li:
            li.remove(int(command[1]))
    if command[0] == 'append':
        li.append(int(command[1]))
    if command[0] == 'sort':
        li.sort()
    if command[0] == 'pop':
        if len(li) != 0:
            li.pop()
    if command[0] == 'reverse':
        li.reverse()

print(li)