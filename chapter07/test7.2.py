# 7-4 比萨配料
prompt = "Please enter a topping:"
prompt += "\nEnter 'quit' to end the loop."
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print("We will add " + topping + " to your pizza!")

# 7-5 电影票
prompt = "Please enter your age."
prompt += "\nEnter 'quit to end the loop."
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Free")
        elif age <= 12:
            print("$10")
        else:
            print("$15")

# 7-6 三个出口
# 修改 7-5
# 用户输入'quit'时用break结束循环
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Free")
        elif age <= 12:
            print("$10")
        else:
            print("$15")

# while循环中使用条件测试结束循环
age = ""
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("Free")
        elif age <= 12:
            print("$10")
        else:
            print("$15")

# 7-7 无限循环
while True:
    print(1)

