import pytest
from pyxtend import extend

# テスト用クラス
class User:
    def __init__(self, name):
        self.name = name

# 正常系：新しいメソッドを追加できる
def test_extend_adds_method():
    @extend(User)
    def greet(self):
        return f"こんにちは、{self.name}さん！"

    user = User("田中")
    assert user.greet() == "こんにちは、田中さん！"
    assert "greet" in User.__extensions__

# 異常系：非クラス型を渡す
def test_extend_with_non_type_raises():
    with pytest.raises(TypeError, match="extend\\(\\) の引数は型である必要があります。"):
        @extend(123)
        def fake(self):
            return "NG"

# 異常系：組み込み型を渡す
def test_extend_builtin_type_raises():
    with pytest.raises(TypeError, match="は組み込み型であり、拡張できません。"):
        @extend(str)
        def shout(self):
            return self.upper() + "!"

# 異常系：すでに存在するメソッド名を追加
def test_extend_existing_method_raises():
    class Product:
        def price(self):
            return 1000

    with pytest.raises(AttributeError, match="にはすでに 'price' が存在します。"):
        @extend(Product)
        def price(self):
            return 2000

# 正常系：異なるメソッド名は追加できる
def test_extend_multiple_methods():
    class Animal:
        def __init__(self, name):
            self.name = name

    @extend(Animal)
    def speak(self):
        return f"{self.name} が鳴いた！"

    @extend(Animal)
    def run(self):
        return f"{self.name} が走った！"

    a = Animal("ねこ")
    assert a.speak() == "ねこ が鳴いた！"
    assert a.run() == "ねこ が走った！"
    assert Animal.__extensions__ == ["speak", "run"]
