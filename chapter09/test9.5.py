# 9-13 使用OrderedDict
from collections import OrderedDict
vocabulary = OrderedDict()

vocabulary['stack'] = 'LIFO'
vocabulary['queue'] = 'FIFO'
vocabulary['http'] = '应用层协议'
vocabulary['cpu'] = '中央处理器'
vocabulary['pop'] = '弹出'

for key, value in vocabulary.items():
    print(key + ": " + value)

# 9-14 骰子
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


die_0 = Die()
for i in range(10):
    die_0.roll_die()

die_1 = Die(10)
for i in range(10):
    die_1.roll_die()

die_2 = Die(20)
for i in range(20):
    die_2.roll_die()
