#4-10 切片
my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'chicken']
print("The first three items in the list are:")
print(my_foods[:3])
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last three items in the list are:")
print(my_foods[-3:])

#4-11 你的比萨和我的比萨
pizzas = ['beef pizza', 'fruit pizza', 'seafood pizza']
friend_pizzas = pizzas[:]
pizzas.append('chicken pizza')
friend_pizzas.append('mutton pizza')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12 使用多个循环
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)