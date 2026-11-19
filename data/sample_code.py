"""
Sample code: a simple user management system
Used to demonstrate code review features
"""


class UserManager:
    """Manage users."""

    def __init__(self):
        self.users = []

    def add_user(self, name, age, email):
        """Add a user."""
        user = {"name": name, "age": age, "email": email}
        self.users.append(user)
        return True

    def get_user(self, name):
        """Get user information."""
        for user in self.users:
            if user["name"] == name:
                return user
        return None

    def delete_user(self, name):
        """Delete a user."""
        for i, user in enumerate(self.users):
            if user["name"] == name:
                del self.users[i]
                return True
        return False

def calculate_average_age(users):
    """Compute mean age for a nonempty user list with numeric age values."""
    total = 0
    for user in users:
        total += user["age"]
    return total / len(users)

def send_email(email, message):
    """Simulate sending an email."""
    print(f"发送邮件到 {email}: {message}")
    return True

