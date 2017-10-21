with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 将文件各行存储在一个列表中

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
