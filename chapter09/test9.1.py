# 9-1 餐馆
class Restaurant:
    """模拟餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆名和菜肴类型"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆信息"""
        print("restaurant name: " + self.restaurant_name)
        print("cuisine_type: " + self.cuisine_type)

    def open_restaurant(self):
        """表示餐厅正在营业"""
        print("restaurant is open!")


restaurant = Restaurant("KFC", "junk food")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 三家餐馆
restaurant_0 = Restaurant("M", "junk food")
restaurant_1 = Restaurant("hamburger king", "hamburger")
restaurant_2 = Restaurant("黄焖鸡米饭", "中餐")
restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()


# 9-3 用户
class User:
    """描述用户信息的类"""
    def __init__(self, first_name, last_name, *profile):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile

    def describe_user(self):
        """打印用户信息摘要"""
        print(self.first_name)
        print(self.last_name)
        print(self.profile)

    def greet_user(self):
        """问候用户"""
        print("Hello, " + self.first_name + " " + self.last_name + "!")


user_1 = User('wang', 'tianran', 'a', 'b', 'c')
user_2 = User('steve', 'nash', 'handsome')
user_1.describe_user()
user_1.greet_user()
user_2.greet_user()
user_2.describe_user()
