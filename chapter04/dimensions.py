#定义元祖
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#遍历元祖中的所有值
for dimension in dimensions:
    print(dimension)

#修改元祖变量
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)