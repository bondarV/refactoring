# Файл: main.py

from user import User
from admin import Admin


if __name__ == '__main__':
    user1 = User("John", "Doe", "john.doe@example.com", "johnny", True)
    user2 = User("Jane", "Smith", "jane.smith@example.com", "jane_doe", False)

    user1.describe_user()
    user1.greeting_user()

    user2.describe_user()
    user2.greeting_user()

    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    print(f"Login attempts for {user1.first_name}: {user1.login_attempts}")

    user1.reset_login_attempts()
    print(f"Login attempts for {user1.first_name} after reset: {user1.login_attempts}")

    admin_user = Admin("Max", "Smith", "max.smith@example.com", "admin_max", True)
    admin_user.priv.show_privileges()
