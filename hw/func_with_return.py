# ex a:
def my_avg(number1: int, number2: int) -> float:
    """accepts 2 int parameters and returns a float of their average."""
    return (number1 + number2) / 2


# ex b:
def my_headline(str1: str) -> str:
    """accepts a parameter of type str and returns str of that string in uppercase letters with '!' at the end of the sentence."""
    return str1.upper() + '!'


# ex c:
def concat_list(l1: list[int], l2: list[int], l3: list[int]) -> list[int]:
    """gets 3 lists of int and returns a merged list"""
    return l1 + l2 + l3


# aid function:
def get_grades_list() -> list[int]:
    """collect valid grades from the user, till enter the number -99, and returns it."""
    grades: list[int] = []
    while True:
        grade = int(input("enter a student's grade:"))
        if grade == -99:
            break
        if grade < 0 or grade > 100:
            continue;
        grades.append(grade)
    return grades
