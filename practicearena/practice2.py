# You will be given to list main_list and sub_list.
# You have to check sublist presents in main list or not?

main_list, sub_list = input().split() , input().split()
#Write your code here
check =  all(item in main_list for item in sub_list)
print(check)