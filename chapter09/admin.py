from only_user import User


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