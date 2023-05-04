## Task2
# a = int(input())
# b = int(input())
# n = input()
# if n == 'max':
#     if a > b:
#         print(a)
#     elif a == b:
#         print(a)
#     else:
#         print(b)
# if n == 'min':
#     if a > b:
#         print(b)
#     elif a == b:
#         print(a)
#     else:
#         print(a)
# else:
#     'error'

# # Task2
# a = int(input())
# b = int(input())
# if a > 100 and b > 100:
#     choise = input('Input +, -, average or * ')
#     if choise == '+':
#         print(a+b)
#     elif choise == '-':
#         if a > b:
#             print(a-b)
#         elif a< b:
#             print(b-a)
#         else:
#             print(0)
#     elif choise == 'average':
#         print((a+b)/2)
#     elif choise == '*':
#         print(a*b)
#     else:
#         print('Wrong choise')
# else:
#     print('Error! Numbers are < 100')

# #Task 5
# x = int(input())
# y = int(input())
# login = input('Choose "Admin - a", "User - b", "New USer - c": ')
# if login == 'a':
#     level = input('You are Admin. Choose Full (a1) of Part (a2): ')
#     if level == 'a1':
#         print('sum = ', x+y)
#     elif level == 'a2':
#         print('multiply = ', x*y)
#     else:
#         print('wrong choise')
# elif login == 'b':
#     level = input('You are User. Choose Full (b1) of Part (b2): ')
#     if level == 'b1':
#         print('minus = ', x-y)
#     elif level == 'b2':
#         print('devide = ', x/y)
#     else:
#         print('wrong choise')
# elif login == 'c':
#     print('You are New User. Go to Admin')
# else:
#     print('Error')

# a = 5; print(a)

# import numpy as np
# for i in np.arange(1, 10, 2):
#     print(i)

# for i in range(1, 10):
#     if i == 5:
#         continue
#     elif i == 8:
#         break
#     print(i)

a = int(input())
while a < 10:
    print(a)
    a +=1
