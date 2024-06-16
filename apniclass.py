# print("Hello World")
import sys

# str = "GOOD Morning"
# print(type(str))
# print(len(str))
# print(str[3])
# print(sys.getsizeof(str))
#
# print(str.replace('G','t'))
# print(str)

# mutable datatype --> list, set, dict
# immutable datatype --> string , tuple, int, float,

# TUPLE
# num = ( 2,4,7,3,5,8,8,45)
# print(num[0])
# # num[0] = 102
# # print(num)
# num = { 2,4,7,3,5,8,8,45}
# print(type(num))
# num.add(59)
# print(num)
# num.remove(5)
# print(num)
# print(len(num))

# LIST
# num = [ 2,4,7,3,5,8,8,45]
# print(len(num))
# num[1] = 8
# print(num)
# num.append(100)
# print(num)
# num.insert(4, 52)
# print(num)

# # Dictinary
# dict = {'a':1,'b': 2}
# # print(type(dict))
# # print(dict['b'])
# # dict['c']=3
# # print(dict)
# print(dict.pop('a'))
# print(dict)
#
#
# [6,7,4,5,6,10] == [4,5,6,10,7]
# {6,7,4,5,6,10} =={4,5,6,10,7}
#
# ordered dt = list, string, tuple
# unordered dt = set, dict
#
# {'a':1,'b': 2}== {'b':2, 'a':1}
#
# value = [1,2.3,True, 'alok', [3,4,5],(4,3), {3,4,5}, {1:2, 3:4}]
# print(len(value))
# print(type(value))
#
# value = { 1:[4,4], 3.4:(5,6),'A':{3,5,6},(3,5):(5,78,54)}
# print((value[(3.4)]))
# value[5] = "suhel"
# value.update({5:6})
# print(value)


# x =10
# y =23
# x =43
# print(x)

# Duplicate values
# string, list, tuple
# str = "Hello World"
# num = [ 2,4,7,3,5,8,8,45]
# num =  ( 2,4,7,3,5,8,8,45)
# print(num)

# Set
# value = {1,3,6,5,3,5,5,5,5,53,2, 0, '1', True, False}
# print(type(value))
# print(value)

# num_lst= [ 2,4,7,3,5,8,8,45]
# num_tuple = ( 2,4,7,3,5,8,8,45)
# num_set = { 2,4,7,3,5,8,8,45}
# num_str = ' 2,4,7,3,5,8,8,45'
#
# print(sys.getsizeof(num_set))
# print(sys.getsizeof(num_str))
# print(sys.getsizeof(num_tuple))
# print(sys.getsizeof(num_lst))


# print("Hello World")
import sys

# str = "GOOD Morning"
# print(type(str))
# print(len(str))
# print(str[3])
# print(sys.getsizeof(str))
#
# print(str.replace('G','t'))
# print(str)

# mutable datatype --> list, set, dict
# immutable datatype --> string , tuple, int, float,

# TUPLE
# num = ( 2,4,7,3,5,8,8,45)
# print(num[0])
# # num[0] = 102
# # print(num)
# num = { 2,4,7,3,5,8,8,45}
# print(type(num))
# num.add(59)
# print(num)
# num.remove(5)
# print(num)
# print(len(num))

# LIST
# num = [ 2,4,7,3,5,8,8,45]
# print(len(num))
# num[1] = 8
# print(num)
# num.append(100)
# print(num)
# num.insert(4, 52)
# print(num)

# # Dictinary
# dict = {'a':1,'b': 2}
# # print(type(dict))
# # print(dict['b'])
# # dict['c']=3
# # print(dict)
# print(dict.pop('a'))
# print(dict)
#
#
# [6,7,4,5,6,10] == [4,5,6,10,7]
# {6,7,4,5,6,10} =={4,5,6,10,7}
#
# ordered dt = list, string, tuple
# unordered dt = set, dict
#
# {'a':1,'b': 2}== {'b':2, 'a':1}
#
# value = [1,2.3,True, 'alok', [3,4,5],(4,3), {3,4,5}, {1:2, 3:4}]
# print(len(value))
# print(type(value))
#
# value = { 1:[4,4], 3.4:(5,6),'A':{3,5,6},(3,5):(5,78,54)}
# print((value[(3.4)]))
# value[5] = "suhel"
# value.update({5:6})
# print(value)


# x =10
# y =23
# x =43
# print(x)

# Duplicate values
# string, list, tuple
# str = "Hello World"
# num = [ 2,4,7,3,5,8,8,45]
# num =  ( 2,4,7,3,5,8,8,45)
# print(num)

# Set
# value = {1,3,6,5,3,5,5,5,5,53,2, 0, '1', True, False}
# print(type(value))
# print(value)

# num_lst= [ 2,4,7,3,5,8,8,45]
# num_tuple = ( 2,4,7,3,5,8,8,45)
# num_set = { 2,4,7,3,5,8,8,45}
# num_str = ' 2,4,7,3,5,8,8,45'
#
# print(sys.getsizeof(num_set))
# print(sys.getsizeof(num_str))
# print(sys.getsizeof(num_tuple))
# print(sys.getsizeof(num_lst))

# lst = [3,4,6,3,7,8,1,4,5,9, 'abcd',[43,65,9,432], 'True',False]
# print(lst[5])
# print(lst[0])
# print(lst[3])
# print(lst[-1])
# print(lst[-1])
# # print(lst)
# phone_no = { "Ram": 1234, "Shayam":3456, "Kavita":1987}
# print(phone_no)
# print(phone_no['Shayam'])

phone_no = dict({'Ram':1234,
                 'Shayam':3456,
                 'Kavita':1987
                 })
# phone_no['Mohon'] = 9954
# print((phone_no))
# phone_no['Madhav'] = { 11111, 33333, 554544}
# print((phone_no))
# phone_no['Shayam'] = {"Shayam_home": 123455,"Shayam_office":987654}
# print((phone_no))
# print(phone_no['Shayam']['Shayam_office'])
# print(phone_no['Shayam']['Shayam_home'])
# del(phone_no['Ram'])
# print(phone_no)
#
# print(phone_no.pop('Shayam'))
# print(phone_no)
#print(phone_no)
#print(phone_no.popitem())
#print(phone_no)
# #print(phone_no.clear())
# print(phone_no.keys())
# print(phone_no.values())
# print(phone_no.items())

phone_no = dict({'Ram':1234,
                 'Shayam':3456,
                 'Kavita':1987
                 })
# for i in phone_no:
#     print(i, end=",")
# for i in phone_no:
#  print(phone_no[i])

# for i in phone_no.items():
#     print(i)
#phone_no == phone_no.copy()
# print(phone_no)
# print(len(phone_no))

# # NESTED DICTIONARY
# student_data = {'Ram':{'roll_no':10, 'age': 10, 'course':'python'},'Mohan':{'roll_no':20, 'age':22, 'course':'Java'}}
# print(student_data)
# print(student_data['Mohan'])
# print(student_data['Mohan']['roll_no'])
# print(student_data['Ram']['roll_no'])
# student_data['Mohan']['phone_no'] = 98567432
# student_data['Ram']['phone_no'] = 12235468895
# print(student_data)
# del(student_data['Mohan']['phone_no'])
# print(student_data['Mohan'])


# NESTED list in dictionary
# travel_data = {'Gujarat':['Davarikadhish', 'Somnath', 'Statue of unity'], 'Rajasthan':['Jaipur','Uaipur']}
# print(travel_data)
# print(travel_data['Rajasthan'])
# print(travel_data['Gujarat'])

# NESTED DICTIONARY WITHIN LIST
# student_data = [{'Name':'Ram','roll_no':10, 'age': 10, 'course':'python'},{'Name':'Mohan','roll_no':20, 'age':22, 'course':'Java'}]
# print((student_data))
# print(student_data[0])
# print(student_data[1])
# student_data[1]['phone_no'] = [568652265]
# student_data[0]['phone_no'] = [ 14652364]
# print(student_data)



#TUPLE
# tpl1 = (12, 6, -8,'jenny', 1.1, True) # mixed type bhi ban sakta hai and then individual type bhi
# print(tpl1)
# print(tpl1[3])
# print(tpl1[-1])
# print(type(tpl1))

# tpl2 = (12, 6,6,-8,'Jenny',False)
# print(type(tpl2))   A = 65 a = 97

# tpl2[0] = 13
# print(tpl2)
# print(tpl2[1:3])
# print(len(tpl2)) # k = steps

# tpl3 = (tpl1 + tpl2)
# print(tpl3)
# print(min(tpl3))
# print(tpl3[-1][-1])
# print(len(tpl3))
#
#
# tpl4  = (30, 20, 10, 0, 1,5,60,51,60)
# print((max(tpl4)))
# print(tpl4.count(60))
# print(tpl4.index(60))

# tpl4  = [30, 20, 10, 0, 1,5,60,51,60]
# print(tuple(tpl4)) # typecasting                                   \n -

# tpl5 = 'khvbdkbe \n ' *5
# print(tpl5)

#SETS

# set1 = {}   #mixed dt and single dt, unordered, duplicates are not allowed
# print(type(set1))
#
#set2 = {12,34, 43,56,67,87,1, True, 0, False} # only single dt True =1 and False =0
# print(type(set2))
#
# set3 = set()
# print(type(set3))
#
#set2.add((65,85,78,56))
#print(len(set2))

# print(set2.pop())
# print(set2)

# set2.discard(68)
# print(set2)
#
# set2.clear()
#print(set2)

# # set1 = {'Ram','Siddhu','Jiya'}
# set2 = {'J','Ji','Aa'}
# # set3 = {'Aa', 'x','y'}
#
# # print(set1.union(set2)) # multiple set are applied
# # print(set2.union(set1))
# #
# # print(set1|set2|set3)
#
# print(set2.update(('M', 'S')))
# ex = {'a','b'}
# print(ex.add('c','d'))

# Question practoice
# Ques1: Print First 10 natural numbers using for loop
# for i in range(1,11):
#     print(i)
#
# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
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

