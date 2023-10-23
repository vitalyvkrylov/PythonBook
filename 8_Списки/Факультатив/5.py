def count_sum_lists(list1, list2, list3):
    max_sum = max(sum(list1), sum(list2), sum(list3))
    min_sum = min(sum(list1), sum(list2), sum(list3))
    return max_sum, min_sum
def reduce_list(list, max_sum, min_sum):
    diff = max_sum - min_sum
    return [x - diff for x in list]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
max_sum, min_sum = count_sum_lists(list1, list2, list3)
print(max_sum)
print(min_sum)
new_list1 = reduce_list(list1, max_sum, min_sum)
new_list2 = reduce_list(list2, max_sum, min_sum)
new_list3 = reduce_list(list3, max_sum, min_sum)
print(new_list1)
print(new_list2)
print(new_list3)