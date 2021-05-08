def count_substring(string, sub_string):
    count1 = 0
    i = string.find(sub_string)
    while i != -1:
        count1 += 1
        i = string.find(sub_string, i + 1)
    return count1


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)