"""
Swift-style class extension decorator.
Usage:
    @extend(SomeClass)
    def new_method(self):
        ...
"""

def extend(cls):
    if not isinstance(cls, type):
        raise TypeError(f"extend() の引数は型である必要があります。: {cls}")

    if cls.__module__ == "builtins":
        raise TypeError(
            f"{cls.__name__} は組み込み型であり、拡張できません。"
            "ユーザー定義クラスを拡張してください。"
        )

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator