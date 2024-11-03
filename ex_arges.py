def my_sub(x=0, y=0):
    """print the diff of 2 numbers
    the numbers are argument. default value == 0"""
    print(f"{x}-{y}={x - y}")


def my_bigger_number(x=0, y=0, z=0):
    """print the biggest of 3 number
     the numbers are argument. default value == 0"""

    print(f"the bigger num is:{x if x > y and x > z else (y if y > z else z)}")


def list_length(l1=None):
    """function that gets a list[int] and print its length"""
    if l1 is None:
        l1 = []
    print(len(l1))


def diff_max_min(l1: list[int]):
    """function that gets a list of int
    print the diff between the max and the min"""
    print(f"{(max(l1) - min(l1)) if l1 else "list is empty"}")


def head_2_tail(my_str: str):
    """function that gets 1 string as parameter
    print tail equals head or not"""
    print(f"the string {my_str} - head {"" if my_str[::-1].lower() == my_str.lower() else "is not"} equals tail")


def bool_equals(bool1: bool=False, bool2: bool=False):
    """function that gets 2 booleans as parameter
    print "the same" if they are the same
    print "different" if they are different"""
    print(f"{"the same" if bool1 == bool2 else "different"} boolean values")


def my_sorted_list(new_float1: float, new_float2: float):
    """function that gets 2 floats as parameter
     create a list from these 2 floats
     sort the list and print it"""
    l2: list = [new_float1, new_float2]
    l2.sort()
    print("new sorted list:", l2)


#### callings:

my_sub(9999, 4444)
my_sub()

my_bigger_number(-10, -100, 1)
list_length([1, 2, 3, 4, 5])
diff_max_min([900, 1010, -87, 0, 10_000])
diff_max_min([])
for word in [ "radar", "apple", "level", "civic", "noon", "shalom"]:
    head_2_tail(word)
head_2_tail("maGo")
head_2_tail("leveL")

bool_equals(True, True)
bool_equals(False, True)
my_sorted_list(9, 5)
