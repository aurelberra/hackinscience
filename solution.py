# Hackinscience Exercises

# 001 - # Strings
# 002 - # Numbers

# 003 - # Hello World
# print("Hello World")

# 004 - # Print Rev Alpha
# 4 Write a program that print the reverse alphabet with the vowels capitalised.
# zyxwvUtsrqpOnmlkjIhgfEdcbA
# print('zyxwvUtsrqpOnmlkjIhgfEdcbA')
## Not validated online: the expected solution was much easier
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# vowels = ['a','e','i','o','u']
# for i in range (0,len(alpha)):
#     if alpha[len(alpha)-i-1] in vowels:
#         print(str.upper(alpha[len(alpha)-i-1]), end='')
#     else:
#         print(alpha[len(alpha)-i-1], end='')

# 005 - # 42
# 5 Write a script named solution.py that prints 42 -- Use the print() function.
# print(42)

# 006 - # Print parameters
# 6 Write a script named solution.py print its own file name.
# import sys
# print(sys.argv[0])

# 007 - # Simple list
# 7 Write a script named solution.py that prints the list ["Hello world", 42]
# a = "Hello world"
# b = 42
# print([a, b])
# print(["Hello world", 42])

# 008 - # Basic loop
# 8 Write a script named solution.py that prints "Hello World !" vertically. You must use the print() function only once in your script.
# text = "Hello World !"
# for i in text:
#     print(i)

# 009 - # Characters counting
# 9 Write a script named solution.py that prints the number of characters in paragraph.
# phantom_menace = """Turmoil has engulfed the Galactic Republic. The\
#  taxation of trade routes to outlying star systems is in\
#  dispute. Hoping to resolve the matter with a blockade of deadly\
#  battleships, the greedy Trade Federation has stopped all shipping to\
#  the small planet of Naboo. While the congress of the Republic\
#  endlessly debates this alarming chain of events, the Supreme\
#  Chancellor has secretly dispatched two Jedi Knights, the guardians of\
#  peace and justice in the galaxy, to settle the conflict"""
# paragraph = phantom_menace
# print(len(paragraph))

# 010 - # Counting Words
# 10 Provide the script solution.py that prints the number of words of the paragraph
# phantom_menace = """Turmoil has engulfed the Galactic Republic. The\
#  taxation of trade routes to outlying star systems is in\
#  dispute. Hoping to resolve the matter with a blockade of deadly\
#  battleships, the greedy Trade Federation has stopped all shipping to\
#  the small planet of Naboo. While the congress of the Republic\
#  endlessly debates this alarming chain of events, the Supreme\
#  Chancellor has secretly dispatched two Jedi Knights, the guardians of\
#  peace and justice in the galaxy, to settle the conflict"""
# words = phantom_menace.split()
# print(len(words))

# 011 - # Print Hello World, 100 times
# 11 Provide a script solution.py that prints Hello World one hundred times, one line per each.
# for i in range (1,101):
#     print("Hello World")

# 012 - # Import
# 12 Write a script named solution.py that print the factorial of 27, by using the factorial function from the math module.
# import math
# print(math.factorial(27))

# 013 - # Maybe for very large values of 2
# 13 Provide a script solution.py that prints what python think about 2 + 2 not being equal to 5.
# a = 2 + 2
# b = 5
# print(a != b)

# 014 - # Print the first parameter
# 14 Write a script named solution.py that print the first parameter given to the script. If thereis no parameters given, it should print the following error message : usage: python3 solution.py PARAM.
# import sys
# if len(sys.argv) > 1:
#     print(sys.argv[1])
# else:
#     print('usage: python3 solution.py PARAM')

# 015 - # Using operators
# 15 Make a python script that print the result for 245850922 / 78256779 on one line, and the result of (1 + √5) / 2 on the next.
# print(245850922 / 78256779)
# print((1 + 5**0.5) / 2)

# 016 - # Print Alpha
# 16 Write a script named solution.py that prints "abcdefghijklnmopqrstuvwxyz", using the print() function.
# print("abcdefghijklnmopqrstuvwxyz")

# 019 - # my add
# 17 Write a script named solution.py that print the result of simple addition. If no parameters are given, you must print the following error message : usage: python3 solution.py OP1 OP2.
# import sys
# if len(sys.argv) != 3:
#     print('usage: python3 solution.py OP1 OP2')
# else:
#     print(int(sys.argv[1]) + int(sys.argv[2]))

# 020 - # my sub
# 18 Write a script named solution.py that print the result of simple substraction. If no parameters is given, you must print the following error message: usage: python3 solution.py OP1 OP2.
# import sys
# if len(sys.argv) != 3:
#     print('usage: python3 solution.py OP1 OP2')
# else:
#     print(int(sys.argv[1]) - int(sys.argv[2]))

# 025 - # my date
# 19 Write a program called solution.py that print the actual date (day month year hour minute and seconds) in a human readable format
# import datetime
# print("Today is", datetime.date.today(), "and it is", datetime.datetime.now().strftime('%H:%M:%S'))

# 030 - # Print even numbers in the range [1; 100]
# 20 Write a script names solution.py that prints every even numbers between 1 and 100 inclusive, one line per each.
# for i in range (1,101):
#     if i % 2 != 0:
#         pass
#     else:
#         print(i)

# 040 - # SUM of pairs numbers <= 100
# 21 Provide a script solution.py that prints the sum of every even numbers in the range [0; 100]
# sum = 0
# for i in range (0,101):
#     if i % 2 != 0:
#         pass
#     else:
#         sum += i
# print(sum)

# 045 - # First function
# 22 Provide the script solution.py where you define a function sqrt(num), where num is a number and sqrt a funtion that returns the square root of num.
# use `return`, not `print`!
# def sqrt(num):
#    "This function prints the square root of number `num`"
#    num_sqrt = num ** 0.5
#    return(num_sqrt)
#
# def sqrt(num):
#     "This function prints the square root of number `num`"
#     num_sqrt = num ** 0.5
#     if num == 0:
#         return(0)
#     else:
#         return(num_sqrt)

# 050 - # Multiples of 3 and 5
# 23 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000 and print it with a script named solution.py.
# sum = 0
# for i in range (0,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
#     else:
#         pass
# print(sum)

# 060 - # Print every two letters pairs
# 24 Provide the script solution.py that prints every possible pairs of two letters, only lower case, one by line, ordered alphabetically.
# alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range (0,len(alpha)):
#     letter1 = str.lower(alpha[i])
#     for j in range (0,len(alpha)):
#         letter2 = str.lower(alpha[j])
#         j += 1
#         letters = letter1 + letter2
#         print(letters)
#     i += 1

# 070 - # Print every two letters pairs, without duplicates
# 25 Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically, but that skip duplicates, such as 'aa', 'bb', etc...
# alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range (0,len(alpha)):
#     letter1 = str.lower(alpha[i])
#     for j in range (0,len(alpha)):
#         letter2 = str.lower(alpha[j])
#         j += 1
#         letters = letter1 + letter2
#         if letter1 != letter2:
#             print(letters)
#         else:
#             pass
#     i += 1

# 080 - # Print combinations of two lower case letters
# 26 Print every possible combinations of 2 lowercase letters, one by line.
# alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range (0,len(alpha)):
#     letter1 = str.lower(alpha[i])
#     for j in range (i+1,len(alpha)):
#         letter2 = str.lower(alpha[j])
#         j += 1
#         letters = letter1 + letter2
#         if letter1 != letter2:
#             print(letters)
#         else:
#             pass
#     i += 1

# 055 - # Distance
# 72 Create a dist function, receiving a list of numbers (integers or floating points), and returning the bigger distance between any two given values, so typically the distance between the biggest and the smallest, like:
# def dist(listnum):
#     listnum_dist = max(listnum) - min(listnum)
#     return(listnum_dist)

# 085 - # sort_students
# 1 Write a function sort_a_list that takes a list as argument and return the list sorted in the descending order, such as:
# l = [1, 3, 2, 4, 6, 5, 9, 7]
# def sort_a_list(l):
#     l.sort(reverse=True)
#     return(l)
# sort_a_list(l)

# 2 Given a list where each element is a list of a mark, and a student name, such as:
# Write a function sort_by_mark that take as argument a similar list and returns it sorted by mark in the descending order.
# my_class = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'], [84, 'Joseph Pedersen'], [12, 'Bonnie Torres'], [36, 'John Freeman'], [27, 'Betty Askins'], [22, 'Mark Osbourne'], [42, 'Lidia Robel']]
# def sort_by_mark(l):
#     l.sort(reverse=True)
#     return(l)
# sort_by_mark(my_class)

# 3 Sort by name
# my_class = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'], [84, 'Joseph Pedersen'], [12, 'Bonnie Torres'], [36, 'John Freeman'], [27, 'Betty Askins'], [22, 'Mark Osbourne'], [42, 'Lidia Robel']]
# from operator import itemgetter
# def sort_by_name(l):
#     sorted_l = sorted(l, key=itemgetter(1))
#     return(sorted_l)

# # With OrderedDict, it works but this is not the output format expected by the validator
# from collections import OrderedDict
# from operator import itemgetter
# def sort_by_name(l):
#     dict(l)
#     sorted_l = OrderedDict(sorted(l, key=itemgetter(1)))
#     return(sorted_l)
# sort_by_name(my_class)

# all
# def sort_a_list(l):
#     l.sort(reverse=True)
#     return(l)
#
# def sort_by_mark(l):
#     l.sort(reverse=True)
#     return(l)
#
# from operator import itemgetter
# def sort_by_name(l):
#     sorted_l = sorted(l, key=itemgetter(1))
#     return(sorted_l)

# 097 - # Sets of love
# # 1
# alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
# bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
#
# def love_meet(bob, alice):
#     tryst = []
#     for i in range(len(alice)):
#         if alice[i] in bob:
#             tryst.append(alice[i])
#             i += 1
#         else:
#             pass
#             i += 1
#     return(set(tryst))
#
# love_meet(bob, alice)
#
# # 2
# alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
# bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
# silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']
#
# def affair_meet(bob, alice, silvester):
#     tryst = []
#     for i in range(len(alice)):
#         if alice[i] in silvester and alice[i] not in bob:
#             tryst.append(alice[i])
#             i += 1
#         else:
#             pass
#             i += 1
#     return(set(tryst))
#
# affair_meet(bob, alice, silvester)

# 107 - # Select students
# my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]
#
# from operator import itemgetter
# def select_student(my_class, mark):
#     accepted = []
#     refused = []
#     for item in my_class:
#         if item[1] >= mark:
#             accepted.append(item)
#         else:
#             refused.append(item)
#     results = {'Accepted': sorted(accepted, key=itemgetter(1), reverse=True),
#         'Refused': sorted(refused, key=itemgetter(1))}
#     return(results)

# 110 - # calculator1
# Write a program that do basic calculations. You need to be able to get basic operators such as +, - , *, /, % and ^. Input will integer numbers.
# Your program will give a usage message if you don't give the three parameters.
# For every other errors like if an operand is not an integer, you'll print an input error.

import sys
def calculator(num1, operator, num2):
    if len(sys.argv) != 1:
        print('Please enter two numbers exactly.')
    # elif num1 or num2
    elif:
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "%":
            print(num1 % num2)
        elif operator == "^":
            print(num1 ^ num2)
    else:
        print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')

# 200 - # Create a function, is_prime, that check if its given number is a prime one
# 204 - # Perfect deck shuffle
# 210 - # Print the sum of every prime number < 1000
# 215 - # Pernicious numbers
# 220 - # Print every prime numbers in a range
# 230 - # Print the fist prime number after the given one
# 240 - # Print the head of the fibonacci sequence
# 250 - # Draw N Squares
# 260 - # 3 Ways to Distance
# 270 - # Roman Numerals
# 280 - # Exceptions
# 285 - # Doing HTTP requests
# 300 - # Print the content of the file 'words'
# 310 - # Count the lower 'e' in the 'words' file
# 320 - # Give the frequency of letters in the 'words' file
# 328 - # Multiply all the given parameters
# 329 - # Largest product in a series
# 350 - # bencode / bdecode
# 440 - # Lambda expressions
# 450 - # Caesar Cypher
# 455 - # Py Master Mind
# 456 - # Solve Mind
# 461 - # Optimization 101
# 500 - # Largest product in a grid
# 501 - # Change for 42€
# 515 - # Sequence Mining
# 525 - # Longest Collatz sequence
# 600 - # Elementary cellular automaton
# 700 - # Make your own 2048 in python !
# 705 - # Evolve mind
# 715 - # Sapin
# 742 - # Be creative, import math
