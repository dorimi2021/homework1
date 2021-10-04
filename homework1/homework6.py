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
