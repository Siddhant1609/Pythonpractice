# num = eval(input("Entyer the number: "))
# if num >= 60:
#     print("CONGRATULATIONS,The candidate has PASS the exam")
# else:
#     print("Better Luck! next time")

# soil_moisture  =  eval(input("Enter the value: "))
# if soil_moisture <= 40:
#     print("Water the plant")
# else:
#     print("No Actions are required")

# num = eval(input("Enter the number: "))
# if num % 2 == 0:
#     print("The number is EVEN")
# else:
#     print("The number is ODD")
#
# num1  =  eval(input("Enter the number1: "))
#
# if (num1 % 3 == 0) and ( num1 % 7 == 0):
#     print("The number is  divisible by  both 3 and 7")
# else:
#     print("The number is not divisible by 3 and 7 both")


#palindrome
# str = input("Enter the String: ")
# str_rev = str[::-1]
# if str_rev == str:
#     print("THE word is palindrome")
# else:
#     print("Not a palindrome")


# char  = input("Enter the alphabet: ")
# if  char.lower() in ("a,e,,i,o,u"):
#     print("YES, It is a vowel")
# else:
#     print("Its a consonant")

# var_list = eval(input("enter the list: "))
# num = eval(input("Enter the number: "))
#
# if num in var_list:
#     count = var_list.count(num)
#     print(f'{num} with {count} times')
# else:
#     print("Only single time present")

# for num in range(0,11):
#     print(num**2)

# lst = [23,56,32,78,45,43,10]
# for i in lst:
#     if i % 2 == 0:
#         print(f"The {i} is EVEN")
#     else:
#         print(f"The {i} is ODD")

#
# lst = [5,6,-7,-8,2,0,6,8,9,9,10,11,13]
# for i in lst:
#     if i == 0:
#         print(f"The number is {i}")
#     elif i > 0:
#         print(f"The {i} is positive")
#     else:
#         print(f"The {i} is negative")


# num = eval(input("Enter the nuumber: "))
# for fact in range(1, num+1):
#     if num % fact == 0:
#         print(fact)


# num = eval(input("Enter the number: "))
# for fact in range(2, num+1):
#     if (num%fact == 0) and (fact % 2 == 0):
#         print(fact)

# num = eval(input("Enter the number: "))
# for fact in range(1, num+1):
#     if (num%fact == 0) and (fact % 1== 0):
#         print(fact)

# word= input("Enter the word: ")
# for i in word:
#     if i.lower() in "aeiou":
#         print(f"The word {i} is vowel")
#     else:
#         print(f"The word {i} is consonant")


# num = int(input("Enter the number: "))
# fact = 1
# for i in range (1,num+1):
#     fact = fact *i
# print(fact)

#
# n = int(input("Enter the number: "))
# n_str = str(n)
# total = 1
# for i in n_str:
#     total *= int(i)
# print(total)


# num = int(input("Enter the number: "))
#
# n_str = str(num)
# total = 0
# for i in n_str:
#     if int(i) % 2 == 0:
#         total = total + int(i)**2
#     else:
#         total = total + int(i)**3
# print(total)

# string = input("Enter the word: ")
# count = 0
# for i in string:
#     if i in 'aeiouAEIOU':
#         count = count +1
#
# print(count)

# num_lst  =[]
# for i in range (29, 80):
#     if i %3 == 0:
#         num_lst.append(i)
#
# print(num_lst)
#
# word = input("Enter the word: ")
# output_str = ''
# for i in word:
#     if i.lower() in 'aeiou':
#         output_str = output_str +i
#
# print(output_str)

# word  = input()
# index = eval(input())
# output = ''
# for i in index:
#     output = output + word[i]
# print(output)



# ex = [2,32,54,2,31,6,87,98,123,1,2,3,4,5,6]
# max = ex[0]
# for i in ex:
#     if i > max:
#         max = i
# print(max)

#
# number = int(input("Enter the number: "))
# def fact(number):
#     if number == 0:
#         fact = 1
#     else :
#         fact =

# def repeat_string(s,n):
#     return (s*n)
#     return repeat
#
# s = input()
# n = int(input())
# repeat_string(s,n)

# def cube_root(n=0):
#     cr = n**(1/3)
#     return round(cr)
#
# cube_root(n=27)
# cube_root(n=64)

# def list_pow(l,n=1):
#     op_result = []
#     for i in l:
#         op_result.append(i**n)
#     return op_result
#
#     list_pow(l=[1,2,3,4], n=2)
#     list_pow(l=[1,2,3,4], n=3)
#
# ex = ['red','green','white','black','pink','yellow']
# index_ex = eval(input())
# op = []
# for i in range(len(ex)):
#   if i not in index_ex:
#     op.append(ex[i])
# print(op)

#
# ex = ['red','green','white','black','pink','yellow']
# index_ex = eval(input())
# op = []
# for i in range(len(ex)):
#   if i not in index_ex:
#     op.append(ex[i])
# print(op)

#
# def prime (n):
#   prime_check = True
#   for i in range(2,n):
#     if n%i ==0:
#       prime_check = False
#       break
#     return prime_check
#
# n = int(input())
# list(filter(prime,range(1,n+1)))


# class bankaccount:
#     bank_name = 'SBI'
#     ifsc_code = 'SBIN0000'
#
# # p1 = bankaccount()
# # p2 = bankaccount()
# #
# # print(p1.bank_name)
# # print(p2.bank_name)
#
# def __init__ (self,aadhar_card,city):
#     self.aadhar_card = aadhar_card
#     self.city = city
#
# p1 = bankaccount(aadhar_card = '23131313', city = 'blr')
# p2 = bankaccount(aadhar_card = '54654665', city = 'mum')
# print(p1.bank_name)
# print(p2.bank_name)
# print(p1.aadhar_card)
# print(p2.aadhar_ca)

class BankAccount:
    bank_name = 'SBI'
    ifsc_code = 'SBIN0000'

    def __init__(self, aadhar_card, city):
        self.aadhar_card = aadhar_card
        self.city = city

p1 = BankAccount(aadhar_card='23131313', city='blr')
p2 = BankAccount(aadhar_card='54654665', city='mum')

print(p1.bank_name)  # Output: SBI
print(p2.bank_name)  # Output: SBI
print(p1.aadhar_card)  # Output: 23131313
print(p2.aadhar_card)  # Output: 54654665
