# ex a:
number: int = -1
while True:
    number = int(input("enter a number with 0-9999:"))
    if not 0 <= number <= 9999:
        continue;
    break;
l_num: list[int] = []
origin_number:int = number
while number > 0:
    l_num.append(number % 10)
    number //= 10
print(f"{"True" if len(l_num) == l_num.count(origin_number % 10) else "False"}")

#ex b:

x=int(input("enter origin price to pay (bigger then 0):"))
list_2_pay=[]
my_sum=0
discount=0;
while True:
    discount+=10
    if x>=100:
        my_sum+=((100*(100-discount))/100)
        x-=100
    else:
        my_sum +=((x * (100 - discount)) / 100)
        break
if my_sum:
    print("total after discount:",my_sum)

#ex c:

num1=float(input("enter decimal number:"))
num2=float(input("enter decimal number:"))
num3=float(input("enter decimal number:"))
if num1+num2==num3 or num1+num3==num2 or num3+num2==num1:
    print("True")
else:
    print("False")


#ex d:
char_list=[]
word=input("enter a word:")
while True:
    char=input("enter char: ")
    if char=="*":
        break
    char_list.append(char)

for c in char_list:
    if not c in word:
        print("False")

    word= word.replace(c, '')
else:
    if len(word)>0:
        print("False")
    else:
        print("True")