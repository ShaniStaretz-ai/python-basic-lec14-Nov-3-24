def half_num(num) -> int:
    """gets a number and returns half of it (as int)"""
    return int(num / 2)


print("half_num(8):", half_num(8))
print("half_num(9):", half_num(9))


def smaller_num(num1: float, num2: float) -> float:
    """gets 2 floats and returns the smaller one"""
    return num1 if num1 < num2 else num2  ## or return min(a,b)


print("smaller_num(8, 9):", smaller_num(8, 9))
print("smaller_num(10, 9):", smaller_num(10, 9))


def longer_str(str1: str, str2: str) -> str:
    """gets 2 string and returns the longer string"""
    return str1 if len(str1) > len(str2) else str2;


print('longer_str("abcde", "ab"):', longer_str("abcde", "ab"))
print('longer_str("fgh", "i"):', longer_str("fgh", "i"))


def bool_equal(bool1: bool, bool2: bool) -> bool:
    """gets 2 bool and returns True if they are the same otherwise False"""
    return bool1 == bool2


print("bool_equal(True, False):", bool_equal(True, False))
print("bool_equal(False, False):", bool_equal(False, False))


def longer_list(list1: list, list2: list) -> list:
    """gets 2 list and returns the longer list"""
    return list1 if len(list1) >= len(list2) else list2;


print("longer_list([1, 2, 3], [4, 5]):", longer_list([1, 2, 3], [4, 5]))
print("longer_list([], [6,7]):", longer_list([6, 7], [6, 7]))


def reversed_str(str1: str) -> str:
    """gets a string and returns the reversed string"""
    return str1[::-1]


print('reversed_str("NONO"):', reversed_str("NONO"))


def is_in_list(word: str, list1: list[str]) -> bool:
    """gets a word and a list[word] return true if the word appear in the
    list otherwise returns false"""
    return word in list1


print('is_in_list("banana", ["banana", "apple"]):', is_in_list("banana", ["banana", "apple"]))
print('is_in_list("orange", ["banana", "apple"]):', is_in_list("orange", ["banana", "apple"]))


# bonus:
def index_in_list(word: str, list1: list[str]) -> int | None:
    """gets a word and a list[word] return index of the word, if it appears in the list.
    otherwise returns None"""
    if is_in_list(word, list1):
        return list1.index(word)
    return None;


print('index_in_list("banana", ["banana", "apple"]):', index_in_list("banana", ["banana", "apple"]))
print('index_in_list("orange", ["banana", "apple"]):', index_in_list("orange", ["banana", "apple"]))
