# n = int(input())
# for i in range(1,n+1):
#     for j in range (1, n+1):
#         print("*",end = '')
#     print()
#
# n = int(input())
# for i in range(1,n+1):
#     for j in range (1, n+1):
#         print(i,end ='')
#     print()
#
# n = int(input())
# for i in range(1,n+1):
#     for j in range (1, n+1):
#         print(j,end ='')
#     print()
#
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(i,end = '')
#     print()
#
n = int(input())
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(j, end = '')
#     print()

#k =1  , 1 to from 1 and 2 to start from 2
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         print('{:2d}'.format(k), end='')
#         k+=1
#     print()

# k =2  # 1 to from 1 and 2 to start from 2
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         print('{:2d}'.format(k), end=' ') #1 then print all the odd number and 2 to print all the even number
#         k+=2
#     print()

# for i in range (1,n+1):
#     for j in range(1, n+1):
#         print((i*j), end=' ')
#     print()


for i in range(1, n+1):
    p = i;
    for y in range(1,n+1):
        print('{:2d} '.format(p), end='')
        p +=n;
    print()