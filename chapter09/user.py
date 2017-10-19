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


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限"""
        for privilege in self.privileges:
            print(privilege)