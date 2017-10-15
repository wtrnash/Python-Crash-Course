#5-1 条件测试
person = 'nash'
print("Is person == 'nash'? I predict True.")
print(person == 'nash')

print("\nIs person == 'curry'? I predict False")
print(person == 'curry')

print("\nIs person != 'curry'? I predict True")
print(person != 'curry')

print("\nIs person == 'Nash'? I predict False")
print(person == 'Nash')

print("\nIs person.title() == 'Nash'? I predict True")
print(person.title() == 'Nash')

#5-2 更多的条件测试
str1 = 'abc'
print(str1 == 'abc')
print(str1 == 'cba')

str2 = 'AbC'
print(str2 == 'abc')
print(str2.lower() == 'abc')

num1 = 8
num2 = 12
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(str1 == 'abc' and num1 < num2)
print(str1 == 'cba' or num1 <= num2)

persons = ['mike', 'john']
print('sarah' in persons)
print('sarah' not in persons)