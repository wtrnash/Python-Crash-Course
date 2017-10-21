# 10-6 加法运算
try:
    number1 = input("Please input a number:")
    number2 = input("Please input another number:")
    sum1 = int(number1) + int(number2)
    print(sum1)
except ValueError:
    print("Please input number.")

# 10-7 加法计算器
while True:
    try:
        number1 = input("Please input a number:")
        number2 = input("Please input another number:")
        sum1 = int(number1) + int(number2)
        print(sum1)
    except ValueError:
        print("Please input number.")
    else:
        break

# 10-8 猫和狗
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'
try:
    with open(filename_1) as file_object:
        print(file_object.read())
    with open(filename_2) as file_object:
        print(file_object.read())
except FileNotFoundError:
    print("File not exist!")

# 10-9 沉默的猫和狗
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'
try:
    with open(filename_1) as file_object:
        print(file_object.read())
    with open(filename_2) as file_object:
        print(file_object.read())
except FileNotFoundError:
    pass

# 10-10 常见单词
filename = 'little_women.txt'
with open(filename) as file_object:
    contents = file_object.read()

print(contents.lower().count('the'))
