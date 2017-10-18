# 8-6 城市名
def city_country(city, country):
    """返回城市和属于的国家"""
    return city + ", " + country


print(city_country('Hangzhou', 'China'))
print(city_country('Phoenix', 'America'))
print(city_country('Wuhan', 'China'))


# 8-7 专辑
def make_album(singer, name, count=''):
    """创建描述音乐专辑的字典"""
    if count:
        album = {'singer': singer, 'name': name, 'count': count}
    else:
        album = {'singer': singer, 'name': name}
    return album


album_0 = make_album("孙燕姿", "逆光")
album_1 = make_album("孙燕姿", "是时候")
album_2 = make_album("张杰", "我想", 10)
print(album_0)
print(album_1)
print(album_2)


# 8-8 用户的专辑
while True:
    print("请输入一个专辑的歌手和名称，你可以随时输入'q'来退出")

    singer = input("请输入歌手:")
    if singer == 'q':
        break

    name = input("请输入名称:")
    if name == 'q':
        break

    album = make_album(singer, name)
    print(album)


