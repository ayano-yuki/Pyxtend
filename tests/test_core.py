import pytest
from pyxtend import extend

class User:
    def __init__(self, name):
        self.name = name

def test_user_greet():
    @extend(User)
    def greet(self):
        return f"こんにちは、{self.name}さん！"
    
    u = User("田中")
    assert u.greet() == "こんにちは、田中さん！"

def test_extend_str_error():
    with pytest.raises(TypeError):
        @extend(str)
        def shout(self):
            return self.upper() + "!"