# Task 1
def sum_diagonal(table):
    sum = 0
    for x in range(len(table)):
        for y in range(len(table[0])):
            if x == y:
                sum = sum + table[x][y]
    return sum


def test_sum_diagonal():
    assert sum_diagonal([
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]) == 6
    assert sum_diagonal([
        [0, 2, 3],
        [1, 0, 3],
        [1, 2, 0]
    ]) == 0
    assert sum_diagonal([
        [-1, 2, 3],
        [1, 2, 3],
        [1, 2, -3]
    ]) == -2
    assert sum_diagonal([
        [1, 2],
        [1, 2],
    ]) == 3
    assert sum_diagonal([
        [1],
    ]) == 1
    print("Test 1 passed")


test_sum_diagonal()


# Task 2
def max_in_row(table):
    max = [0] * len(table)
    for x in range(len(table)):
        max[x] = table[x][0]
        for y in range(len(table[x])):
            if table[x][y] > max[x]:
                max[x] = table[x][y]
    return max


def test_max_in_row():
    assert max_in_row([
        [1, 2, 3, 4, 1],
        [1, -1, 1, 2, 1],
        [-4, -3, -2, -1]
    ]) == [4, 2, -1]
    assert max_in_row([
        [1],
        [2],
        [3],
    ]) == [1, 2, 3]
    assert max_in_row([
        [-1, -2, -3, -4],
        [-1, -1, -1, -2],
        [-4, -3, -2, -1]
    ]) == [-1, -1, -1]
    print("Test 2 passed")


test_max_in_row()


# Task 3
def sum_of_row(table):
    y = []
    z = []
    for i in range(len(table)):
        stroki = 0
        for j in range(len(table[0])):
            stroki += table[i][j]
        y.append(stroki)
    return y


def test_sum_of_row():
    assert sum_of_row([
        [1, 2, 3, 4],
        [1, -1, 1, 2],
        [-4, -3, -2, -1]
    ]) == [10, 3, -10]
    assert sum_of_row([
        [1, 2, 3, 4],
        [0, 0, 0, 0],
        [1, 1, 1, 1]
    ]) == [10, 0, 4]
    assert sum_of_row([
        [1, 2, 3],
        [1, -1, 1],
        [-4, -3, -2]
    ]) == [6, 1, -9]
    print("Test 3 passed")


test_sum_of_row()


# Task 4
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    print("Test 4 passed")


test_fibonacci()


# Task 5
def recursive_pow(a, n):
    if n == 0:
        return 1
    elif n >= 1:
        return recursive_pow(a, n - 1) * a


def test_recursive_pow():
    assert recursive_pow(2, 5) == 2 ** 5
    assert recursive_pow(2, 0) == 1
    assert recursive_pow(1, 100) == 1
    assert recursive_pow(1, 0) == 1
    assert recursive_pow(3, 2) == 9
    assert recursive_pow(4, 4) == 4 ** 4
    print("Test 5 passed")


test_recursive_pow()
