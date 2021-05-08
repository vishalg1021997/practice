#Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    l1 = ''.join(l)
    return l1

def mutate_string1(string, position, character):
    string1 = string[:position] + character + string[position+1:]
    return string1

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
s_new1 = mutate_string1(s, int(i), c)
print(s_new)
print(s_new1)