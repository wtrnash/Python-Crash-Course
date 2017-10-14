#3-4嘉宾名单
people = ['john', 'mike', 'sarah', 'nash', 'kobe']
print(people[0].title() + "," + people[1].title() + "," + people[2].title() + "," + people[3].title() + "," +
      people[4].title() + ", welcome to have dinner with me!")

#3-5修改嘉宾名单
print("It's a pity that " + people[1] + " can't enter my dinner.")
people[1] = 'james'
print(people[0].title() + "," + people[1].title() + "," + people[2].title() + "," + people[3].title() + "," +
      people[4].title() + ", welcome to have dinner with me!")

#3-6添加嘉宾
print("I have found a bigger table")
people.insert(0, "curry")
people.insert(3, "durant")
people.insert(7, "kidd")
print(people[0].title() + "," + people[1].title() + "," + people[2].title() + "," + people[3].title() + "," +
      people[4].title() + "," + people[5].title() + "," + people[6].title() + "," +
      people[7].title() + ", welcome to have dinner with me!")

#3-7缩减名单
print("Sorry, only two persons can have dinner with me")
person = people.pop()
print("Sorry " + person + ", I can't invite you to enter my dinner")
person = people.pop()
print("Sorry " + person + ", I can't invite you to enter my dinner")
person = people.pop()
print("Sorry " + person + ", I can't invite you to enter my dinner")
person = people.pop()
print("Sorry " + person + ", I can't invite you to enter my dinner")
person = people.pop()
print("Sorry " + person + ", I can't invite you to enter my dinner")
person = people.pop()
print("Sorry " + person + ", I can't invite you to enter my dinner")
print(people[0] + ", you still can have dinner with me!")
print(people[1] + ", you still can have dinner with me!")
del people[1]
del people[0]
print(people)
