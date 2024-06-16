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
#
# phone_no = dict({'Ram':1234,
#                  'Shayam':3456,
#                  'Kavita':1987
#                  })
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

#
# tpl = (10,34.45, 68,'jonshon',"jakson",True  )
# print(tpl)
# print(tpl[0])
# print(tpl[1])
# print(tpl[-1])
# print(tpl[::-1])
# print(type(tpl))
#
# tpl2 = (456,'natak', 'nautanki na karoo', 'chal be hawa ane de')
# print(type(tpl2))
# print(tpl[1::])
# print(len(tpl))
# print(len(tpl2))
# # NESTED TUPLE
# tpl3 = (tpl  + tpl2)
# print(tpl3)
# print(len(tpl3))
# print(tpl3[0])
# print(tpl[0])
# print(tpl3[::-1])

# #  STATEMENT , INDENTATION AND CONDITIONS
#  universal adult frachise = 18 + to app vote dal akte hoo nahi to nai
# if conditional_Statment:
#      statment
# else:conditional_Statment()

# age = eval( input())
#  age hamari kuch bhi hposakti hai int , float
# print(age)
# print(type(age))

# college = input(" Entyer your college name ")
# print(college)
# print(type(college))

# str = input()
# print(str)
# print(type(str))
# a = 54
# print(a)
# print(type(a))


# compound Statement
# depend upon the coditinal statment

# x = "jklmn"
# if x == 'geeksforgeeks':
#     print("Its a right value")

# x = input(" Enter the string")
# if x == 'geeksforgeeks':
#     print("Its a right value")



# x = input("Enter the string: ")
# if x == 'geeksforgeeks':
#     print("It's the right value")

# SYNTAX : IF ELSE CONDITION
# if condition:
#     " do your coding here"
# else:
#     "Do your coding here"

#  adult franchise

# created a user defined data

# jo bhi value ager 18+ hai then he or she is adult
# else condition aayegi wo hamesha questin ki need pe deepend karega

# age = eval(input("Enter the age "))
# if age >= 18:
#     print("The guy is adult")
# else:
#     print(" this guys is not adult")

# SPEED LIMIT NOT EXCEED 50KM/HR
# speed = int(input())
# if speed >= 50:
#     print("high speed")
# else:
#     print("not a high speed")

# CHECK IF THE VALUE IS POSITIVE, NEGATIVE OR ZERO
# num = int(input("Enter the number: "))
# if num > 0:
#     print(f"The {num} is positive")
# elif num < 0:
#     print(f"The {num} is negative")
# else:
#     print(f"The {num} is zero")

# MARKS INPUT WHICH IS FAIL OR PASS IF IT WAS GRATER THEN 60
# marks = int(input("Enter the marks: "))
# if marks > 60:
#     print(f"The {marks} is Good marks and Congratulation")
# else:
#     print(f"You are fail as your marks is  {marks} ")

# SOIL MOISTURE LEVEL <40 WE HAVE TPO GIVE WATER TO PLANT ELSE : THEE MOISTURE IS AT GOOD LEVEL
# moisture_level = eval(input("Enter the marks: "))
# if moisture_level < 40:
#     print(f"WATER THE PLANT AS IT WAS ,{moisture_level},😔")
# else:
#     print(f"MOISTURE LEVEL IS GOOD, {moisture_level}, 😀")


# CHECK THE NUM IS EVEN OR ODD
#  NUM % 2 == 0 EVEN  , AND IF NUM %2 != 0 THE NUM IS ODD
# num = eval(input("Enter the marks: "))
# if num % 2 == 0:
#     print(f"the {num} is even")
# else:
#     print(f"the {num} is odd")

# LOGICAL OPERATORS  CHECK THE  NUM IS DIVISIBLE BU BOTH 3 AND 2
#  == and = difference
# num = eval(input("Enter the marks: "))
# if num % 3 == 0 and num %2 ==0:
#     print(f"The number {num} is divisible by both 3 and 2")
# else:
#     print(f"The number {num} is not divisible by both 3 and 2")


# # Dividend is completely divisible by the divisor
# dividend = eval(input("Enter the dividend: "))
# divisor = eval(input("Enter the divisor: "))
# if dividend % divisor == 0:
#     print(f"The {dividend} is completely divisible by the {divisor} , quoitent is {dividend // divisor}")
# else:
#     print(f"The {dividend} is not completely divisible by the {divisor}  quoitent is {dividend / divisor}")

# # WHAT IS THE REMINDER WHEN THE DIVISOR DIVIDES THE DEVIDEND
# dividend = eval(input("Enter the dividend: "))
# divisor = eval(input("Enter the divisor: "))
# if dividend % divisor == 0:
#     print(f"The {dividend} is completely divisible by the {divisor},reminder is the  {dividend % divisor} quotent is the {dividend// divisor}")
# else:
#     print(f"The {dividend} is not completely divisible by the {divisor},reminder is the {dividend%divisor} quotent is the {dividend// divisor}")


#  PALINDROME
#  high == hgih not palindrom
#  level = level palidrome hai

# word = input("Enter the word: ")
# word_rev = word[::-1]
# if word_rev == word:
#     print(f" The word {word} is Palindrom")
# else:
#     print(f" The word {word} is not Palindrom")

# Dividend is completely divisible by the divisor
# how many times  if not than what is the reminder   using if else--- the formate of the answer is dividend, divisor , quotient and then reminder

# CHECK FOR THE VOWELS AND CONSONENT
# word = input()
# for i in word:
#   if i.lower() in "aeiou":
#     print(f"{i} is a vowel")
#   else:
#     print(f"{i} is a consonant.")

# char = input()
#
# if char in 'aeiouAEIOU':
#   print('Vowel')
# else:
#   print('Consonant')

# CHECK THE LETTER IS PRESENT IN WORD OR NOT
# word = input()
# character = input()
# if character in word:
#   print(f"{character} is in word.")
# else:
#   print(f"{character} is not in word.")

# str=input()
# char=input()
# if char.lower() in str.lower():
#     print(f"{char} is in str")
# else:
#     print(f"{char} not in str")

#  list me koi bhi input dale, we want that ki jo bhi number hai ooska count patta chale123,456 ,654,123,123,123, 198,765
# yes the number is in the loist with taht number of counts
# user_input = eval(input())
# num = eval(input())
# if num in user_input:
#   count = user_input.count(num)
#   print(f"Yes, {num} is in {user_input}, {count} number of times.")
# else:
#   print(f"{num} is not in {user_input}.")

# eligible for the roolercoustrer ride
# > 18  and height >= 110 cm ,  eligible , else he was not

# age = int(input())
# height = float(input())
# if age>18 and height>=110:
#   print("Yes you can ride the rollercoster.")
# else:
#   print("sorry, you cannot ride the rollercoster")


# check kar ki agra koi bhi banda 18> to wo adult other wise wo teen hai, agar wo teen bhi nahi hai to wo child hai
# age = eval(input())
# if age>=18:
#     print("You are an adult")
# else:
#     if age >=13:
#         print("You are a teen")
#     else:
#         print("you are a child")

# if conditional_Statment:
#     result breakpoint(
# elif conditional_Statment:
#     coging breakpoint
# else:
#     codoing breakpoint()

# grade >=80 , grade A
#  80 <=grade <=60 , grade B
# 60<=grade >=40 , grade C
# 20<=grade >=40 , grade d
# grade <= 20 fail

# grade = eval(input("Enter the grade: "))
# if grade>=80:
#   print("Grade A")
# elif grade>=60:
#   print("Grade B")
# elif grade>=40:
#   print("Grade C")
# elif grade>=20:
#   print("Grade D")
# else:
#   print("Fail")

#  FOR LOOP CONCEPTS
lst = [34,45,67,23,5,6,78,99,]
# print(34)
# print(45)
# print(67)
# print(23)
# print(5)
# print(6)
# print(78)
# print(99)
# index = [0,1,2,3,4,5,6,7]
# for i in range(1,lst+1):
#     print(lst[i], end ='  ')


# list=[34,65,67,89,99,100]
# for i in range(-6,0):
#   print(list[i], end=',')
#
# print(list.remove(34))
# print(list)

toppings = ['pepporani',' mushroom', ' olives',' sausages']
# for i in toppings[::-1]:
#     print(i, end=',')
# for i in toppings:
#     print(i.upper(), end=',')
#
# for i in range(0, len(toppings)):
#     print(toppings[i]. upper(), end=',')    GIVES SAME ANSWER AS ABOVE

# # CHECK
# for i in range(1,11):
#     print(f'The Square of number {i} : {i**2}')

#
# for i in ['a','b','c','d']:
#     print(i , end= ',')

# i=32
# if i%2 == 0 :
#     print(f'{i} is EVEN')
# else:
#     print(f'{i}is odd')


def sum_of_degits(n):
    total = 0
    num_str = str(n)
    for digit in num_str:
        total = total + int(digit)
    return total

