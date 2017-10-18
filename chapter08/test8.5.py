# 8-12 三明治
def sandwich(*toppings):
    """打印加在三明治中的配料"""
    print(toppings)


sandwich('mushrooms', 'cheese', 'beef')
sandwich('fruit')
sandwich('fish', 'apple')

# 8-13 用户简介
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


profile = build_profile('Tian ran', 'Wang', age='21', hometown='Hangzhou', university='ZJU')
for key,value in profile.items():
    print(key + ":" + value )


# 8-14 汽车
def make_car(manufacturer,model,**information):
    """将汽车信息存储在字典中"""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key,value in information.items():
        car_info[key] = value

    return car_info


car = make_car('subaru', 'outback', color='blue', two_package=True)
for key,value in car.items():
    print(key + ":" + str(value))
