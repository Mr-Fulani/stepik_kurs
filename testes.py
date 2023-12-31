# import timeit
# import random
#
# # merge sort using default library
# def merge(list1, list2):
#     return sorted(list1 + list2)
#
# # from stepic
# def quick_merge(list1, list2):
#     result = []
#     p1 = 0
#     p2 = 0
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
#     return result
#
# numbers1 = sorted([random.randint(1, 2000000) for _ in range(1000000)])
# numbers2 = sorted([random.randint(1, 2000000) for _ in range(2000000)])
#
# start = timeit.default_timer()
# merge(numbers1, numbers2)
# print("Processing time merge: %s" % (timeit.default_timer() - start))
#
# start = timeit.default_timer()
# quick_merge(numbers1, numbers2)
# print("Processing time quick_merge: %s" % (timeit.default_timer() - start))



# import time
#
# arr_list = [i for i in range(1000000)]
# arr_set  = {i for i in range(1000000)}
#
# element = 100000
#
# list_start_time = time.time()
# element in arr_list
# list_end_time = time.time()
# set_start_time = time.time()
# element in arr_set
# set_end_time = time.time()
#
# print("--- %2.10f list seconds ---" % (list_end_time - list_start_time))
# print("--- %2.10f set seconds ---" % (set_end_time - set_start_time))