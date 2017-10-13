#字符串改变大小写
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#字符串拼接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

#制表符、换行符的使用
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#删除空白
favorite_language = 'python   '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())