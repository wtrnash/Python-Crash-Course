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