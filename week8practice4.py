def doublelist(old_list):
    new_list = []
    for x in range(10):
        newval = old_list[x] * 2
        new_list.append(newval)
    return new_list

user_list = [1,2,3,4,5,6,7,8,9,10]

print(doublelist(user_list))
