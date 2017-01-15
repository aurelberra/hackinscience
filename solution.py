# Hackinscience Exercises

# 3
# print("Hello World")

# 4
# Write a program that print the reverse alphabet with the vowels capitalised.
# zyxwvUtsrqpOnmlkjIhgfEdcbA
alpha = "abcdefghijklmnopqrstuvwxyz"
vowels = ['a','e','i','o','u']
for i in range (0,len(alpha)):
    if alpha[len(alpha)-i-1] in vowels:
        print(str.upper(alpha[len(alpha)-i-1]), end='')
    else:
        print(alpha[len(alpha)-i-1], end='')
