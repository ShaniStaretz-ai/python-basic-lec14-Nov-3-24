def my_div(x:int,y:int=1):
    if y:
        print(x/y)
    else:
        print("can divide with 0")


def my_power(x:int,x_power:int):
    return x**x_power

my_div(10)
my_div(10,0)
my_div(9,4)
print("my_power:",my_power(5,3))