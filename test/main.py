# def count_greater_or_equal(numbers, x):
#     s=0
#     for number in numbers:
#         if (number>=x):
#             s+=1
#     return s
# #print(count_greater_or_equal((1,2,3,4,5), 2))
#
# def test_count_greater_or_equal():test_count_greater_or_equal
#     assert count_greater_or_equal([1, 2, 3, 4, 5], 2) == 4
#     assert count_greater_or_equal([1, 2, 3, 4, 5], 1) == 5
#     assert count_greater_or_equal([1, 2, 3, 4, 5], 0) == 5
#     assert count_greater_or_equal([0, 1], 2) == 0
#     assert count_greater_or_equal([], 2) == 0
#     print("Great your solution works!")
#
# test_count_greater_or_equal()

def rotate(numbers, rotateIndex):
    if len(numbers) == 0:
        return numbers
    arrayCorect = 1
    numbersLen = len(numbers) - arrayCorect
    for outer in range(0, rotateIndex):
        lastElement = numbers[numbersLen]
        for inner in range(0, numbersLen):
            rotatePosition = numbersLen - arrayCorect - inner
            bigger = numbers[rotatePosition]
            numbers[rotatePosition + arrayCorect] = bigger
        numbers[0] = lastElement
    return numbers


def test_rotate():
    assert rotate([1, 2, 3], 1) == [3, 1, 2]
    assert rotate([1, 2, 3], 2) == [2, 3, 1]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    assert rotate([1], 1) == [1]
    assert rotate([1], 0) == [1]
    assert rotate([], 2) == []
    print("Great your solution works!")


test_rotate()
