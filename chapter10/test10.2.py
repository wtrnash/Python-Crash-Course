# 10-3 访客
filename = 'guest.txt'
name = input("Please input your name:")
with open(filename, 'w') as file_object:
    file_object.write(name)

# 10-4 访客名单
filename = 'guest_book.txt'
while True:
    name = input("Please input your name(you can enter 'q' to quit):")
    if name == 'q':
        break
    print("Hello, " + name + " !")
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')

# 10-5 关于编程的调查
filename = 'programming_reasons.txt'
while True:
    reason = input("Please input why you love programming(you can enter 'q' to quit):")
    if reason == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(reason + '\n')
