# 9-4 就餐人数
class Restaurant:
    """模拟餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆名和菜肴类型"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆信息"""
        print("restaurant name: " + self.restaurant_name)
        print("cuisine_type: " + self.cuisine_type)

    def open_restaurant(self):
        """表示餐厅正在营业"""
        print("restaurant is open!")

    def set_number_served(self, number_served):
        """设置就餐人数"""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """增加就餐人数"""
        self.number_served += increment


restaurant = Restaurant("kfc", "junk food")
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(100)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)

# 9-5 尝试登陆次数
"""描述用户信息的类"""
class User:
    def __init__(self, first_name, last_name, *profile):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        print(self.first_name)
        print(self.last_name)
        print(self.profile)

    def greet_user(self):
        """问候用户"""
        print("Hello, " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        """登陆次数加一"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """登陆次数置0"""
        self.login_attempts = 0


user = User('steve', 'nash', 'handsome')
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)