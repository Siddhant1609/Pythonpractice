#
# # Question 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# number = int(input())
# 1500<= number <= 2700
# if number % 7 ==0 and number % 5 ==0:
#  print("Yes number is divisible by 7 and multiple of 5")
# elif number < 1500:
#  print(" Wrong number")
# else:
#     print("No number is divisible by 7 and multiple of 5")
#
#  #Question 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#   #            [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# degree_celcius = int(input("Enter the temperature in degree celcius"))
# degree_fahrenheit = (9* degree_celcius)/5 +32
# print("Your temp in degree Fahrenheit is:" + str(degree_fahrenheit))
#
# #Question 3. Write a Python program to guess a number between 1 and 9.
#  #           Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
#   #           on successful   guess, user will get a "Well guessed!" message, and the program will exit
# number = int(input("Enter the number"))
#
# if 1<=number <= 9:
#  print("Well guesed")
# else:
#  print("Wrong guesed")
#
# #Question 4.Write a Python program that accepts a word from the user and reverses it.
# sentence = input("Enter the String: ")
# if sentence[::-1] == sentence:
#  print("Sentence is palindrome --> " + sentence)
# else:
#  print("Sentence is not a palindrome -->"+ sentence)
#
#
# #Question 5:  Write a Python program to count the number of even and odd numbers in a series of numbers
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
#
# even_count = len([num for num in numbers if num % 2 == 0])
# odd_count = len(numbers) - even_count
#
# print("Number of even numbers:", even_count)
# print("Number of odd numbers:", odd_count)
#
#
# #Question 6:  Write a Python program that iterates the integers from 1 to 50.
# #For multiples of three print "Fizz" instead of the number and for multiples of
# #five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# numbers = input("Enter the numbers separated by spaces: ").split()
#
# for num_str in numbers:
#     num = int(num_str)
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#
#  #Question 7: Write a Python program to calculate a dog's age in dog years.
#   #  Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# human_age = int(input("Enter the age of the dog in human years: "))
#
# if human_age <= 2:
#     dog_years = human_age * 10.5
#     print("Dog Year: " + str(dog_years))  # Convert dog_years to a string for concatenation
# else:
#     dog_years = (2 * 10.5 + (human_age - 2) * 4)
#     print("Dog Year: " + str(dog_years))  # Convert dog_years to a string for concatenation
#
#
# #Question 8: Write a Python program to check whether an alphabet is a vowel or consonant.
# alphabet = input("Enter the Alphabet ")
# vowels = "a,e,i,o,u,A,E,I,O,U"
# if alphabet in vowels :
#     print("It is a vowel character")
# else:
#     print("It is a consonant")
#
#
# #Question 9: Write a Python program to convert a month name to a number of days.
# #Dictionary mapping month names to their corresponding number of days
# month_days = {
#     "January": 31,
#     "February": "28 or 29",
#     "March": 31,
#     "April": 30,
#     "May": 31,
#     "June": 30,
#     "July": 31,
#     "August": 31,
#     "September": 30,
#     "October": 31,
#     "November": 30,
#     "December": 31,
#     "january": 31,
#     "february": "28 or 29",
#     "march": 31,
#     "april": 30,
#     "may": 31,
#     "june": 30,
#     "july": 31,
#     "august": 31,
#     "september": 30,
#     "october": 31,
#     "november": 30,
#     "december": 31
# }
# month_name = input("Enter month name: ")
# if month_name in month_days:
#     print("Number of days is:", month_days[month_name])
# else:
#     print("Wrong month name")
#
# #Question 10:  Write a Python program to check if a triangle is equilateral, isosceles or scalene
# side1 = int(input("Enter the side 1"))
# side2 = int(input("Enter the side 2"))
# side3 = int(input("Enter the side 3"))
# if side1 == side2 == side3:
#     print("It is an Equilateral Triangle")
# elif side1 == side2 or side2 ==side3 or side3 == side1:
#     print("It is an Isoscelene Triangle")
# else:
#     print("The triangle is Scalene")
import random

#Question 11. Program to find how many days, weeks and months left in your rest life.
# age = int(input("Enter your age"))
# year_left = 100-age
# days_left = year_left*365
# month_left = year_left * 12
# weeks_left  = year_left*52
#
# print(f"My age is {age}.I have {year_left} years, {weeks_left} weeks, {days_left} days,{month_left} months")

#Question 12. Write a program to show that if you are height is greater than 3 feet you have to take the token otherwise not
# height = int(input("Enter the height in feet"))
# if height>3:
#     print("You have to take the token \n Now you an board the train")
# else:
#     print("No token required \n You can board without token"

#QUESTION 13.
# height = int(input("What is your height -->"))
# bill = 0
# if height >= 3:
#     print("can ride")
#     age = int(input("what is your age -->"))
#     if age <12:
#         bill = 150
#         print("Tickect price is 150 rupees")
#     elif age <= 18:
#         bill = 250
#         print("Ticket price is 250 rupees")
#     else:
#         bill = 500
#         print("Ticket price is 500 Rupees")
#     want_photo = input("Do you want to take photo(Y/N) -->")
#     if want_photo == "y" or want_photo == "Y":
#         bill += 50
#     print(f" Your total bill is {bill}")
# else:
#     print("Can't Ride")
# print("bye, Have a nice day")

# Question 14
# size = input("Enter what size of pizza you want(S/M/L)?" )
# bill = 0
# if size == "s" or size == "S":
#     bill += 100
#     print("Small pizza prize is 100 rupees")
# elif size == "m" or size == "M":
#     bill += 200
#     print("Medium pizza is of 200 rupees")
# else:
#     bill += 300
#     print("Large pizza is of 300 rupees")
#
# add_pepperoni = input("Do you want to add pepperoni(Y/N)")
# if add_pepperoni == "y" or add_pepperoni == "Y":
#     if size == "s" or size == "S":
#         bill += 30
#     else:
#         bill += 50
#
# extra_cheese = input("Do you want to add extra_cheese")
# if extra_cheese == "y" or extra_cheese == "Y":
#         bill += 20
#
# print(f"Your final bill is {bill} rupees")

#Question 15 : LOVE CALCULATOR
# name1 = input("Enter the name")
# name2 = input("Enter the name")
# combine_String = name1 + name2
# lower_case_String = combine_String.lower()
# t = lower_case_String.count('t')
# r = lower_case_String.count('r')
# u = lower_case_String.count('u')
# e = lower_case_String.count('e')
# true = t+r+u+e
#
# l = lower_case_String.count('l')
# o = lower_case_String.count('o')
# v = lower_case_String.count('v')
# e = lower_case_String.count('e')
# love = l+o+v+e
#
# love_score = int(str(true)) + int(str(love))
#
# if love_score <10  or love_score > 90:
#     print(f"Your score is{love_score} and you go together like coke and mentos")
# elif love_score >= 40 and love_score<= 50:
#     print(f"Your score is{love_score} and you are alright together")
# else:
#     print(f"Your love score is {love_score}")

#
# size = input("Enter what size of pizza you want(S/M/L)? ")
# bill = 0
#
# # Calculate base price based on size
# if size.lower() == "s":
#     bill += 100
#     print("Small pizza price is 100 rupees")
# elif size.lower() == "m":
#     bill += 200
#     print("Medium pizza price is 200 rupees")
# else:
#     bill += 300
#     print("Large pizza price is 300 rupees")
#
# # Add pepperoni based on user input
# add_pepperoni = input("Do you want to add pepperoni (Y/N)? ")
# if add_pepperoni.lower() == "y":
#     if size.lower() == "s":
#         bill += 30
#     else:
#         bill += 50
#
# # Add extra cheese based on user input
# extra_cheese = input("Do you want to add extra cheese (Y/N)? ")
# if extra_cheese.lower() == "y":
#     bill += 20
#
# print(f"Your final bill is {bill} rupees")

import _random
import sys

#a = random.randint(1,7)  any random number can be taken from 1 to 7
#a = random.randrange(1,3) in this a random number is taken from 1 to 3 but 3 is not taken
#a = random.random()  it chooses any number randomly
#a = random.uniform(1,3) it can take any number randomly from 1 and 2 it will not include 3
# l = [2,45,3,5,6,4,3,2,4,5,5,3,224343,32,24,3,23,3,44]
# a = random.choice(l)  it choose any number with in the list
# l = [2,45,3,5,6,4,3,2,4,5,5,3,224343,32,24,3,23,3,44]
# random.shuffle(l)
# print(l)

#
# class change:
#     def __init__(self, x, y, z):
#         self.a = x + y + z
#
#
# x = change(1, 2, 3)
# y = getattr(x, 'a')
# setattr(x, 'a', y + 1)
# print(x.a)

# class A:
#     def __init__(self,name):
#         self.name=name
# a1=A("john")
# a2=A("john")

# Ques1: Print First 10 natural numbers using for loop
# for i in range(1,11):
#     print(i)
#
# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# # 1 2 3 4 5
# depth = int(input())
# for i in range(1, depth+1):
#     print("*" * i)
#
# Exercise 3: Calculate the sum of all numbers from 1 to a n number (n is of yours choice)
# number = int(input())
# sum = 0
# for i in range(1,number+1):
#     sum +=i
#     print("Sum up to", i, ":", sum)
#
# Exercise 4: Write a program to print multiplication table of a given number (format i * 1 = i)    THODA PROBLEM HAI
# number = int(input())
# for i in range(1, number+1):
#     print(f"{number} * {i} = {number*i}")
#
# Exercise 5: Display numbers from a list using loop
# lst  = [56,45,85,47,54,32,14,25,28,26,28,277]
# for i in range(0,len(lst)):
#     print(lst[i])
#
# Exercise 6: Count the total number of digits in a number (for example 765432 = 6 digits)
# number = int(input())
# number_digit = len(str(number))
# print("The total number of digits in number is :", number_digit)
#
# Exercise 7: Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
#
# Exercise 7: Print the following pattern
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
#
# depth = int(input())
# for i in range (depth, 0,-1):
#     print(str(i)* i )
#
# Exercise 8: Print list in reverse order using a loop
# lst = [45,65,25,3,13,45,88,96,74,45]
# for i in range(len(lst)-1,-1,-1):
#     print(lst[i], end=" ")
#
# Exercise 9: Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i, end =" ")
#
# Example 10: Use else block to display a message “Done” after successful execution of for loop
# 0
# 1
# 2
# 3
# 4
# Done!
# for i in range(6):
#     print(i)
# else:
#     print("Done!")
#
# Exercise 11: Write a program to display all prime numbers within a range 1 to 50
# print("Prime numbers within the range 1 to 50:")
# for number in range(1, 51):
#     if number > 1:
#         is_prime = True
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(number, end=",")
#
# Exercise 12: Display Fibonacci series up to 10 terms
# a, b = 0,1
# for i in range(19):
#     print(a, end=",")
#     a,b = b, a+b
#
# Exercise 13: Find the factorial of a given number
# numbers = int(input())
# for i in range (1, numbers+1):
#     if numbers%i == 0:
#         print(i, end=",")
#
# Exercise 14: Reverse a given integer number (like 1234567 should be 7654321)
# numbers = input("Enter the number")
# reversed_number = numbers[::-1]
# print(reversed_number)
#
# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# for ex.. my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] and result should be like print the number which are present at the odd index.
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(len(my_list)):
#     if i%2 !=0:
#         print(my_list[i], " Index Numbers", i)
#
# Exercise 16: Calculate the cube of all numbers from 1 to a n number
# numbers = int(input())
# for i in range(1,numbers+1):
#     print(f"Cube of number {i} is {i**3}")
#
# Exercise 17: Find the sum of the series upto n terms
#     like this -- Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become
#    2 + 22 + 222 + 2222 + 22222 = 24690
# n = int(input("Enter the value of terms: "))
# sum_series = 0
# term = 0
# for i in range(1,n+1):
#     term = term*10+2
#     sum_series += term
# print("Sum of the series upto", n ," term is ", sum_series)
#
# Exercise 18: Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# depth = int(input())
# for i in range(1, depth+1):
#     print("*" * i)
# for i in range(depth-1, 0, -1):
#     print("*" * i)

# ex = 'hello'
# print(ex[ -5 : 1 ])
#
#
#
# ex = [ 1,2,3,4]
# sorted_value = ex.sort()
# print(sorted_value([0+2]-[1+3]))

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print()


# n = int(input("eNTER THE NUMBER"))
# sum  = 0
# for i in range(1, n+1):
#     sum = sum + 1/i
# print(sum)

# n = int(input()) # 54336
# n_str = str(n) # '54336'
#
# mul = 1
# for i in n_str: # '54336'
#   mul = mul * int(i)
#
# print(mul)


# QUESTIONS

# word  = 'Google colab'
# word[6] == word[-7]
#
# str = 'hello world'
# str = str.replace('HELLO','hello')

# num = (3,5,6,7,8,9)
# num [4] = 100
# print(num)

#
# num_lst = [1,3,4,5,6,7,8,9]
# num_set = {1,3,4,5,6,7,8,9}
# num_str = '1,3,4,5,6,7,8,9'
# num_tpl = (1,3,4,5,6,7,8,9)
# print(sys.getsizeof(num_lst))
# print(sys.getsizeof(num_set))
# print(sys.getsizeof(num_str))
# print(sys.getsizeof(num_tpl))

# lst = [2,3,4,[54,67,345,56],True,[764,564]]
# print(lst[3][2])
# print(lst[-1][0])

# lst = [30, 'IN', [45,2547,56],[['Indexing','PYTHON'],['QUERY','JAVA']]]
# # Write the code to excess the indexing value of, PYTHON , 2547 and Indexing
# print(lst[3][0][1])
# print(lst[2][1])
# print(lst[3][0][0])

#FUNCTION
# def factorial(n):
#     if n==0:
#         fact =1
#     else:
#         fact =1
#         for i in range(1, n+1):
#             fact = fact*i
#     return fact
#
# def print_factorial(n):
#     result = factorial(n)
#     print(f"the factorial of {n} is:", result)
#
# print_factorial(7)
#
#
# # Permutatin and combination
# n = int(input())
# r = int(input())
# print(factorial(n)/factorial(n-r))


# def add (a,b):
#     s = a+b
#     return s
#
# a = int(input())
# b = int(input())
# s = a+b
# print(s)

# def string_repeat(s,n):
#     repeat = s*n
#     return repeat
#
# s = 'Almabetter'
# n =3
# print(string_repeat(s,n))

# def calculator(n1,n2):
#     def add(n1,n2):
#         return n1+n2
#     def subtract(n1,n2):
#         return n1-n2
#     if n1 == 0:
#         print(-n2)
#     else:
#           print(n1-n2)
#     def multiply(n1,n2):
#         return n1*n2
#     def divide(n1,n2):
#         return n1/n2
#     if n1 == 0:
#         print("Result not found")
#     else:
#         print(n1/n2)
#
#
# n1 = int(input("Enter the number:"))
# n2 = int(input("Enter the number:"))
# sign = input("Enter the sign +,-,/,*:")
# if sign == "+":
#     print("Add:", n1+n2)
# elif sign == "-":
#     print("Substraction:",n1-n2)
# elif sign == "*":
#     print("Multiplication:", n1*n2)
# elif sign == "/":
#     print("Divide:", n1/n2)
# else:
#     print("Invalid sign")


#
# def list_pow(l,n=1):
#     op_result = []
#     for i in l:
#         op_result.append(i**n)
#     return op_result
#
# result1  =  list_pow(l = [1,2,3,4], n=2)
# result2  = list_pow(l = [1,2,3,4], n=3)
# print("Result 1:", result1)
# print("Result 2:", result2)

# def series_sum(limit):
#     total = 0
#     for i in range(limit+1):
#         if i % 2 == 0:
#             total = total+ i**2
#         else:
#             total = total+i**3
#     return total
#
# print(series_sum(limit=5))

# def sum_digits(n):
#     total = 0
#     for i in str(n):
#         total = total + int(i)
#     return total
#
# print(sum_digits(123456789))

# def consonant(w):
#     s = ' '
#     for i in w:
#         if i.lower() not in 'aeiou':
#             s = s+i
#     return s
#
# print(consonant(w = 'ALMABETTER'))

# def multiply (a,b):
#     m= a*b
#     return m
#
# a = 4
# b = 6
# result = multiply(a,b)
# print(result)
#
# m1 = 10 # global variable
# def multiply(a,b):
#     m1 = 6 # local variable
#     m =a*b
#     return m
#
# a = 4
# b= 5
# result= multiply(a,b)
# print(result)
#
# def word_consonant(s):
#     global op
#     op = ''
#     for i in s:
#         if i.lower() not in "aeiou":
#             op = op +i
#     return op
# word_consonant("Hello excuse me miss")
# print(op)


# def even_odd(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
#
# result = even_odd(95)
# print(result)


# books = {"HARRY POTTER": 10, "HANUMAN": 5, "RAMAYAN": 3, "SHREE KRISHNA": 8, "MAHABHARAT": 5}
#
# def book_inventory(books):
#     output = {}
#     for book, quantity in books.items():
#         if quantity < 10:
#             output[book] = quantity
#     return output
#
# result = book_inventory(books)
# print(result)


#ADVANCE LOOPING CONCEPT
# ex = [23,47,78,90]
# def multiply(n):
#     return(n*9)
# print(list(map(multiply,ex)))

# def square(n):
#     return n**6
# ex = [3,9,7,5]
# print(list(map(square,ex)))


# def odd_even_pow(n):
#     if n%2 == 0:
#         result = n**2
#     else:
#         result = n**3
#     return result
# ex = list(range(1,11))
# print(list(map(odd_even_pow,ex)))

# ex = ['data','Science','Engineering','Art','Commerce']
# def reverse(l):
#     return l[::-1]
# print(list(map(reverse,ex)))

# ex = ['Mr.John', 'Ms.Siya','Mrs.tara','Mr.Tonny']
# def gender(n):
#     if n.split('.')[0] == 'Mr':
#         result = 'Male'
#     else:
#         result = 'Female'
#     return result
#
# print(list(map(gender,ex)))

# # Get the input string from the user
# input_string = input("Enter a string: ")
#
# # Initialize an empty dictionary to store character frequencies
# char_freq = {}
#
# # Iterate through each character in the input string
# for char in input_string:
#     # Check if the character is already in the dictionary
#     if char in char_freq:
#         # If yes, increment its frequency
#         char_freq[char] += 1
#     else:
#         # If not, add it to the dictionary with frequency 1
#         char_freq[char] = 1
#
# # Print the character frequency dictionary
# print(char_freq)

#
# month_name = input("Enter the month name: ")
# if month_name in ['January','March','May','July','August','October', 'December']:
#     print( "No. of days: 31 days")
# elif month_name == 'February':
#     print("No. of days: 28 or 29")
# elif month_name in ['April','June','September','November']:
#     print("No.of days: 30 days ")
# else:
#     print("Invalid Month Name")

# number = int(input("Enter the number: "))
# if number == 0:
#     print("Number is zero")
# elif number > 0:
#     print("It is a positive number")
# else:
#     print("It is a negative number")

#
# word = input("Enter the word: ")
# word_rev = word[::-1]
# print(word_rev)

#given a  list of integer and find and print all the even  number in the list
# number = [10,21,17,97,34,45,68,73,84]
# ex_output = []
# for i in number:
#     if i%2 == 0:
#         ex_output.append(i)
# print(ex_output)
# print(sorted(ex_output))
# print(tuple(ex_output))

# sentence = input("Enter the sentence: ")
# s_word = sentence.split('')
# word_len = []
# for i in s_word:
#     len_i = len(i)
#     word_len.append(len_i)
# print(word_len)

# output_lst  = []
# for i in range (23,80):
#     if i%3 == 0:
#         output_lst.append(i)
# print(output_lst)

# word = input()
# output_str = ''
# for i in word:
#     if i.lower() in ('a','e','i','o','u'):
#         output_str = output_str + i
# print(set(output_str))

# index = eval(input())
# output = ''
# for i in index:
#     output = output + word[i]
# print(output)

# ex = [23,24,26,10,56,23,67]
# maximum = ex[0]
# for i in ex:
#     if i> maximum:
#         maximum = i
# print(maximum)

# sentence = 'Python is an interesting language'
# word = sentence.split(' ')
# longest_word = word[0]
# for i in word:
#     if len(i)> len(longest_word):
#         longest_word = i
# print(longest_word)
#
# ex = [32, 31,30,27,24,34,31,25]
# minimum = ex[0]
# for i in ex:
#     if i< minimum:
#         minimum = i
# print(minimum)

# word = input("Enter the word: ")
# output_dict = {}
# for i in word:
#     count_i = word.count(i)
#     output_dict[i] = count_i
# print(output_dict)

# word = input()
# output_dict = {}
# for i in word:
#     output_dict[i] = ord(i)
# print(output_dict)

# price = [[200,.1,4],[300,.2,5],[400,.1,4],[500,.2,9]]
# for i, j,k in price:
#     print(i)
#     print(j)
#     print(k)


# price = [[200,.1],[300,.2],[400,.1],[500,.2]]
# final_price= []
# for i,j in price:
#     final_price.append(i*(1-j))
# print(final_price)

# word = 'ALMABETTER'
# output = ' '
# for i in range (len(word)):
#     if i%2 ==0:
#         output = output + word[i]
# print(output)
# print(list(enumerate(word)))]

# word = 'ALMABETTER'
# output = ' '
# output = ' '
# for i,j in enumerate(word):
#     if i%2 == 0:
#         output = output +str(i)
# print(output)


# ex = [23,24,25,30]
# even_sum = 0
# odd_sum = 0
# for index,number in enumerate(ex):
#     if index%2 ==0:
#         even_sum = even_sum + number
#     else:
#         odd_sum = odd_sum + number
# print(even_sum, odd_sum)

# ZIP :COMBINE THE DATA INDEX WISE

# price = [30,45,65,23,46,76]
# discount = [.1,.2,.3,.5]
# item_no = [2,4,2,1]
# for i,j,k in zip(price,discount,item_no):
#     print(i*(1-j)*k,end=' ')

# price = [30,45,65,23,46,76]
# discount = [.1,.2,.3,.5]
# for i,j in zip(price,discount):
#     print(i*(1-j) ,end=' ')

# cart = [7,15,35,80,5]
# total_cost = 0
# for i in cart:
#     if i>=10 and i<=50:
#         discount = 1*0.1
#     elif i>50:
#         discount = i *0.2
#     else:
#         discount = 0
#         total_cost = total_cost + (i-discount)
# print(total_cost)

# num = int(input())
# num_str = str(num)
# n_digit = len(num_str)
# arm_check = 0
# for i in num_str:
#     arm_check = arm_check + int(i) ** n_digit
#     if arm_check == num:
#         print("ARMSTRONG NUMBER")
#     else:
#         print("NOT AN ARMSTRONG NUMBER")

# break: stop the loop/ breaks the loop
#  find the first even number in a list

# ex = [35, 65, 78, 67, 56, 89]
# for i in ex:
#     if i%2 == 0:
#         print(i)
#         break

# ex = [1,2,3,4,5,6,7,8,9]
# for i in ex:
#     if i==5:
#         break
#     print(i)

# first factor dividing the number apart from one and itself

# num  = 30
# for i in range(2, num):
#     if num%i == 0:
#         print(i)
#         break

# num = int(input("Enter the number: "))
# n_divisor  =0
# for i in range(2, num):
#     if num%i == 0:
#         n_divisor +=1
#         break
#
# if n_divisor >0:
#     print("FALSE")
# else :
#     print("TRUE")

# CONTINUE: SKIP THE STATMENT
# ex = [1,2,3,4,5,6,7,8,9]
# for i in ex :
#     if i == 5:
#         continue
#     print(i, end=' ')

#  PRINT ONLY VOOWELS AND CONTINUE
# word = input()
# for i in word:
#     if i not in ('a','e','i','o','u','A','E','I','O','U'):
#         continue
#     print(i)

# lst1 = [1,2,3,4]
# lst2 = ['A','B','C','D']
# for i in lst1:
#     for j in lst2:
#         print(f'Value of i:{i} and value of j:{j}')

# name = ['John','Aryan','Ravi','Trishta']
# sweet = ['ROOSOGULA','JALEBI','LADDU','RASHMALAI']
# for i in name:
#     for j in sweet:
#         print(f'{i} got {j}')

# cart = [7, 15, 35, 80, 5]
# total_cost = 0
# for i in cart:
#     if i >= 10 and i <= 50:
#         total_cost += i * 0.9
#     elif i >= 50:
#         total_cost += i * 0.8
#     else:
#         total_cost += i
# print(total_cost)


# num = int(input())
# num_str = str(num)
# n_digits = len(num_str)
#
# arm_check  = 0
# for i in num_str:
#     arm_check = arm_check + int(i) ** n_digits
# if arm_check == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

# practice (fibbonacci Series)
# num = int(input())
# fibonacci_output = []
# for i in range (num +1):
#     if i in (0,1):
#         fibonacci_output.append(i)
#     else:
#         fibonacci_output.append(fibonacci_output[i-1]+fibonacci_output[i-2])
# print(fibonacci_output)

# WHILE LOOP\
# ex = [2,4,5,6,7]
# for i in ex:
#     pass
#
# play  ='True'
# while play == 'True':
#     print('Congratulations! Nice game')
#     play = input("Do you want to contribute playing (True/False): ")

# ex = ['pepperoni','mushroom','olives','sausages']
# index = 0
# while index < len(ex):
#     print(ex[index])
#     index = index +1

# num=1
# while num <=10:
#     print(num**2)
#     num = num+1


#
# ex = [['request'],['Alok Sir'],['to meet'],['personally']]
# i = 0
# op_list = []
# while i< len(ex):
#     op_list.append(ex[i][0])
#     i=i+1
# print(op_list)
# '  '.join(op_list)

# num = [5,6,-7,-8,2,0,6,8,9,9,10,11,13]
# index= 0
# while index <len(num):
#     if num[index] > 0:
#         print(f'{num[index]} is positive')
#     elif num[index] < 0:
#         print(f'{num[index]} is non negative')
#     else:
#         print('Zero')
#     index = index +1


# word  = input()
# index  = 0
# while index < len(word):
#     if word[index].lower() in ('a','e','i','o','u'):
#         print(f'char : {word[index]} at : {index} is Vowel')
#     else:
#         print(f'char : {word[index]} at : {index} is consonanat')
#     index = index+1

# ex = [4,5,6,7,8,9,10]
# print(len(ex))

# n = int(input("Enter the number: "))
# i =1
# total = 0
# while i <= n:
#     total = total +i
#     i +=1
#     print(total,end=' ')

# n = int(input())
# n_str = str(n)
# index  =0
# total = 0
# while index < len(n_str):
#     total = total  + int(n_str[index])
#     index = index+ 1
#     print(total)

# sentence = input("Enter the Sentence: ")
# s_word = sentence.split(' ')
# i = 0
# op_dict = {}
# while i<len(s_word):
#     op_dict[s_word[i]] = len(s_word[i])
#     i = i+1
#     print(op_dict)

# ex  = eval(input("enter the list: "))
# ex.clear()
# print('List after removing all elements: ', ex)


# num = int(input())
# prime_check = "True"
# i = 2
# while i<num:
#     if num % i == 0:
#         prime_check = 'False'
#         break
#     i = i+1
# print(prime_check)

# ex_lst  = [2,3,4,5,5,4]
# num_to_remove = 5
# i = 0
# while i<len(ex_lst):
#     if ex_lst[i] == num_to_remove:
#         ex_lst.pop(i)
#     else:
#         i +=1
# print(ex_lst)
# n= int(input())
# def cube_root(n=0):
#     cr = n**(1/3)
#     return(round(cr))


# def list_pow(l,n=1):
#     op_result = []
#     for i in l:
#         op_result.append(i**n)
#     return op_result
#
# list_pow(l=[1,2,3,4],n=2)
# list_pow(l=[1,2,3,4],n=3)
#
# l= eval(input())
# n= eval(input())
# op_result = []
# for i in l:
#     op_result.append(i**n)
#     print(op_result)


#                                                             ADVANCE LOOPING CONCEPTS
# ex = [23,47,78,90]
# def add_1(n):
#     return n+1
# print(list(map(add_1,ex)))

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def generate_primes():
#     primes = []
#     for num in range(2, 100):  # Generating prime numbers up to 100
#         if is_prime(num):
#             primes.append(num)
#     return primes
#
# def find_product_of_three_primes(n):
#     primes = generate_primes()
#     result = []
#     for i in range(2, n + 1):
#         prime_factors = []
#         num = i
#         for prime in primes:
#             while num % prime == 0 and len(prime_factors) < 3:
#                 prime_factors.append(prime)
#                 num /= prime
#         if len(prime_factors) == 3 and num == 1:
#             result.append((i, prime_factors))
#     return result
#
# n = int(input("Enter a value of n: "))
# results = find_product_of_three_primes(n)
# print("Integers between 1 to n that are the product of exactly three primes:")
# for number, factors in results:
#     print(f"{number} : {factors}")


# def is_palindrome(s):
#     return s == s[::-1]
#
# def closest_palindrome(input_string):
#     for i in range(len(input_string)):
#         left = input_string[:len(input_string) - i]
#         if is_palindrome(left) and len(left) > 1:
#             return left
#         right = input_string[i + 1:]
#         if is_palindrome(right) and len(right) > 1:
#             return right
#
# input_str = input("Enter a string: ")
# closest = closest_palindrome(input_str)
# print(f"The closest palindrome to '{input_str}' is: {closest}")


# def multiply_num(n):
#     tot = 1
#     for i in n:
#         tot = tot * i
#     return tot
#
# n = eval(input())
# print(multiply_num(n))
import math

# num1  = int(input())
# if num1 == 0:
#     print("Its is zero")
# else:
#     print("Any number other tha zero")

#
# speed  = int(input())
# if speed >= 50:
#     print("Mom goona beat you")
# else:
#     print("Good boy, drive slowly")


# n = int(input())
# n_str = str(n)
# total = 0
# for i in n_str:
#     total = total+int(i)
# print(total)

# def calculate_harmonic_sum(n):
#     if n ==1:
#         return 1
#     else:
#         harmonic_sum = 0
#         for i in range(1,n):
#             harmonic_sum += 1/i
#             return harmonic_sum
#
# n = int(input())
# result = calculate_harmonic_sum(n)
# print(f"the harmonic sum of {n-1} is:{result}")


# ex = [1000,4000, 8000, 3000,9000,7500]
# def emp_filter(n):
#     if n > 5000:
#         return True
#     else:
#         return False
# print(list(filter(emp_filter,ex)))
#
# word = ['Data','Science','Almabetter','Engineering','Hi','Machine']
# def filter_len(w):
#     return len(w)> 5
# print(list(filter(filter_len,word)))
#
# names = ['Abhishek','Aryan','Rahul','Nitin']
# def name_A(n):
#     return n[0].lower() == 'a'
# print(list(filter(name_A,names)))
#
# ex = [2,4,16,9,27,64]
# def perfect_square(n):
#     return int(n**(1/2)) == n**(1/2)
# print(list(filter(perfect_square,ex)))


#
# ex = [2,4,16,9,27,64]
# def perfect_square(n):
#     if int(n**(1/2)) == n**(1/2):
#         print("True")
#     else:
#         print('False')
# print(list(filter(perfect_square,ex)))

# ex = ['red','green','white','black','pink','yellow']
# index_ex = eval(input())
# op = []
# for i in range (len(ex)):
#     if i not in index_ex:
#         op.append(ex[i])
# print(op)

# class bank_account:
#     bank_name = 'SBI'
#     IFSC_code = 'SBIN0000'

# p1 = bank_account()
# p2 = bank_account()
# p1.bank_name
# p2.bank_name

# print('hello wrold')

