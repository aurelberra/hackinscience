# Hackinscience Exercises

# 3
# print("Hello World")

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

# 5 Write a script named solution.py that prints 42 -- Use the print() function.
# print(42)

# 6 Write a script named solution.py print its own file name.
# import sys
# print(sys.argv[0])

# 7 Write a script named solution.py that prints the list ["Hello world", 42]
# a = "Hello world"
# b = 42
# print([a, b])
# print(["Hello world", 42])

# 8 Write a script named solution.py that prints "Hello World !" vertically. You must use the print() function only once in your script.
# text = "Hello World !"
# for i in text:
#     print(i)

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

# 11 Provide a script solution.py that prints Hello World one hundred times, one line per each.
# for i in range (1,101):
#     print("Hello World")

# 12 Write a script named solution.py that print the factorial of 27, by using the factorial function from the math module.
# import math
# print(math.factorial(27))

# 13 Provide a script solution.py that prints what python think about 2 + 2 not being equal to 5.
# a = 2 + 2
# b = 5
# print(a != b)

# 14 Write a script named solution.py that print the first parameter given to the script. If thereis no parameters given, it should print the following error message : usage: python3 solution.py PARAM.
# import sys
# if len(sys.argv) > 1:
#     print(sys.argv[1])
# else:
#     print('usage: python3 solution.py PARAM')

# 15 Make a python script that print the result for 245850922 / 78256779 on one line, and the result of (1 + √5) / 2 on the next.
# print(245850922 / 78256779)
# print((1 + 5**0.5) / 2)

# 16 Write a script named solution.py that prints "abcdefghijklnmopqrstuvwxyz", using the print() function.
# print("abcdefghijklnmopqrstuvwxyz")

# 17 Write a script named solution.py that print the result of simple addition. If no parameters are given, you must print the following error message : usage: python3 solution.py OP1 OP2.
# import sys
# if len(sys.argv) != 3:
#     print('usage: python3 solution.py OP1 OP2')
# else:
#     print(int(sys.argv[1]) + int(sys.argv[2]))

# 18 Write a script named solution.py that print the result of simple substraction. If no parameters is given, you must print the following error message: usage: python3 solution.py OP1 OP2.
# import sys
# if len(sys.argv) != 3:
#     print('usage: python3 solution.py OP1 OP2')
# else:
#     print(int(sys.argv[1]) - int(sys.argv[2]))

# 19 Write a program called solution.py that print the actual date (day month year hour minute and seconds) in a human readable format
# import datetime
# print("Today is", datetime.date.today(), "and it is", datetime.datetime.now().strftime('%H:%M:%S'))

# 20 Write a script names solution.py that prints every even numbers between 1 and 100 inclusive, one line per each.
# for i in range (1,101):
#     if i % 2 != 0:
#         pass
#     else:
#         print(i)

# 21 Provide a script solution.py that prints the sum of every even numbers in the range [0; 100]
# sum = 0
# for i in range (0,101):
#     if i % 2 != 0:
#         pass
#     else:
#         sum += i
# print(sum)

# 22 Provide the script solution.py where you define a function sqrt(num), where num is a number and sqrt a funtion that returns the square root of num.
def sqrt(num)
# to be continued…
