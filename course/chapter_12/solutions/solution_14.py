import copy
def uniqueness(set_list):
    a = set_list[0]
    for i in range(1,len(set_list)-1):
        a = a^set_list[i+1]
    return a

set_list = [{1, 2}, {2, 3}, {4, 5}]
print(uniqueness(set_list))