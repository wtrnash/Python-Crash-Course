# 8-3 T恤
def make_shirt(size, words):
    """打印T恤尺码和字样"""
    print("The size of T-shirt is " + size + ".")
    print("There are words on T-shirt: " + words)


make_shirt('XL', 'Go Warriors!')


# 8-4 大号T恤
def make_shirt(size='L', words='I love Python'):
    """打印T恤尺码和字样"""
    print("The size of T-shirt is " + size + ".")
    print("There are words on T-shirt: " + words)


make_shirt()
make_shirt('M')
make_shirt('XL', 'Go Warriors!')


# 8-5 城市
def describe_city(city, country='China'):
    """打印城市及所属国家"""
    print(city + " is in " + country + ".")


describe_city('Hangzhou')
describe_city('Wuhan')
describe_city('New York','America')





