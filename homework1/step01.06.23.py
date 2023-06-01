# Калькулятор на основе class
# class Calc:
#     def __init__(self, num1, oper, num2):
#         self.num1 = num1
#         self.oper = oper
#         self.num2 = num2
#
#     def calculate(self):
#         if self.oper == '+':
#             res = self.num1 + self.num2
#             return res
#         elif self.oper == '-':
#             res = self.num1 - self.num2
#             return res
#         elif self.oper == '*':
#             res = self.num1 * self.num2
#             return res
#         elif self.oper == '/':
#             res = self.num1 / self.num2
#             return res
#         else:
#             return print('error')
#
# a=int(input('Input num1 '))
# b=int(input('Input num2 '))
# oper = input('Input operation ')
# n = Calc(a,oper,b)
# print(n.calculate())
#############################################################
# class Calc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def add(self):
#         return self.a+self.b
#     def minus(self):
#         return self.a-self.b
#     def mult(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
#     def squ(self):
#         return self.a**self.b
#     def min(self):
#         return min(self.a,self.b)
#     def max(self):
#         return max(self.a,self.b)
#     def percent(self):
#         return self.b/100*self.a
#
# # MAIN PART
# def main():
#     n = input('Calculate - yes [y] or no[n]: ')
#     while n == 'y':
#         a = int(input('Input a: '))
#         c = input('Input +, -, *, /, ^, min, max, %: ')
#         b = int(input('Input b: '))
#         result = Calc(a,b)
#         if c == '^':
#             print('Degree= ',result.squ())
#         elif c == '+':
#             print('Sum = ',result.add())
#         elif c == '+':
#             print('Minus = ',result.minus())
#         elif c == '*':
#             print('Multiply = ',result.mult())
#         elif c == '/':
#             print('Division = ',result.div())
#         elif c == 'min':
#             print('Minimum = ',result.min())
#         elif c == 'max':
#             print('Maximum = ',result.max())
#         elif c == '%':
#             print('Percent = ',result.percent())
#         else:
#             print('Select correct operation')
#         n = input('Calculate - yes or no: ')
#     else:
#         print('Thank you! Have a nice day!')
#
# main()
###############################################################################
# lst = [0, -2, 8, 10, 13, 9, 17, 6, 21, 27, -13, -31, 19, 22, 36]
# print(lst)
# print(max(lst))
# print(min(lst))
# even = sorted([i for i in lst if i % 2 == 0])
# print(even)
# odd = sorted([i for i in lst if i % 2 != 0])
# print(odd)
#############################################################################
# class Classlist:
#     def __init__(self,lst):
#         self.lst=lst
#
#     def maxlist(self):
#         return max(self.lst)
#     def minlist(self):
#         return min(self.lst)
#     def even(self):
#         return sorted([i for i in self.lst if i % 2 == 0])
#     def odd(self):
#         return sorted([i for i in self.lst if i % 2 != 0])
#
# def main():
#     lst = [0, -2, 8, 10, 13, 9, 17, 6, 21, 27, -13, -31, 19, 22, 36]
#     result=Classlist(lst)
#     print('Maximum=', result.maxlist())
#     print('Minimum=', result.minlist())
#     print('Even=', result.even())
#     print('Odd=', result.odd())
# main()
#######################################################################
# class Classlist:
#     def __init__(self,lst):
#         self.lst=lst
#
#     def separetaBy(self, isNum=True):
#         if(isNum):
#             return [i for i in self.lst if type(i) == int]
#         else:
#             return [i for i in self.lst if type(i) == str]
#
# def main():
#     lst =  ["Game","App",5,0,-10,48,"Play","Music",10,8,31,"Movie"]
#     result=Classlist(lst)
#
#     print(result.separetaBy(True))
#
# main()
###############################################################################
class Classlisttext:
    def __init__(self,lst):
        self.lst=lst
    def textlist(self):
        return [i for i in self.lst if type(i)==str]
    def numlist(self):
        return [i for i in self.lst if type(i)==int]

def main():
    lst =  ["Game","App",5,0,-10,48,"Play","Music",10,8,31,"Movie"]
    result=Classlisttext(lst)
    print(result.textlist())
    print(result.numlist())

main()
