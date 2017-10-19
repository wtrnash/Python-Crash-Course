# 9-10 导入Restaurant类
import restaurant
restaurant_0 = restaurant.Restaurant("kfc", 'junk food')
restaurant_0.describe_restaurant()

# 9-11 导入Admin类
import user
admin = user.Admin('Tian ran', 'Wang', [ 'read'], 'handsome')
admin.show_privileges()

# 9-12 多个模块
from only_user import User
from admin import Admin, Privileges
admin = Admin("steve", "nash", ["read"], "handsome")
admin.show_privileges()