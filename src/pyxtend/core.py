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
        if hasattr(cls, func.__name__):
            raise AttributeError(
                f"{cls.__name__} にはすでに '{func.__name__}' が存在します。上書きは許可されていません。"
            )
        setattr(cls, func.__name__, func)

        if not hasattr(cls, '__extensions__'):
            cls.__extensions__ = []
        cls.__extensions__.append(func.__name__)
        
        return func
    return decorator