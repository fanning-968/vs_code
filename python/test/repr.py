class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # 这个字符串应该尽可能准确地描述对象
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        # 用户友好的描述
        return f"{self.name}，{self.age}岁"

p = Person("Alice", 30)
print(repr(p))  # 输出: Person(name='Alice', age=30)
print(str(p))   # 输出: Alice，30岁
