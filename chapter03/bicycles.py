#列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#访问列表元素
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

#索引值为-1时返回列表最后一个元素
print(bicycles[-1])

#使用列表中的值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)