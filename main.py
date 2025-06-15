from pyxtend import extend

class User:
    def __init__(self, name):
        self.name = name

@extend(User)
def greet(self):
    return f"Hello, {self.name}!"

user = User("Alice")
print(user.greet())  # 出力: Hello, Alice!