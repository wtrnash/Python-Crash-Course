# 10-11 喜欢的数字
import json
number = input("Please input your love number")
filename = 'love_number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

with open(filename) as f_obj:
    love_number = json.load(f_obj)

print("I know your favorite number! It's " + love_number)

# 10-12 记住喜欢的数字
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("Please input your love number")
    filename = 'love_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
else:
    print("I know your favorite number! It's " + number)


# 10-13 验证用户
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户， 并指出其名字"""
    username = get_stored_username()
    if username:
        print("Is your name " + username + "?")
        is_name = input("Please input yes or no?")
        if is_name == 'yes':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
