# ex a:
number: int = -1
while True:
    number = int(input("enter a number with 0-9999:"))
    if not 0 <= number <= 9999:
        continue;
    break;
l_num: list[int] = []
origin_number: int = number
while number > 0:
    l_num.append(number % 10)
    number //= 10
print(f"{"True" if len(l_num) == l_num.count(origin_number % 10) else "False"}")

# ex b:

x = int(input("enter origin price to pay (bigger then 0):"))
final_discount = 0;
match x:
    case _ if 0 <= x <= 100:
        final_discount = 10
    case _ if 100 <= x <= 200:
        final_discount = 20
    case _ if 200 <= x <= 500:
        final_discount = 30
    case _ if 500 <= x <= 800:
        final_discount = 40
    case _:
        print("invalid price")
my_sum = 0
discount = 10
while discount <= final_discount:
    if x >= 100:
        my_sum += ((100 * (100 - discount)) / 100)
        x -= 100
    else:
        my_sum += ((x * (100 - discount)) / 100)
    discount += 10
if my_sum:
    print("total after discount:", my_sum)

# ex c:

num1 = float(input("enter decimal number:"))
num2 = float(input("enter decimal number:"))
num3 = float(input("enter decimal number:"))
if num1 + num2 == num3 or num1 + num3 == num2 or num3 + num2 == num1:
    print("True")
else:
    print("False")

# ex d:
char_list = []
word = input("enter a word:")
while True:
    char = input("enter char: ")
    if char == "*":
        break
    char_list.append(char)

for c in char_list:
    if not c in word:
        print("False")

    word = word.replace(c, '')
else:
    if len(word) > 0:
        print("False")
    else:
        print("True")
