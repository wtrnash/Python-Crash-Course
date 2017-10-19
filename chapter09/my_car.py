from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 通过方法修改属性的值
my_new_car.update_odometer(18)
my_new_car.read_odometer()

# 通过方法对属性的值进行递增
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

