# #  BEGIN Task 1  Цельсий в Фаренгейт
# print("Insert °C")
# cel = float(input())
# far = cel * 9 / 5 + 32
# print(far)
# #  END
#
# #  BEGIN Task 2  Модуль числа
# print("Insert number")
# number = int(input())
# if number >= 0:
#     print(number)
# else:
#     print(number * -1)
# #  END
#
# #  BEGIN Task 2 - 2
# print("Insert number")
# print(abs(int(input())))
# #  END
#
# # BEGIN Task 3  Голосование
# x=int(input())
# y=int(input())
# z=int(input())
# if ((x+y+z)<=1):
#     print (False)
# else:
#     print (True)
# #  END
# # BEGIN Task 3 - 2
# x=int(input())
# y=int(input())
# z=int(input())
# print(x+y+z>1)
# #  END
#
# # BEGIN Task 3 - 3
# print(int(input())+int(input())+int(input())>1)
# #  END
#
# # BEGIN Task 3 - 4
# sum = 0
# for i in range(0, 3):
#     sum += int(input())
# print(sum>1)
# #  END
#
# # BEGIN Task 4  Факториал
# print("Insert number")
# n = int(input())
# fact = 1
# for number in range(1, n + 1):
#     fact = fact * number
# print(fact)
# #  END
#
# # BEGIN Task 5  Произведение чисел
# print("Insert number")
# n = int(input())
# a = 1
# for number in range(2, n + 1, 2):
#     a = a * number
# print(a)
# #  END
#
# # BEGIN Task 6  Количество "а"
# string=input()
# s=0
# for n in string:
#     if n == "a":
#         s=s+1
# print(s)
# #  END
#
# # BEGIN Task 7   Количество гласных
string=input()
a=e=i=o=u=y=0
for n in string:
    if n == "a":
        a+=1
    if n == "e":
        e += 1
    if n == "i":
        i += 1
    if n == "o":
        o += 1
    if n == "u":
        u += 1
    if n == "y":
        y += 1
print(f"a={a} e={e} i={i} o={o} u={u} y={y}")
print("Sum="+str(a+e+i+o+u+y))
#  END

