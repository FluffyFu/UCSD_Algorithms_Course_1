from sorting import partition3, randomized_quick_sort_2, randomized_quick_sort

# a = [2, 3, 9, 2, 9]
# randomized_quick_sort(a, 0, len(a)-1)

a = [9, 3, 9, 2, 2]
l, r = 0, len(a) - 1
partition3(a, l, r)
