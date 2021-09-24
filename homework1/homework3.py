#  BEGIN Task 1  Цельсий в Фаренгейт
print("Insert °C: ")
cel = float(input())
far = cel * 9 / 5 + 32
print(far)
#  END

#  BEGIN Task 2  Модуль числа
print("Insert number: ")
number = int(input())
if number >= 0:
    print(number)
else:
    print(number * -1)
#  END

#  BEGIN Task 2 - 2
print("Insert number: ")
print(abs(int(input())))
#  END

# BEGIN Task 3  Голосование
print("Insert 1 or 0: ")
x=int(input())
y=int(input())
z=int(input())
if ((x+y+z)<=1):
    print (False)
else:
    print (True)
#  END
# BEGIN Task 3 - 2
print("Insert 1 or 0: ")
x=int(input())
y=int(input())
z=int(input())
print(x+y+z>1)
#  END

# BEGIN Task 3 - 3
print("Insert 1 or 0: ")
print(int(input())+int(input())+int(input())>1)
#  END

# BEGIN Task 3 - 4
print("Insert 1 or 0: ")
sum = 0
for i in range(0, 3):
    sum += int(input())
print(sum>1)
#  END

# BEGIN Task 4  Факториал
print("Insert number: ")
n = int(input())
fact = 1
for number in range(1, n + 1):
    fact = fact * number
print(fact)
#  END

# BEGIN Task 5  Произведение четных чисел
print("Insert number: ")
n = int(input())
a = 1
for number in range(2, n + 1, 2):
    a = a * number
print(a)
#  END

# BEGIN Task 6  Количество "а"
string=input("Input sentence: ")
s=0
for n in string:
    if n == "a":
        s=s+1
print(s)
#  END

# BEGIN Task 7   Количество гласных
string=input("Input sentence: ")
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
print(str(a+e+i+o+u+y) + f" (a-{a}, e-{e}, i-{i}, o-{o}, u-{u}, y-{y})")
# END

# BEGIN Task 7   Количество согласных
string=input("Input sentence: ")
let=0
for n in string:
    if n != "a" and n != "e" and n != "i" and n != "o" and n != "u" and n != "y" and n != " ":
        let+=1
print(let)
# END

# BEGIN Task 8   Обратный порядок
string = input("Input sentence: ")
result = ""
for current in range(len(string) - 1, -1, -1):
    result += string[current]
print(result)
# END

# BEGIN Task 9   Пирамида
n = int(input("Input number: "))
for number in range (1, n+1):
    t=""
    for inner in range(1, number + 1):
        t+=" "+str(number)
    print(t)
# END

