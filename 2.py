some_list = [1, 2, 3, 5, 1, 5, 3, 10]
list1 = [x for x in some_list if some_list.count(x) == 1]


print(list1)


