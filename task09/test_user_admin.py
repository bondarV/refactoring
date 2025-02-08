import pytest
from user import User
from admin import Admin, Privileges


@pytest.fixture
def user1():
    return User("John", "Doe", "john.doe@example.com", "johnny", True)

@pytest.fixture
def user2():
    return User("Jane", "Smith", "jane.smith@example.com", "jane_doe", False)

@pytest.fixture
def admin_user():
    return Admin("Max", "Smith", "max.smith@example.com", "admin_max", True)


def test_user_attributes(user1):
    assert user1.first_name == "John"
    assert user1.last_name == "Doe"
    assert user1.email == "john.doe@example.com"
    assert user1.nickname == "johnny"
    assert user1.subscribe_newsletter == True


def test_user_greeting(user1, capsys):
    user1.greeting_user()
    captured = capsys.readouterr()
    assert "Hello, John! Welcome back." in captured.out


def test_increment_login_attempts(user1):
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    assert user1.login_attempts == 3


def test_reset_login_attempts(user1):
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.reset_login_attempts()
    assert user1.login_attempts == 0


def test_admin_privileges(admin_user, capsys):
    admin_user.priv.show_privileges()
    captured = capsys.readouterr()
    assert "Allowed to add message" in captured.out
    assert "Allowed to delete users" in captured.out
    assert "Allowed to ban users" in captured.out


def test_describe_user(user1, capsys):
    user1.describe_user()
    captured = capsys.readouterr()
    assert "Full Name: John Doe" in captured.out
    assert "Email: john.doe@example.com" in captured.out
    assert "Nickname: johnny" in captured.out
    assert "Subscribed to Newsletter: True" in captured.out
