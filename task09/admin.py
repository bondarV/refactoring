# Файл: admin.py

from user import User

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, subscribe_newsletter):
        super().__init__(first_name, last_name, email, nickname, subscribe_newsletter)
        self.priv = Privileges()
