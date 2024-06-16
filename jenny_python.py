
                                                                                         #  STRING MANIPULATION
# print("First Program - Python print function")
# print("It is declared like this:")
# print("print('What to print')")
                                                                                        # Question 1

# print("String Manipulation Exercise \n String Concatenation is done with '+' sign ")
# print("e.g print('Hello' + 'Jenny') \n New lines can be created with a backlash and n")

                                                                                        # Question 2

# print("Hey," + " " + input("What is your name") + " how are you " "buddy!!")

                                                                                        # Question 3

# name = input("What is your name ?")
# print(len(name))

                                                                                        # Question 4 -->  Swapping of numbers

# a = input("Enter the value 1: ")
# b = input("Enter the value 2: ")
# c = input("Enter the value 3: ")
# temp  = a
# a = b
# b = c
# c =temp
# print("a = " + a)
# print("b = "+b)
# print("c = " +c)

                                                                                        # Quesstion 5 --> Assignment on Summation
# first_number = input("Enter your number: ")
# second_number = input("Enter your number: ")
# sum = int(first_number) + int(second_number)
# print(sum)

                                                                                        # Question 6 --> Adding a String
# numbers = input("Enter the eight digit String: ")
# first_number = numbers[0]
# second_number = numbers[1]
# third_number = numbers[2]
# fourth_number = numbers[3]
# five_number = numbers[4]
# sixth_number = numbers[5]
# seventh_number = numbers[6]
# eigth_number = numbers[7]
#
# print(int(first_number) * int(second_number) * int(third_number) * int(fourth_number) * int(five_number) * int(sixth_number) * int(seventh_number) *int(eigth_number))

                                                                                        # Question 7 --> Exercise on operators
# a,b = 1,2
# c = a+b
# print(c)
# c += a
# print(c)
# c%=b
# print(c)
# c //=a
# print(c)

                                                                                        # Question 8--> Bitwise operator
# print(26&23)
# print(17 | 24)
# print(17 ^ 24)
# print(~45)
# print(68 << 2)
# print(56 >> 3)

                                                                                        # Question 9 --> Membership Operator

# Str = "Siddhant"
# print('d' in Str)
# print('S' in Str)
# print('i' in Str)
# print('d' in Str)
# print('h' in Str)
# print('a' in Str)
# print('n' in Str)
# print('t' in Str)
# print('G'  in Str)


                                                                                        # Question 10 --> BMI(BODY MASS INDEX)
# weight = int(input("Enter the weight in kg"))
# height = float(input("Enter the height in metre"))
#
# BMI = weight/(height**2)
# print(BMI)
#




# Virtual toss coins
import random

import random
# toss_value = random.randint(0,1)
# print(toss_value)
# if toss_value == 1:
#     print("Heads")
# else:
#     print("Tails")

#who will pay the bill of hotel                                     # SAME CODE WITHOUT HELP OF RANDOM.CHOICE
# names = input("Enter the names seperated by commas ")
# splitted_names = names.split(",")
# length = len(splitted_names)
# random_choice = random.randint(0,length-1)
# print(f"{splitted_names[random_choice]} will going to pay the bill")


                                                                # SAME CODE WITH THE HELP OF RANDOM.CHOICE
# names = input("Enter the names seperated by commas ")
# splitted_names = names.split(",")
# person_selected = random.choice(splitted_names)
# print(f"{person_selected} will going to pay the bill")


#NESTED LIST
#lst1 = [10, 34,67,[34,65,23,58,78],67,87,54]
# print(len(lst1))
# print(lst1[5])
# print(lst1[3])
# print(lst1[-1])
# print(lst1[0])
# print(lst1[1])
# print(lst1[3][2])
# print(lst1[3][1])
# lst1 = [10, 34,67,[34,65,23,58,78],67,87,54,'sameera','sakshi','rafftar']
# print(lst1[::-1])


#Enter the position where you wan to hide your money
# row1 = ['❤️','❤️','❤️']
# row2 = ['❤️','❤️','❤️']
# row3 = ['❤️','❤️','❤️']
# matrix = [row1,row2,row3]
#
# position = input("Enter the position where you want to hide your position: ")
# row_number = int(position[0])
# coloumn_number = int(position[1])
# row_selected = matrix[row_number-1]
# row_selected[coloumn_number-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")


# I = input()
# if I in ("a,e,i,o,u,A,E,I,O,U"):
#  print("Vowels")
# else:
#   print("Consonents")
# num  = eval(input('Enter the number: ')) # Created the data using input and typecasted using eval
# # -4
# if num > 0 :
#
#   print('Positive number')
#
# else:
    #   print('Negative number')

# # PAPER, SCISSOR AND ROCK
# user_choice = int(input("Enter the choice Type 1 for Rock, Type 2 for Paper, Type 3 for Scissor "))
# if user_choice >=3 and user_choice < 0:
#     print("You choose invalid number, You loose")
# else:
#     computer_choice = random.randint(0,2)
#     print("computer_choice")
#     print(computer_choice)
#     if computer_choice == user_choice:
#         print("It's a Draw")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You win")
#     elif computer_choice > user_choice:
#         print("You loose")
#     elif user_choice > computer_choice:
#         print("You win")

                                                                                # TUPLES --> IMMUTABLE
tpl = (10,34.45, 68,'jonshon',"jakson",True  )
print(tpl)
print(tpl[0])
print(tpl[1])
print(tpl[-1])
print(tpl[::-1])
print(type(tpl))

tpl2 = (456,'natak', 'nautanki na karoo', 'chal be hawa ane de')
print(type(tpl2))
print(tpl[1::])
print(len(tpl))
print(len(tpl2))
# NESTED TUPLE
tpl3 = (tpl  + tpl2)
print(tpl3)
print(len(tpl3))
print(tpl3[0])
print(tpl[0])
print(tpl3[::-1])
