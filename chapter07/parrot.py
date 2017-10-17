message = input("Tell me something, and I will repeat it back tou you: ")
print(message)

# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back tou you:"
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# 使用标志
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

