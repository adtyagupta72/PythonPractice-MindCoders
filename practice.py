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



# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])

# print(my_list)

'''
my_list         [1, 2, 3]   [1, 1, 2, 3]    [1, 1, 1, 1, 2, 3]
v (3)           0      1    2

'''

# def message():
#     print("Enter a value: ")
#     temp = int(input())
#     return temp

# print("Step 1")
# a = message()       #Invocation / Calling a function

# print("Step 2")
# b = message()

# print("Step 3")
# c = message()

# print("a:", a)
# print("b:", b)
# print("c:", c)

# def message():
#     print("Enter a value: ")

# #message = 1

# print("We start here.")
# print(message)
# message()
# print("We end here.") 


# def hi():
#     print("hi")
# hi(5)


# def hello(n): # defining a function
#     print("Hello,", n) # body of the function

# name = input("Enter your name: ")
# hello(name) # calling the function

# def message(number):
#     print("Enter a number")
#     number = int(input())
#     return number
 

# number = message(1)
# print(number) 

# def message(what, number):
#     print("Enter", what, "number", number)
 
# message("telephone", 11)
# message(11, "telephone")
# message("price", 5)
# message("number", "number")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
 
# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")

# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")
# introduction("Skywalker", last_name = "Luke")


# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# adding(1, 2, 3)
# adding(c = 1, a = 2, b = 3)
# adding(3, c = 1, b = 2)
# adding(3, a = 1, b = 2)

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")

# happy_new_year(False)

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123

# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...")

# print(None + 2)

# def checkMyVar(variable):
#     if(variable == 10):
#         print("Variable is 10")
#         return 2
#     else:
#         print("Variable is not up to the mark")
#         return
    
# checkMyVar(5)
# print()


# def list_sum(lst):
#     s = 0
 
#     for elem in lst:
#         s += elem
 
#     return s
# print(list_sum([5, 4, 3]))
# print(list_sum(2))


# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         #strange_list.insert(0, i+1)
#         strange_list.append(i+1)
    
#     return strange_list

# print(strange_list_fun(5))

# def scope_test():
#     x = 123
# scope_test()
# print(x)

# def my_function():
#     print("Do I know that variable?", var)

# var = 1
# my_function()
# print(var)

# def mult(x):
#     var = 7
#     return x * var 
# var = 3
# print(mult(7))

# def my_function():
#     global var
#     var = 2
#     print("Do I know that variable?", var)

# var = 1
# my_function()
# print(var)

# var = 2
# print(var) # outputs: 2
 
# def return_var():
#     global var
#     var = 5
#     return var
 
# print(return_var()) # outputs: 5
# print(var)

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)

# var = 1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0] # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# def countDown(number):
#     print(number)
#     if number == 0:
#         return
#     else:
#         print("Going in rec:",  number)
#         countDown(number -1)
#         print("Out of rec:",  number)

# print("Starting Recursion")
# countDown(5)
# print("Completed Recursion")

'''
cd  1   2   3   4   5   6
n   5   4   3   2   1   0
op  5   4   3   2   1   0

'''

# 5! = 5, 4, 3, 2, 1 = 120

# def factorial(number):
#     if number <= 0:
#         return 1
#     else:
#         return number * factorial(number - 1)

# print(factorial(5))

# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# my_tuple = (10, 100, 1000)
# my_tuple += (10000, 100000)
# print(my_tuple)

# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)

# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2 
# print(tuple_4)
# print(tuple_5)

# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)
# print(type(my_tuple))
 
# my_list = [2, 4, 6]
# print(my_list) # outputs: [2, 4, 6]
# print(type(my_list)) # outputs: <class 'list'>
# tup = tuple(my_list)
# print(tup) # outputs: (2, 4, 6)
# print(type(tup)) # outputs: <class 'tuple'>
# var = 123
 
# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)
 
# t1, t2, t3 = t2, t3, t1
 
# print(t1, t2, t3)
# print(type(t1), type(t2), type(t3))

# dictionary = {
# "cat": "chat", 
# "dog": "chien", 
# "horse": "cheval"
# }
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}
 
# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary['cat'])
# print(phone_numbers['Suzy'])
# #print(phone_numbers['president'])

# words = ['cat', 'lion', 'horse']
 
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print("-----",word, "is not in dictionary", "-----")

# print(dictionary.keys())

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# print(dictionary.items())

# for key, value in dictionary.items():
#     print(key, "->", value)

# print(dictionary.values())

# for value in dictionary.values():
#     print(value)


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# print("pol_eng_dictionary: ", pol_eng_dictionary)
# copy_dictionary = pol_eng_dictionary.copy()

# print("copy_dictionary: ",copy_dictionary)

# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item)

# phonebook = {} # an empty dictionary
 
# print(phonebook)
# phonebook["Adam"] = 3456783958 # create/add a key-value pair
# print(phonebook) # outputs: {'Adam': 3456783958}
 
# del phonebook["Adam"]
# print(phonebook)


# pol_eng_dictionary = {"kwiat": "flower"}
 
# pol_eng_dictionary.update(
#     {
#         "gleba": "soil"
#     })
# print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}
 
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
 
# if "zamek1" in pol_eng_dictionary:
#    print("Yes! zamek1 is present in the Dictionary")
# else:
#    print("No! zamek1 is not present in the Dictionary")

# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))
 
# pol_eng_dictionary.clear()
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))
 
# del pol_eng_dictionary
# print(pol_eng_dictionary)

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
# dictionary.update({"duck": "canard"})
# print(dictionary)

# sd = {}

# while True:
#     name = input("Enter Students name:")
#     if name == "":
#         break
#     score = int(input(f"Enter {name}'s score:"))

#     if score not in range(1,11):
#         break
#     if name in sd:
#         sd[name] += (score, )
#     else:
#         sd[name] = (score, )

# print(sd)

# for name, mark in sd.items():
#     sum = 0
#     for m in mark:
#         sum += m
#     print(name, "-> ", sum/len(mark))

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val
 
#     def set_second(self, val):
#         self.second = val

#     def example_method():
#         pass

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
# example_object_3.example_method()

# class Classy:
#     def method(self, par):
#         print("method", par)

# obj = Classy()
# obj.method(1)

# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)

# obj = Classy()
# obj.var = 3
# obj.method()

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = Star("Sun", "Milky Way")
# print(sun)

# class ExampleClass:
#     counter = 0
#     a = 1
#     def __init__(self, val = 1):
#         #self.__first = val
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1

# example_object = ExampleClass(1)

# if hasattr(example_object, 'a'):
#     print("a = ", example_object.a)

# if hasattr(example_object, 'b'):
#     print("b = ", example_object.b)

# print(hasattr(ExampleClass, 'b'))   #
# print(hasattr(ExampleClass, 'a'))   #


# try:
#     print("a = ",example_object.a)
# except AttributeError:
#     try:
#         print("b = ",example_object.b)
#     except AttributeError:
#         print("The error has occured! Sliently passing it!")



# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
 
# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False

# myObj = Python()
# print("myObj.population: ", myObj.population)
# print("myObj.victims: ", myObj.victims)
# print("myObj.length_ft: ", myObj.length_ft)
# print("myObj.__venomous: ", myObj._Python__venomous)###
# print("myObj.venomous: ", myObj.venomous)

# class Classy:
#     def visible(self):
#         print("visible")
    
#     def __hidden(self):
#         print("hidden")

# obj = Classy()
# obj.visible()               # Output: visible
# try:
#     obj.__hidden()          # This fails
# except:
#     print("failed")         # Output: failed
# obj._Classy__hidden()       # Output: hidden

# obj = Classy()
# print(type(obj))
# print(type(obj).__name__)

# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()


# class SampleClass:
#     def __init__(self, val):
#         self.val = val

# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary had a little "
# string_2 = "Mary had a little lamb"
# string_1 += "lamb"

# print(string_1 == string_2, string_1 is string_2)

# class Super:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return "My name is " + self.name + "."

# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)

# obj = Sub("Andy")
# print(obj)

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11

# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21

# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

# class Level1:
#     var = 100
#     def fun(self):
#         return 101

# class Level2(Level1):
#     var = 200        # Overrides
#  Level1.var
#     def fun(self):   # Overrides Level1.fun()
#         return 201

# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var, obj.fun())

# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var = "R"           # Same name as Left.var
#     var_right = "RR"
#     def fun(self):      # Same name as Left.fun()
#         return "Right"
# class Sub(Left, Right):
#     pass
# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun())

# class One:
#     def do_it(self):
#         print("do_it from One")
    
#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# one = One()
# two = Two()
# one.doanything()  # Output: do_it from One
# two.doanything()

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("It's time to say goodbye")
#         return n

# print("------------")
# print("reciprocal(2): ", reciprocal(2))  # Uses else branch
# print("------------")
# print("reciprocal(0): ", reciprocal(0))
# print("------------")

# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())

# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")
#     print(thisclass.__name__)
#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)

# print_exception_tree(BaseException)

# class MyZeroDivisionError(ZeroDivisionError):    
#     pass
 
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:        
#         raise ZeroDivisionError("some bad news")

# do_the_division(False)
# do_the_division(True)

# city = 'Bhopal'
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3]) 
# print(city[3]) 

# name = 'Priya Sharma'
# print(name[0:5])   # Priya  (index 0 to 4)
# print(name[6:])    # Sharma (from index 6 to end)
# print(name[:5])    # Priya  (from start to index 4)
# print(name[::2])   # Pay hr  (every 2nd character)
# print(name[::-1])  # amrahS ayirP  (reversed!)
 
# # Length of string
# print(len(city))   # 6
# print(len(name))

text = '  Hello Python World!  '
# Case
# print(text.upper())           # '  HELLO PYTHON WORLD!  '
# print(text.lower())           # '  hello python world!  '
# print(text.title())           # '  Hello Python World!  '
# print(text.capitalize())      # '  hello python world!  ' → first only
 
# # Strip whitespace
# print(text.strip())           # 'Hello Python World!'
 
# # Search
# print('Python' in text)       # True
# print(text.find('Python'))    # 8  (index where found, -1 if not found)
# print(text.count('l'))   

# Replace
# print(text.replace('Python', 'AI'))  # '  Hello AI World!  '
 
# Split and Join
# csv = 'Rahul,22,Bhopal,Engineer'
# parts = csv.split(',')        # ['Rahul', '22', 'Bhopal', 'Engineer']
# print(parts)
# print(parts[0])               # Rahul
# rejoined = ' | '.join(parts)  # 'Rahul | 22 | Bhopal | Engineer'
# print(rejoined)
 
# # Check content
# print('hello123'.isalnum())   # True — all letters/digits
# print('12345'.isdigit())      # True — all digits
# print('Python'.isalpha())     # True — all letters
# print('  '.isspace())         # True — all spaces

# # Start/end check
# email = 'student@gmail.com'
# print(email.endswith('.com'))  # True
# print(email.startswith('stu')) # True

# name, marks, rank = 'Anita', 92.567, 3
 
# # Basic
# print(f'Hello, {name}!')
 
# # Format numbers
# print(f'Marks: {marks:.2f}')       # 92.57 (2 decimal places)
# print(f'Marks: {marks:.0f}')       # 93    (rounded)
# print(f'Count: {1000000:,}')       # 1,000,000 (comma separator)
 
# # Padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')  # left/right align
# print(f'hello {name:^10}')
# print(f'hello {name:>10}')
# print(f'hello {name:<10}')
# print(f'hello {name:*^11}')
# # Anita          |   92.57|Rank:3
 
# # Expressions inside {}
# price, gst = 500, 0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')

# string = "Hello, How are you doing today?"
# Count vowels in the string
# Print you from the string
# Print the string in reverse order
# non_palin, palin = "abcdef", "axttxa"
# check if the string is palindrome or not

# with open("data.txt", "r") as file: 
#     data = file.read()

# print(data)


# with open('students.txt', 'w') as f:
#     f.write('Rahul Sharma,85,Bhopal\n')
#     f.write('Priya Verma,92,Indore\n')
#     f.write('Amit Kumar,73,Jabalpur\n')

# with open('students.txt', 'a') as f:
#     f.write('Sneha Joshi,88,Bhopal\n')

# with open('students.txt', 'r') as f:
#     content = f.read()
# print(content)

# with open('students.txt', 'r') as f:
#     for line in f:
#         name, marks, city = line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print("------------")

# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B']
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# name = input("Enter Student Name for Search:")

# found = False

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         if row["Name"] == name:
#             print(f'Found {name}')
#             print(f'{row["Name"]}: {row["Marks"]} marks ({row["City"]})')
#             found = True
#             break

# if not found:
#     print("Student Not found!!")

# import numpy as np

# arr1d = np.array([1, 2, 3, 4, 5])
# arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])  # 3 students x 3 subjects
 
# print(arr2d.shape)     # (3, 3)
# print(arr2d.dtype)     # int64
# print(arr2d.ndim)      # 2 (2-dimensional)

# zeros = np.zeros((3,4))
# # 3x4 array of 0s
# print(zeros)
# ones  = np.ones((2,5))            		
# # 2x5 array of 1s
# print(ones)
# rng   = np.arange(0,50,5)         		
# # [0,5,10,15,...,45]
# print(rng)

# lin   = np.linspace(0,1,11)
# print(lin)

# random  = np.random.randint(40,100,(5,3))
# print(random)

# arr = np.array([10,20,30,40,50])

# print(arr * 2)        # [20 40 60 80 100]

# print(arr + 5)        # [15 25 35 45 55]

# print(arr ** 2)       # [100 400 900 1600 2500]

# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

# print(np.mean(marks_2d))           # Overall mean

# print(np.mean(marks_2d, axis=1))   # Mean per student (row)

# print(np.mean(marks_2d, axis=0))   # Mean per subject (column)

# print(np.max(marks_2d))            # Highest mark

# print(np.std(marks_2d))            # Standard deviation

# arr = np.array([55,82,43,91,67,78,35,88])

# print(arr[arr > 70])   # [82 91 78 88] — only values > 70

import pandas as pd

data = {
    'Name':   ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age':    [22, 21, 23, 20, 24],
    'Marks':  [85, 92, 78, 88, 73],
    'City':   ['Bhopal','Indore','Bhopal','Jabalpur','Indore'],
}
df = pd.DataFrame(data)
print(df)
# Explore the data
print(df.shape)          # (5, 4) — 5 rows, 4 columns
print(df.head(3))        # First 3 rows
print(df.dtypes)         # Data type of each column
print(df.describe())     # Statistical summary

# Select columns
print("df['Name']: \n", df['Name'])                   # Single column → Series
print(df[['Name', 'Marks']])        # Multiple → DataFrame
 
# # Filter rows
print(df[df['Marks'] >= 85])        # High scorers
print(df[df['City'] == 'Bhopal'])   # Bhopal students
