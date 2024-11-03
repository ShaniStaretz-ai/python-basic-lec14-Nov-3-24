def half_num(num):
    """gets a number and returns half of it (as int)"""
    return int(num / 2)


def smaller_num(num1: float, num2: float):
    """gets 2 floats and returns the smaller one"""
    return num1 if num1 < num2 else num2


def longer_str(str1, str2):
    """gets 2 string and returns the longer string"""
    return str1 if len(str1) > len(str2) else str2;


def bool_equal(bool1, bool2):
    """gets 2 bool and returns True if they are the same otherwise False"""
    return bool1 == bool2


def longer_list(list1, list2):
    """gets 2 list and returns the longer list"""
    return list1 if len(list1) >= len(list2) else list2;


def reversed_str(str1):
    """gets a string and returns the reversed string"""
    return str1[::-1]


def is_in_list(word: str, list1: list[str]):
    """gets a word and a list[word] return true if the word appear in the
    list otherwise returns false"""
    return word in list1


# bonus:
def index_in_list(word: str, list1: list[str]):
    """gets a word and a list[word] return index of the word, if it appears in the list.
    otherwise returns None"""
    if is_in_list(word, list1):
        return list1.index(word)
    return None;
