import calc
import string
import new

new.factorial(55)

expression: str = input()
res = calc.calc(expression)
print(res)

print(string.has_substring('hello', 'hello there'))
print(string.is_number('4'))
print(string.is_case_insensitive_equal("AAbbAA", "aaBBaA"))