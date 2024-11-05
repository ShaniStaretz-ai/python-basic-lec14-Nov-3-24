from statistics import mean


# ex a:
def my_ascending(number1: int, number2: int) -> None:
    """ accepts 2 int parameters and prints the numbers in ascending order."""
    print(sorted([number1, number2]))


# ex b:
def my_details(str1: str) -> None:
    """ accepts a string str and prints the first character of the string, the middle character, and the last character."""
    print(str1[0], str1[len(str1) // 2], str1[len(str1) - 1])


# ex c:
def say_bool(bool1: bool) -> None:
    """accepts a boolean. If the boolean is True it will print "yes"
Otherwise it will print "no"."""
    print(f"{"yes" if bool1 else "no"}")


# ex d:
def print_zugi(l1: list[int]) -> None:
    """accepts as a parameter a list of numbers and prints for each number in the list "even" or "odd"."""
    for num in l1:
        print(f"{"even" if num % 2 == 0 else "odd"}", end=" ")
    print()


# ex e:
def my_statistics(grades: list[int]) -> None:
    """accepts list of grades and prints the highest grade, the lowest grade, the number of grades, the average grade"""
    if not grades:
        print("no grades to analyze")
    else:
        print("highest grade:", max(grades))
        print("lowest grade:", min(grades))
        print("total grades:", len(grades))
        print("avg:", mean(grades))
