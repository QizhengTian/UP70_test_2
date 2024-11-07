class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"姓名: {self.name}, 年龄: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def include(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 教授科目: {self.subject}")
