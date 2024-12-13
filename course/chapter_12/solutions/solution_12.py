import copy
def uniqueness(set_list):
    a = set_list[0]
    b = a&set_list[1]
    for i in range(1,len(set_list)):
        b = b | a&set_list[i]
        a = (a-b) | (set_list[i]- b)
    return a

#set_list = [{1, 2}, {2, 3}, {4, 5}]
#print(uniqueness(set_list))