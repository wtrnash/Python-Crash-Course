#5-8 以特殊方式跟管理员打招呼
users = ['admin', 'star', 'nash', 'kobe', 'james']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again")

#5-9 处理没有用户的情形
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some users!")

#5-10 检查用户名
current_users = ['admin', 'star', 'Nash', 'kobe', 'james']
new_users = ['admin', 'curry', 'NASH', 'kidd', 'jordan']
lower_current_users = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print("The user name have been used! You need to input another user name!")
    else:
        print("The user name have not been used!")

#5-11序数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
