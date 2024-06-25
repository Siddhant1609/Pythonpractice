# STATEMENT , INDENTATION AND CONDITIONALS
# age = eval(input("Enter your age: "))
# print(type(age))

# x = input("Enter your institute name: ")
# if x == "Almabetter":
#     print("All the best buddy. ")

# speed = int(input("Enter the speed: "))
# if speed >= 50:
#     print("Mom is waiting at home")
#
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are at a grown up stage")

# num = int(input("Enter the number: "))
# if num == 0:
#     print("Number is zero")
# else:
#     if num >=0:
#         print("The number is positive")
#     else:
#         print("Number is NEGATIVE")

# marks = eval(input("Enter the marks: "))
# if marks >= 60:
#     print("You pass the exam")
# else:
#     print("YOu are fail")

# Soil_moisture_level= eval(input("Enter the moisture level: "))
# if Soil_moisture_level >= 45:
#     print("No action is required")
# else:
#     print("Water the plant")

# num = int(input("Enter the number: "))
# if num%2 == 0:
#     print("The number is EVEN")
# else:
#     print(" The number is ODD")


# num = int(input("Enter the number: "))
# if num%3 == 0 and num%7 ==0:
#     print("The number is divisible by both 3 and 7")
# elif num%3 == 0:
#         print("The number is only divisible by 3 not 7")
# elif num%7 == 0:
#  print(" The number is not divisible by 7 not by 3")
#
# else:
#     print("The number is not divide by both the number")

# dividend = eval(input("Enter the dividend: "))
# divisor = eval(input("Enter the divisor: "))
# if dividend % divisor == 0:
#     print(f"{dividend} is perfectly divisible by {divisor}")
# else:
#     print(f"{dividend} is not perfectly divisible by {divisor}")

# if dividend % divisor==0:
#     print(f" {dividend} is completely divisible  by {divisor} by {dividend// divisor} times")
# else:
#     print(f" {dividend} is  not completely divisible  by {divisor}

# reminder = dividend % divisor
# if reminder == 0:
#     print(f"{dividend} is divisible by the {divisor}")
#     print(f"{dividend} is divisible by {dividend//divisor} times")
# else:
#     print(f"{dividend} is  not divisible by {divisor}")
#     print(f" The reminder is {reminder}")

# word = input("Enter the word: ")
# word_rev = word[::-1]
# if word == word_rev:
#     print(f"Yes, the {word} is palindrome")
# else:
#     print("The word os not a palindrome")


# char = input("Enter the characters: ")
# if char in "aeiouAEIOU":
#     print(f"YES, the char {char} is a vowel")
# else:
#     print(f"The char {char} is a consonant ")


# sentence = input("Enter the Sentence: ")
# word = input("Enter the word present in  the sentence: ")
# if word.lower() in sentence.lower():
#     print(f'YES, The word {word} present in the sentence')
# else:
#     print(f' NO, The word {word} is not present in the sentence')

# var_lst = eval(input("Enter the list values: "))
# num = eval(input('Enter the num from the list values: '))
# if num in var_lst:
#     print(f'YES, the number {num} present in the list')
#     count_num = var_lst.count(num)
#     print(count_num,'times')
# else:
#     print("Number is not present in the list")

# age = int(input("ENTER THE AGE: "))
# if age >= 18:
#     print("YOU are an adult")
# else:
#     if age >=13 and age<=18:
#         print("YOU are a teenager")
#     else:
#         print(" YOU are a child")

# score  = int(input("ENTER THE MARKS: "))
# if score >= 80:
#     print("Grade A")
# elif score >= 60 and score < 80:
#     print("Grade B")
# elif score >= 40 and score < 60:
#     print("Grade C")
# else:
#     print("You are not able to make it this time")

#
# season_month = eval(input("Enter the month: "))
# if season_month > 12 and season_month < 1:
#     print("Invalid Month")
# elif season_month >= 3 and season_month <= 5:
#     print("Welcome to the blossom of SPRING")
# elif season_month <= 6 and season_month <= 8:
#     print(" HAYEE GARMIIIIII!!")
# elif season_month >=9 and season_month <= 11:
#     print(" Ye patjhad aur sawan ka mausam yr shayarana andaj lata hai")
# else:
#     print("YE kadkaddati huii thanda yr")

# year = int(input("Enter the year: "))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"The {year} is a leap year ")
#     else:
#         print(f"The year {year} is non-leap year")
# else:
#     if year%4 == 0:
#         print(f"The {year} is a leap year ")
#     else:
#         print(f"The year {year} is non-leap year")


# balance =10000
# correct_pin = 1234
# print(''' choose an option
# 1. WITHDRAW
# 2. CHECK BALANCE
# 3. DEPOSIT''')
# option = int(input("Enter the choice 1, 2 0r 3: "))
# pin = int(input("Enter the pin: "))
# if pin == correct_pin:
#     if  option ==1:
#         amount = float(input("Enter your amount: "))
#         if amount > balance:
#             print("Insufficient funds.")
#         else:
#             balance = balance- amount
#             print("Withdraw", amount)
#             print("New balance", balance)
#
#     elif option==2:
#         print("Balance", balance)
#     elif option==3:
#         deposit = float(input("Enter the amount deposited:"))
#         balance = balance + deposit
#         print("Deposited", deposit)
#         print("New Balance", balance)
#     else:
#         print("Invalid option, Please choose 1,2 or 3")
# else:
#     print("Incorrect pin entered")

# x = "Pepperoni"
# print ("This is ", x)

# x =100
# if x > 100:
#     print("Slow down")

toppings = ["pepperoni", "Mushroom", "olives", "sausages"]
# print(toppings[0])
# print(toppings[1])
# print(toppings[2])
# print(toppings[3])
# index = [0,1,2,3]
# for i in index:
#     print(toppings[i])

# for i in range(0, len(toppings)):
#     print(toppings[i])
# for i in range(2, len(toppings)):
#     print(toppings[i])

# for i in range(-4,0):
#     print(toppings[i])


# for i in range(-4, 0):
#     print("Iterations", [i])
# for i in toppings[::-1]:
#     print(i)

# for i in toppings:
#     print(i.upper())

# for i in range(0, len(toppings)):
#     print(toppings[i].upper())

# for i in range(1,101):
#     print(f"The square of {i} is {i**2}")

# for i in ("A","B","C","D"):
#     print(i)

# ex = [23,45,56,78,23,14,12,15,45,98,65,34,64,76,56]
# for i in ex:
#     if i%2 == 0:
#         print(f"This element {i} is EVEN")
#     else:
#         print(f"This element {i} is ODD")

ex = [5,4,6,8,2,1,3,-1,-4,-5,-6,0,0,11,23]
# for i in ex:
#     if i>0 :
#         print(f"{i} is positive", ex.count(i))
#     elif i<0 :
#         print(f"{i} is negative", ex.count(i))
#     else:
#         print(f"{i} is zero", ex.count(i))

# for i in range(len(ex)):
#     if ex[i] < 0:
#        print(f"{i} is negative")
#     elif ex[i] > 0:
#         print(f"{i} is positive")
#     else:
#         print(f"{i} is zero")

# num = int(input("Enter the number: "))
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)
#
# for i in range( 1,num+1):
#     if num%i == 0 and i%2 == 0:
#         print(i)

# for i in range(1,num+1):
#     if num % i == 0 and i % 2 == 0:
#         print(i, end = ',')

# for i in range(1, 10):
#     print(i, end = ',')

# num = int(input("Enter the number: "))
# for i in range(1,num+1):
#     if num % i == 0 and i % 2!= 0:
#         print(i)

# word = input("Enter the word: ")
# for i in word:
#     if i in "aeiouAEIOU":
#         print(f"{i} is vowels")
#     else:
#         print(f"{i} is consonant")

# ex = {"Product A": False, "Product B": True,"Product C":False,"Product D":False,"Product E": True}
# for i,j in ex.items():
#     if j== True:
#         print(i)
#
# print(list(ex.items()))


# log = {'/home': 200,'/about': 200,'/home/product': 200, '/home/product/electronics': 404, '/home/product/fashion': 200}
# for i, j in log.items():
#     if j == 404:
#         print(i)

# ex = {"Product A": False, "Product B": True,"Product C":False,"Product D":False,"Product E": True}
# print(ex)
# print(ex.keys())

# num = int(input("Enter the numbers: "))
# total = 0
# for i in range(1, num+1):
#     total = total + i
# print(total)

# num = int(input("Enter the numbers: "))
# total = 0
# for i in range(1, num +1):
#     total = total + i**2
# print(total)

# n = int(input())
# total = 0
# for i in range (0, n+1):
#     if i%2 == 0:
#         total = total + i
# print(total)





