# Given an integer n,n and  space-separated integers as input, create a tuple,t , of those n  integers.
# Then compute and print the result of hash(t).
#
# Note: hash(t) is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(t)
print(hash(t))



