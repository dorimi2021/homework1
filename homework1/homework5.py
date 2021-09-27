#TASK 1
def unique(numbers):
    return list(set(numbers))

def test_unique():
    assert unique([1, 1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1]) == [1]
    assert unique([]) == []
    print("Task 1 done!")
test_unique()

#TASK 2
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
    print("Task 2 done!")
test_count_words()

#Task 3
def consistent_string(strings, allowed):
    response = set()
    for string in strings:
        flag = True
        for char in string:
            if allowed.__contains__(char):
                continue
            else:
                flag = False
        if flag:
            response.add(string)
    return response


def test_consistent_string():
    assert consistent_string(allowed="ab", strings=["ad", "bd", "aaab", "baa", "badab"]) == {"aaab", "baa"}
    assert consistent_string(allowed="abc", strings=["a", "b", "c", "ab", "ac", "bc", "abc"]) == {"a", "b", "c", "ab",
                                                                                                  "ac", "bc", "abc"}
    assert consistent_string(allowed="cad", strings=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == {"cc", "acd",
                                                                                                           "ac", "d"}
    print("Task 3 done!")


test_consistent_string()

#Task 4
def sort_desc(strings):
    strings.sort(reverse=True)
    return strings


def test_sort_desc():
    assert sort_desc(["ad", "bd", "aaab", "baa", "badab"]) == ['bd', 'badab', 'baa', 'ad', 'aaab']
    assert sort_desc(["a", "b", "c", "ab", "ac", "bc", "abc"]) == ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a']
    print("Task 4 done!")


test_sort_desc()

#Task 5
def filter_even(numbers):
    s=list(filter(lambda x: x%2 == 0,numbers))
    return s

def test_filter_even():
    assert filter_even([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]) == [2, 4, 6, 8, 10, 12]
    assert filter_even([2, 2, 4, 6, 6, 8, 10, 12]) == [2, 2, 4, 6, 6, 8, 10, 12]
    assert filter_even([1, 1, 2, 3]) == [2]
    assert filter_even([1, 3, 5]) == []
    print("Task 5 done!")
test_filter_even()
