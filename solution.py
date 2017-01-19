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

# import sys
# if len(sys.argv) != 4:
#     print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
# else:
#     try:
#         num1 = int(sys.argv[1])
#         operator = sys.argv[2]
#         num2 = int(sys.argv[3])
#         if operator == "+":
#             print(num1 + num2)
#         elif operator == "-":
#             print(num1 - num2)
#         elif operator == "*":
#             print(num1 * num2)
#         elif operator == "/":
#             print(num1 / num2)
#         elif operator == "%":
#             print(num1 % num2)
#         elif operator == "^":
#             print(num1 ** num2)
#         else:
#             raise
#     except:
#         print('input error')
## Solution plus compexe pour les erreurs
    # else:
    #         raise Exception("Problème !")
    # except Exception as e:
    #     print(e)

# 200 - # Create a function, is_prime, that check if its given number is a prime one
# Provide a script defining the function is_prime(num).
# num is number that the function is_prime takes as a parameter.
# The function is_prime return True if num is a prime number, False otherwise.

# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False

# 204 - # Perfect deck shuffle
# A perfect shuffle of a deck of card is splitting a deck of cards into equal halves, and perfectly interleaving them.
# Perfectly shuffling [1, 2, 3, 4, 5, 6] gives [1, 4, 2, 5, 3, 6].
# You'll expose a perfect_shuffle(deck) function, perfectly shuffling the given iterable.
# Did you know that if you shuffle 10 times a deck of 1024 cards, the deck returns to its initial state ? It's probably a good way to test your implementation.

# import operator
# from itertools import *
# def perfect_shuffle(deck):
#     middle = len(deck)/2
#     half1 = deck[:int(middle)]
#     half2 = deck[int(middle):]
#     shuffled = list(zip_longest(half1, half2, fillvalue='-'))
#     shuffled_as_list = list(chain.from_iterable(shuffled))
#     return shuffled_as_list

# perfect_shuffle(deck)
# perfect_shuffle([1, 2, 3, 4, 5, 6])

## Test: shuffle 10 times a deck of 1024 cards
## Create deck of 1024 cards
# deck1024 = []
# for x in range(1,1025):
#     deck1024.append(x)
# print(deck1024[0])
# print(deck1024[-1])
#
## Shuffle desk1024
# print(perfect_shuffle(deck1024))
# for i in range(1,3):
#     perfect_shuffle(deck1024)
# repeat(perfect_shuffle(deck1024),3)
# print(deck1024)
# print(deck1024[0])
# print(deck1024[-1])
# print(mytest)
#
# test1024 = perfect_shuffle(deck1024)
# print(test1024)
# print(test1024[0])
# print(test1024[-1])


# 210 - # Print the sum of every prime number < 1000

# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False
#
# my_primes = []
# for i in range (0, 1001):
#     if is_prime(i) == True:
#         my_primes.append(i)
#     else:
#         pass
#
# print(sum(my_primes))

# 215 - # Pernicious numbers
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False
#
# numbers = []
# for i in range(222281, 222381):
#     num_bin = bin(i)[2:]
#     total_num_list = []
#     for j in num_bin:
#         total_num_list.append(float(j))
#     total_num_sum = round(sum(total_num_list))
#     if is_prime(total_num_sum):
#         numbers.append(i)
#     else:
#         pass
# for k in numbers:
#     print(k)

# 220 - # Print every prime numbers in a range
# print every prime number in the range [10000;10050], on one line, separated by comas and spaces.
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False
#
# numbers = []
# for i in range(10000,10050):
#     if is_prime(i):
#         numbers.append(i)
#     else:
#         pass
# print(*numbers, sep=', ')

# 230 - # Print the fist prime number after the given one
# Provide a script that prints the first prime number greater than 100000000.
# You may use itertools.count(), and you may need sys.exit().

# from itertools import *
# import sys
#
# def is_prime(num):
#     if num > 1:
#         for i in range(2, int(num ** 0.5)):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False
#
# p = count(100000000)
# for i in p:
#     if is_prime(i):
#         print(i)
#         exit()

# 240 - # Print the head of the fibonacci sequence

# V1 ante corr.
# Consider the fibonacci sequence starting with 1, 2, 3. Provide the script that print the 10 first numbers of this sequence, separated by comas and spaces, end with a dot. Such as:
# 1, 2, 3, X, X, X, X, X, X, X.

# fib = [1, 2, 3]
# for n in range(1, 8):
#     fib.append(fib[-1] + fib[-2])
# print(*fib, sep=', ', end='.')

# fib = [1, 2]
# for n in range(1, 9):
#     fib.append(fib[-1] + fib[-2])
# print(*fib, sep=', ', end='.')

# V2 corrected
# Consider the fibonacci sequence. Provide the script that print the 10 first numbers of this sequence, separated by comas and spaces, end with a dot. Such as:
# 1, 1, 2, 3, X, X, X, X, X, X.

# fib = [1, 1]
# for n in range(1, 9):
#     fib.append(fib[-1] + fib[-2])
# print(*fib, sep=', ', end='.')



# @TODO # 245 - # Student class
# Implement a Student, School, and a City classes like so:
# Student, School, and City have a name attribute, given as construction.
# A Student have an add_exam(mark) method, recoding a new mark for him, as a float.
# A School have an add_student(student) method.
# A City have an add_school(school) method.
# Student, School, and City have a get_mean() method giving:
# For the Student, the average of its results.
# For the School, the average of the students averages.
# For the City the average of the School averages.
# School have a get_best_student() method.
# Cities have a get_best_school() and a get_best_student() methods.

# def get_marks_thib(self):
#     return [m for student in self.students for m in student.marks]
# def get_marks_hack(self):
#     return self.marks

class Student():
    def __init__(self, name):
        self.name = name
        self.marks = []
    def add_exam(self, mark):
        self.marks.append(float(mark))
    def get_mean(self):
        return float((sum(self.marks)) / max(len(self.marks), 1))

class School():
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def get_mean(self):
        return float((sum(self.marks)) / max(len(self.marks), 1))
    def get_best_student(self):
        for student in self.students:
            self.get_mean() # to be continued…

class City():
    def __init__(self, name):
        self.name = name
        self.schools = []
    def add_school(self, school):
        self.schools.append(school)
    def get_mean(self):
        return float((sum(self.marks)) / max(len(self.marks), 1))
    def get_best_school(self):
        for school in self.schools:
            print(self.get_mean())
    def get_best_student(self):
        for student in self.students:
            print(self.get_mean())

def main():
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_marks in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for mark in student_marks:
            student.add_exam(mark)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)

main()

# if __name__ == '__main__':
#     main()

# Thibault's geek joke
# class PhDStudent(Tutor):
#     def __init__(self, topic):
#         super(PhDStudent, self).__init__(self, topic)

# 250 - # Draw N Squares
# You must provide the function draw_n_squares(n) that returns a string of squares, such as:
# print(draw_n_squares(1))
# +---+
# |   |
# +---+
# n is the number of squares on the diagonal.

# def draw_n_squares(n):
#     odd_line = "+---" * n + "+"
#     even_line = "|   " * n + "|"
#     final_line = "+---" * n + "+"
#     return((odd_line + "\n" + even_line + "\n") * n + final_line)
#
# print(draw_n_squares(1))
# print(draw_n_squares(3))
# print(draw_n_squares(5))

# @TODO # 260 - # 3 Ways to Distance

# @TODO # 270 - # Roman Numerals
# Create a to_roman_numeral function converting a given number to Roman Numerals like:
# >>> to_roman_numeral(1)
# 'I'
# >>> to_roman_numeral(2)
# 'II'
# >>> to_roman_numeral(4)
# 'IV'
# >>> to_roman_numeral(8)
# 'VIII'
# >>> to_roman_numeral(16)
# 'XVI'
# >>> to_roman_numeral(32)
# 'XXXII'

# 280 - # Exceptions

# import sys
# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Not enough parameters.")


# 285 - # Doing HTTP requests

# import sys
# import requests
# try:
#     r = requests.get('https://api.github.com/users/python')
#     print(r.text)
# except Exception:
#     print("No internet connectivity.")

# 300 - # Print the content of the file 'words'

# infile = open("words.txt","w+")
# for i in range(1):
#     infile.write("Longtemps\nje\nme\nsuis\ncouché\nde\nbonne\nheure")
# infile.close()

# infile = open("words.txt", "r")
# text = infile.read()
# infile.close()
# print(text)

# 310 - # Count the lower 'e' in the 'words' file
# Your programm have to open the file words.txt, count the 'e', and print the count.

# infile = open("words.txt", "r")
# text = infile.read()
# infile.close()
# count_of_es = 0
# for letter in text:
#     if letter == "e":
#         count_of_es += 1
#     else:
#         pass
# print(count_of_es)

# 320 - # Give the frequency of letters in the 'words' file
# Your programme will have to open the file 'words.txt', compute the frequency of every letters, and display it according to this format:
# b: 0.02
# p: 0.02

# infile = open("words.txt", "r")
# text = infile.read()
# infile.close()
#
# frequencies = {}
# sum_frequencies = 0
# for char in text:
#     if char == "\n":
#         pass
#     elif char in frequencies:
#         frequencies[char] += 1
#         sum_frequencies += 1
#     else:
#         frequencies[char] = 1
#         sum_frequencies += 1
#
# for char, frequency in frequencies.items():
#     print(char,": ", "%.2f" % (frequency/sum_frequencies), sep='')

# 328 - # Multiply all the given parameters
# Write a function, mul, that multiplies all numbers of the given list of numbers.
# like:
# print(mul([1, 2, 3]))
# 6
# print(mul([0, 1, 2, 3]))
# 0
# print(mul([2, 3, 4]))
# 24

# def mul(listnum):
#     count = 1
#     for num in range(0,len(listnum)):
#         count *= listnum[num]
#     return(count)

# 329 - # Largest product in a series
# adjacent_num = 4
# products_of_four = []
# for num in range(0,1000 - adjacent_num - 1):
#     countnum = 1
#     for i in range(0,adjacent_num):
#         countnum *= int(euler_number[num+i])
#     products_of_four.append(countnum)
# print(max(products_of_four))

# euler_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# euler_number = str(euler_number)
#
# adjacent_num = 13
# products_of_thirteen = []
# for num in range(0,(1000 - adjacent_num - 1)):
#     countnum = 1
#     for i in range(0,adjacent_num):
#         countnum *= int(euler_number[num+i])
#     products_of_thirteen.append(countnum)
# print(max(products_of_thirteen))


# @TODO # 350 - # bencode / bdecode
# @TODO # 440 - # Lambda expressions
# @TODO # 450 - # Caesar Cypher
# @TODO # 455 - # Py Master Mind
# @TODO # 456 - # Solve Mind
# @TODO # 461 - # Optimization 101
# @TODO # 500 - # Largest product in a grid
# @TODO # 501 - # Change for 42€
# @TODO # 515 - # Sequence Mining
# @TODO # 525 - # Longest Collatz sequence
# @TODO # 600 - # Elementary cellular automaton
# @TODO # 700 - # Make your own 2048 in python !
# @TODO # 705 - # Evolve mind
# @TODO # 715 - # Sapin
# @TODO # 742 - # Be creative, import math
