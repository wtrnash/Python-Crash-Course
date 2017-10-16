#6-4 词汇表2
vocabulary = {
    'stack': 'LIFO',
    'queue': 'FIFO',
    'http': '应用层协议',
    'cpu': '中央处理器',
    'pop': '弹出',
    'for': 'for循环',
    'if': '条件语句',
    'list': '列表',
    'dict': '字典',
    'tuple': '元祖',
}

for key, value in vocabulary.items():
    print(key + ": " + value)

#6-5 河流
rivers = {
    'nile': 'egypt',
    'huang river': 'china',
    'hen river': 'indian',
}
for key, value in rivers.items():
    print("The " + key + " runs through " + value + ".")

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

#6-6 调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'nash', 'curry', 'edward']
for person in people:
    if person in favorite_languages.keys():
        print("Thank you for taking the poll, " + person)
    else:
        print("Please take the poll, " + person)
