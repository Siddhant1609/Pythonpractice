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

# def length_of_lastword(A):
#     arr = A.split(' ')
#     size = len(arr)
#     if (size==1):
#         return len(A)
#
#     last_word = arr[-1]
#     print(last_word)
#
#
# A = 'hello almabetter'
# print(length_of_lastword(A))


                                                    #A. REVERSE OF AN ARRAY
#                                                    1. def reverse_array_extra_array(arr):
#     reversed_arr = arr[::-1]
#
#     # Print reversed array
#     print("Reversed Array:", end=" ")
#     for i in reversed_arr:
#         print(i, end=" ")
#
# # Example usage:
# original_arr = [1, 2, 3, 4, 5]
# reverse_array_extra_array(original_arr)

#                                               2.  array reverse using a loop
# def reverseList(A,start,end):
#     while start < end:
#         A[start], A[end] = A[end],A[start]
#         start +=1
#         end -=1
#
# A = [1,2,3,4,5,6]
# print(A)
# reverseList(A,0,5)
# print("Reversed list is: ",A)

#                                               3. Array Reverse Inbuilt Methods (In-place):
# original_array = [1,2,4,5,6,6,7,8,8,9]
# rev_arry = list(reversed(original_array))
# print(rev_arry)

#                                               4.  Array Reverse Recursion (In-place or Non In-place):
# def reverselist(A,start, end):
#     if start >= end:
#         return
#     A[start],A[end] = A[end], A[start]
#     reverselist(A,start+1,end-1)
#
# A = [1,2,3,4,5,6]
# print(A)
# reverselist(A,0,5)
# print("Reversed list is: ", A)

#                                               5. Array Reverse Stack (Non In-place):

# def reverse_arrayy(arr):
#     stack = []
#     for element in arr:
#         stack.append(element)
#
#     for i in range(len(arr)):
#         arr[i] = stack.pop()
#
# arr = [1,2,3,4,5,6,7]
# reverse_arrayy(arr)
# print("Reversed Array:", arr)

#                                                   B. find maximum and minimum number of an array
#                                                   1. USING MINIMUM NUMBER OF THE COMPARISON
# def set_mini(A):
#     mini = float('inf')
#     for num in A:
#         if num<mini:
#             mini = num
#     return  mini
#
# def set_max(A):
#     max = float('-inf')
#     for num in A:
#         if num > max:
#             max = num
#     return max
#
# if __name__ == "__main__":
#     A = [4,9,6,5,2,3]
#     N = len(A)
#     print("Minimum element is:", set_mini(A))
#     print("Maximum element is:", set_max(A))

#                                                       2. Maximum and minimum of an array using Sorting:
# def getMinMax(arr):
#     arr.sort()
#     minmax = {'min':arr[0],'max':arr[-1]}
#     return minmax
#
# arr = [1000,11, 445,1,330,3000]
# minmax = getMinMax(arr)
# print('Minimum element is: ',minmax['min'])
# print('Maximum element is:', minmax['max'])

#                                                       3.MAXIMUM AND MINIMUM OF AN ARRAY USING, LINEAR SEARCH
# class pair:
#     def __init__(self):
#         self.min = 0
#         self.max = 0
#     def getMinMax(arr:list, n:int) -> pair:
#         minmax = pair()
#     if n==1:
#         minmax.max == max[0]
#         minmax.min == arr[0]
#         return getMinMax()
#     if arr[0]> arr[1]:
#         minmax.max = arr[0]
#         minmax.min = arr[1]
#
#     else:
#         minmax.max = arr[1]
#         minmax.min = arr[0]
#
#     for i in range(2,n):
#         if arr[i] > minmax.max:
#             minmax.max = arr[i]
#         elif arr[i] < minmax.min:
#             minmax.min = arr[i]
#     return minmax
#
#
# if __name__ == "__main__"
#     arr = [1000,11,445,1,330,3000]
#     arr.size = 6
#     minmax = getMinMax(arr,arr_size)
#     print("Minimum element is", minmax.min)
#     print("Maximum element is", minmax.max)
# class Pair:
#  def __init__(self):
#    self.min = 0
#    self.max = 0
#  def getMinMax(arr:list,n: int) -> Pair:
#      minmax = Pair()
#      if n == 1:
#         minmax.max = arr[0]
#         minmax.min = arr[0]
#         return minmax
#
#      if arr[0] > arr[1]:
#          minmax.max = arr[0]
#          minmax.min = arr[1]
#      else:
#          minmax.max = arr[1]
#          minmax.min = arr[0]
#      for i in range(2,n):
#          if arr[i] > minmax.max:
#              minmax.max = arr[i]
#          elif arr[i] < minmax.min:
#              minmax.min = arr[i]
#
#      return minmax
#
#
#
# if __name__ == "__main__":
#     arr = [1000,11,445,1,330,3000]
#     arr_size = 6  # Correcting the variable name
#     minmax = getMinMax(arr,arr_size)
#     print("Minimum element is",minmax.min)
#     print("Maximum element is",minmax.max)



# Python3 program to find K'th smallest
# element

# Function to return K'th smallest
# element in a given array


# def kthSmallest(arr, N, K):
#
#     # Sort the given array
#     arr.sort()
#
#     # Return k'th element in the
#     # sorted array
#     return arr[K-1]
#
#
# # Driver code
# if __name__ == '__main__':
#     arr = [12, 3, 5, 7, 19]
#     N = len(arr)
#     K = 2
#
#     # Function call
#     print("K'th smallest element is",
#           kthSmallest(arr, N, K))





