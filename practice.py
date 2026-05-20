print("Hello World")
print("Testing commit changes")

# Sorting of a List:
# my_list = [8, 10, 6, 2, 4]  # list to sort [1, 2, 3, 4, 5]#
# swapped = True  # It's a little fake, we need it to enter the while loop.
# count = 0
# index = 0
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1 - index):
#         index = i
#         count += 1
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)
# print(count)

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
