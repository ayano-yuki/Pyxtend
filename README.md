# pyxtend
Python に Swift の `extension` のような機能を追加する軽量ライブラリです。  
既存のクラスに対して、デコレーターを使ってメソッドを動的に追加できます。


## 📦 特徴
- ✅ Swift風の自然な構文でクラス拡張が可能
- ✅ `@extend(SomeClass)` のシンプルなAPI
- ✅ Python 3.8 以降対応


## 💡 使い方
## 自作クラスにも適用可能
```python
class User:
    def __init__(self, name):
        self.name = name

@extend(User)
def greet(self):
    return f"こんにちは、{self.name}さん！"

u = User("田中")
print(u.greet())  # => こんにちは、田中さん！
```

### 🔍 使い方の注意
- `extend()` はユーザー定義のクラスに対してメソッドを追加するためのデコレーターです。
- Pythonの組み込みイミュータブル型（`str`, `int`, `tuple` など）には属性追加できません。
- 組み込み型を拡張したい場合は、継承したサブクラスを作成してから `extend()` を使ってください。
- 既存の関数名と同じモノは追加出来ません。
```python
class MyStr(str):
    pass

@extend(MyStr)
def shout(self):
    return self.upper() + "!"

print(MyStr("hello").shout())  # HELLO!
```


## 🔍 注意点
- 本ライブラリは「モンキーパッチ」に近い仕組みで動作します。
- 組み込み型を拡張する場合、他のライブラリとの競合に注意してください。
- テストやプロダクション環境では、意図しない副作用がないかを確認することをおすすめします。


## 🛠 開発・テスト方法
```sh
# 仮想環境を作成
uv venv
. .venv/Scripts/activate

# テスト実行（pytest使用）
pytest
```

## その他
### ModuleNotFoundError: No module named 'pyxtend' の対処法
`pip install -e .` を使って、pyxtendを開発モードインストールする。このコマンドを使うことで、プロジェクトのソースコードをインストール先にコピーせずに、編集内容が即座に反映される状態でパッケージを利用できる。
```sh

# Windows
. .venv\Scripts\activate
# macOS/Linux
source .venv\Scripts\activate

uv pip install -e .
```