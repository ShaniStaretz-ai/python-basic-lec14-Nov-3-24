def my_div(x:int,y:int=1):
    if y:
        print(x/y)
    else:
        print("can divide with 0")
my_div(10)
my_div(10,0)
my_div(9,4)