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

# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# #print(board)
# for element in board:
#     print(element)

# # print(len(board))

# #print(board[0][0])

# board[0][0] = "ROOK"
# board[0][7] = "ROOK"
# board[7][0] = "ROOK"
# board[7][7] = "ROOK"

# print("---------------")

# for element in board:
#     print(element)

# board[0][1] = "KNIGHT"
# board[0][6] = "KNIGHT"
# board[7][1] = "KNIGHT"
# board[7][6] = "KNIGHT"

# print("---------------")

# for element in board:
#     print(element)


# temps = [[0.0 for h in range(24)] for d in range(31)]

# temp1 = 19
# temp2 = 32
# count = 0

# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#         days[11] = temp2
#         count = 0
    
# for element in temps:
#     print(element)

# total = 0.0
# for day in temps:
#     total += day[11]
# average = total / 31
# print("Average temperature at noon:", average)

# highest = -100.0
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
# print("The highest temperature was:", highest)

# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
# print(hot_days, "days were hot days in the month.")

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# print(rooms)

# rooms[1][9][13] = True

# rooms[1][9][1] = True

# vacancy = 0
# for room_number in range(20):
#     if not rooms[1][9][room_number]:
#         vacancy += 1
# print("Vacancy in 10th Floor, of 3rd Building is: ", vacancy)

# for room_number in range(20):
#     rooms[0][10][room_number] = True

# rooms[0][10][8] = False

# vacancy = 0
# for room_number in range(20):
#     if not rooms[0][10][room_number]:
#         vacancy += 1
# print("Vacancy in 11th Floor, of 1st Building is: ", vacancy)


# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")

'''
i (5)           0   1   2
OP              *   
'''

# for i in range(1):
#     print("#")
# else:
#     print("#")

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#") 



my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])

print(my_list)

'''
my_list         [1, 2, 3]   [1, 1, 2, 3]    [1, 1, 1, 1, 2, 3]
v (3)           0      1    2

'''