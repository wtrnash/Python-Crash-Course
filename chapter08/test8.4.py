# 8-9 魔术师
def show_magicians(magicians):
    """打印魔术师的名字"""
    for magician in magicians:
        print(magician)


magicians = ['wtr', 'star', 'nash']
show_magicians(magicians)


# 8-10 了不起的魔术师
def make_great(magicians):
    """在每个魔术师名字前加上'the Great'"""
    count = 0
    while count < len(magicians):
        magicians[count] = "the Great " + magicians[count]
        count += 1


make_great(magicians)
show_magicians(magicians)


# 8-11 不变的魔术师
def make_great(magicians):
    """在每个魔术师名字前加上'the Great'返回一个新的列表"""
    count = 0
    while count < len(magicians):
        magicians[count] = "the Great " + magicians[count]
        count += 1

    return magicians


magicians = ['wtr', 'star', 'nash']
new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)

