# 7-1 汽车租赁
car = input("What kind of car do you want to rent?")
print("Let mee see if i can find you a " + car)

# 7-2 餐馆订位
number = input("How many people have dinner there?")
number = int(number)
if number > 8:
    print("There is no empty table")
else:
    print("There is an empty table for you")

# 7-3 10的整数倍
number = input("Please input a number: ")
number = int(number)
if number % 10 == 0:
    print("It's a multiple of 10")
else:
    print("It is not a multiple of 10")


