# TASK 1
# def unique(numbers):
#     return list(set(numbers))
#
# def test_unique():
#     assert unique([1, 1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
#     assert unique([1, 1, 1, 1]) == [1]
#     assert unique([]) == []
#     print("Great your solution works!")
# test_unique()

# TASK 2
def count_words(string):

    my_dict = {}
    for str in string:
        my_dict[str] = 0
    for str in string:
        count = my_dict.get(str)
        count += 1
        my_dict[str] = count
    return my_dict



def test_count_words():
    assert count_words(["text", "text", "apple", "orange", "yellow", "orange"]) == {
        "text": 2,
        "apple": 1,
        "orange": 2,
        "yellow": 1
    }
    assert count_words(["text", "text", "text", "text", "text", "orange"]) == {
        "text": 5,
        "orange": 1,
    }
    assert count_words([]) == {}
    print("success")


test_count_words()
