#6-1 人
person = {'first_name': 'steve', 'last_name': 'nash', 'age': 43, 'city': 'the golden states'}
print(person)
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2 喜欢的数字
number = {
    'star': 4,
    'nash': 13,
    'mike': 1,
    'kobe': 24,
    'james': 23,
}

print("star loves " + str(number['star']))
print("nash loves " + str(number['nash']))
print("mike loves " + str(number['mike']))
print("kobe loves " + str(number['kobe']))
print("james loves " + str(number['star']))

#6-3 词汇表
vocabulary = {
    'stack': 'LIFO',
    'queue': 'FIFO',
    'http': '应用层协议',
    'cpu': '中央处理器',
    'pop': '弹出',
}

print("stack:" + vocabulary['stack'])
print("queue:" + vocabulary['queue'])
print("http:" + vocabulary['http'])
print("cpu:" + vocabulary['cpu'])
print("pop:" + vocabulary['pop'])