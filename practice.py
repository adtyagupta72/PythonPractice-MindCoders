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

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)
# print(list_1)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)


# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# new_list = my_list[-5:3]
# new_list = my_list[:3]
# print(new_list)
# new_list = my_list[2:]
# print(new_list)
#del my_list[1:3]

#del my_list

# del my_list[:]
# print(my_list)

# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
# del list_1[0]
# del list_2
# print(list_3)

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")

# row = ["WHITE_PAWN" for i in range(8)]
# squares = [index ** 2 for index in range(1, 11)]
# twos = [2 ** index for index in range(8)]

# print(row)
# print(squares)
# print(twos)

# squares = [index ** 2 for index in range(1, 11)]
# odds = [f'{element} Is Odd Number!' for element in squares if element % 2 != 0 ]
# print(odds)

board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

#print(board)
for element in board:
    print(element)

print(len(board))