
class User:
    def __init__(self, first_name, last_name, email, nickname, subscribe_newsletter):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.subscribe_newsletter = subscribe_newsletter
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Nickname: {self.nickname}")
        print(f"Subscribed to Newsletter: {self.subscribe_newsletter}")

    def greeting_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
