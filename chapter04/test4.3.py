#4-3 数到20
for number in range(1, 21):
    print(number)

#4-4 一百万
#numbers = list(range(1, 1000001))
#for number in numbers:
#   print(number)

#4-5 计算 1~1000000的总和
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6 奇数
odds_number = list(range(1, 21, 2))
for number in odds_number:
    print(number)

#4-7 3的倍数
numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)

#4-8 立方
numbers = []
for number in range(1, 11):
    numbers.append(number ** 3)
print(numbers)

#4-9 立方解析
numbers = [value ** 3 for value in range(1, 11)]
print(numbers)
