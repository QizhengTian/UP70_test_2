class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"姓名: {self.name}, 年龄: {self.age}")