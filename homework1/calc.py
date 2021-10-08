import re

def calc(expression: str) -> int:
    sign = re.split("[0-9]", expression)
    if (len(sign) < 3):
        return 0
    numbers = re.split("\+|\-|\/|\*", expression)
    if ''.join(sign) == '+':
        return int(numbers[0]) + int(numbers[1])
    elif ''.join(sign) == '-':
        return int(numbers[0]) - int(numbers[1])
    elif ''.join(sign) == '*':
        return int(numbers[0]) * int(numbers[1])
    elif ''.join(sign) == '/':
        return int(numbers[0]) / int(numbers[1])
