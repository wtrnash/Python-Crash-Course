#6-7 人
person_0 = {'first_name': 'steve', 'last_name': 'nash', 'age': 43, 'city': 'the golden states'}
person_1 = {'first_name': 'stephen', 'last_name': 'curry', 'age': 29, 'city': 'the golden states'}
person_2 = {'first_name': 'kobe', 'last_name': 'bryant', 'age': 39, 'city': 'los Angeles'}

people = [person_0, person_1, person_2]
for person in people:
    print(person)

#6-8 宠物
pet_0 = {'kind': 'pig', 'master': 'wtr'}
pet_1 = {'kind': 'dog', 'master': 'star'}
pets = [pet_0, pet_1]
for pet in pets:
    print(pet)

#6-9 喜欢的地方
favorite_places ={
    'star': ['nei meng', 'hang zhou', 'wu han'],
    'wtr': ['phoenix', 'hang zhou'],
    'nash': ['canada', 'america'],
}
for name, places in favorite_places.items():
    print(name + " loves to go to:")
    for place in places:
        print(place)

#6-10 喜欢的数字
number = {
    'star': [4, 18],
    'nash': [13, 10, 3],
    'mike': [1],
    'kobe': [24, 8],
    'james': [23, 6],
}

for person, numbers in number.items():
    print(person + " loves:")
    for number in numbers:
        print(number)

#6-11 城市
cities = {
    'Hangzhou': {
        'country': 'china',
        'popularity': '8,000,000',
        'fact': 'beautiful',
    },
    'Phoenix': {
        'country': 'america',
        'popularity': '1,000,000',
        'fact': 'suns',
    },
    'Neimeng': {
        'country': 'china',
        'popularity': '2,000,000',
        'fact': 'grassland',
    },

}

for city, information in cities.items():
    print(city + "has these information:")
    print("country: " + information['country'])
    print("popularity: " + information['popularity'])
    print("fact: " + information['fact'])


