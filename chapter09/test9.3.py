# 9-6 冰淇淋小店
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


class IceCreamStand(Restaurant):
    """冰淇淋小店"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """初始化"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        """展示冰淇淋口味"""
        for flavor in self.flavors:
            print(flavor)


flavors = ['apple', 'banana', 'mango']
iceCreamStand = IceCreamStand("KFC", "junk food", flavors)
iceCreamStand.show_flavors()


# 9-7 管理员
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


class Admin(User):
    """管理员"""
    def __init__(self, first_name, last_name, privileges, *profile):
        """初始化"""
        super().__init__(first_name, last_name, profile)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        """显示管理员权限"""
        self.privileges.show_privileges()


# 9-8 权限
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限"""
        for privilege in self.privileges:
            print(privilege)


admin = Admin("Tian ran", "Wang", ['add', 'remove'], 'handsome', 'tall')
admin.show_privileges()


# 9-9 电瓶升级
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """汽车有油箱"""
        print("This car need a gas tank!")

class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


car = ElectricCar('BMW', 's', 2016)
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()