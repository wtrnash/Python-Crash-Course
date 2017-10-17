# 7-8 熟食店
sandwich_orders = ['beef sandwich', 'seafood sandwich', 'fruit sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("All of sandwiches have been finished:")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9 五香烟熏牛肉卖完了
sandwich_orders = ['beef', 'pastrami', 'seafood', 'pastrami', 'fruit', 'pastrami', 'pastrami']
print("pastrami have been sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# 7-10 梦想的度假胜地
places = {}
while True:
    username = input("Please input your username")
    place = input("If you could visit one place in the world, where would you go?")
    places[username] = place
    repeat = input("Do you want to input another username? (yes/no)")
    if repeat == 'no':
        break

for username, place in places.items():
    print(username + ":" + place)

