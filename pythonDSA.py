                                                                                                        # FINDING COMMON LETTER
# def common_lettrs():
#     str1 = input('Enter the string')
#     str2 = input('Enter the String')
#     s1 = set(str1)
#     s2 = set(str2)
#     lst = s1 & s2
#     print(lst)
#
# print(common_lettrs())

                                                                                                        #FREQUENNCY OF A WORD APPEAR IN A STRING

# def frequency_words():
#     str = input("Enter the string: ")
#     li = str.split()
#     d = {}
#     for i in li:
#         if i not in d.keys():
#             d[i] = 0
#         d[i] = d[i]+1
#     print(d)
#
# frequency_words()

                                                                                                 # CONVERSION OF TWO LIST INTO DICTIONARY

# def list_to_dict():
#     keys = [1,2,3,4]
#     values = ['one','two','three','four']
#     result  = dict(zip(keys, values))
#     print(result)
#
# list_to_dict()

# def dict_to_tuple():
#     x = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#     for i in x.items():
#         print(i)
#
#
# dict_to_tuple()

                                                                                            #FIND MISSING NUMBER IN AN ARRAY IN PYTHON
# def missing_number_summation(a):
#     n  = a[-1]
#     sum1 = 0
#     total = n*(n+1)/2
#     sum1  = sum(a)
#     print(int(total - sum1))
#
# a = [1,2,4,5,6,7,8,9]
# missing_number_summation(a)

# through xor method
# def get_missing_xor(a):
#     n = len(a)
#     xor_a = a[0]
#     for index in range(1,n):
#         xor_a = xor_a^a[index]
#
#     x2  = 0
#     for i in range(1,n+2):
#         x2=x2^i
#     print(xor_a^2)
#
# a = [1,2,4,5,6,7,8,9]
# get_missing_xor(a)
#

                                                                # Find Out Pairs with given sum in an array in python of time

# def two_sum (arr,sum):
#     arr.sort()
#     left = 0
#     right = len(arr)-1
#     while(left <= right):
#         if (arr[left] + arr[right] > sum):
#             right = right-1
#         elif(arr[left] + arr[right]<sum):
#             left = left+1
#         elif(arr[left] + arr[right]  == sum):
#             print('value of pairs are', arr[left] , '&', arr[right])
#             right = right-1
#             left = left+1
#
#
# arr = [5,7,4,3,9,8,19,21]
# sum = 17
# two_sum(arr,sum)

#Length of Last Word - Algorithm

def length_of_lastword(A):
    arr = A.split(' ')
    size = len(arr)
    if (size==1):
        return len(A)

    last_word = arr[-1]
    print(last_word)


A = 'hello almabetter'
print(length_of_lastword(A))