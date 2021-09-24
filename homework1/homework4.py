# TASK 1
def count_greater_or_equal(numbers, x):
    s = 0
    for number in numbers:
        if (number >= x):
            s += 1
    return s

def test_count_greater_or_equal():
    assert count_greater_or_equal([1, 2, 3, 4, 5], 2) == 4
    assert count_greater_or_equal([1, 2, 3, 4, 5], 1) == 5
    assert count_greater_or_equal([1, 2, 3, 4, 5], 0) == 5
    assert count_greater_or_equal([0, 1], 2) == 0
    assert count_greater_or_equal([], 2) == 0
    print("Great your solution works!")
test_count_greater_or_equal()

# TASK 2
def rotate(numbers, n):
    return numbers[-n:] + numbers[:-n]

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

# TASK 3
def extend(a, b):
    return a + b

def test_extend():
    assert extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extend([4, 5, 6], [1, 2, 3], ) == [4, 5, 6, 1, 2, 3]
    assert extend([], [4, 5, 6]) == [4, 5, 6]
    assert extend([1, 2, 3], []) == [1, 2, 3]
    assert extend([1], [4]) == [1, 4]
    print("Great your solution works!")
test_extend()

# TASK 4
def is_prime(n):
    if n == 0 or n == 1:
        return False
    num = 2
    while n % num != 0:
        num += 1
    return num == n

def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(24) is False
    assert is_prime(5) is True
    assert is_prime(0) is False
    assert is_prime(107) is True
    assert is_prime(19) is True
    print("Great your solution works!")
test_is_prime()


# TASK 5
def merge(a, b):
    n = m = 0
    list = []
    while n < len(a) and m < len(b):
        if a[n] < b[m]:
            list.append(a[n])
            n += 1
        else:
            list.append(b[m])
            m += 1
    list += a[n:]
    list += b[m:]
    return list

def test_merge():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], []) == [4, 5, 6]
    assert merge([], [1, 3, 5]) == [1, 3, 5]
    assert merge([], []) == []
    print("Great your solution works!")
test_merge()

# TASK 6
def has_substring(s, t):
    search_len = len(t)
    for index in range(0, len(s) - search_len + 1):
        ser = s[index:index + search_len]
        if ser == t:
            return True
    return False

def test_has_substring():
    assert has_substring("some text", "text") is True
    assert has_substring("some text", "some") is True
    assert has_substring("", "text") is False
    assert has_substring("text", "") is True  # любая строка содержит в себе пустую подстроку
    assert has_substring("", "") is True  # даже пустая строка содержит в себе пустую подстроку :)
    print("Great your solution works!")
test_has_substring()
