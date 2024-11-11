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

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def include(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 年级: {self.grade}")

class Course:
    def __init__(self, course_name, teacher):
        self.name = course_name
        self.teacher = teacher.name
        self.students = []
        self.students_all = {}

    def add_student(self, student):
        self.students.append(student.name)
        self.students_all[student.name] = {
            "age": student.age,
            "grade": student.grade
        }

    def remove_student(self, student):
        if student.name in self.students:
            self.students.remove(student.name)
            del self.students_all[student.name]

    def show_course_info(self):
        print(
            f"\n*****************************\n课程名称: {self.name}\n授课教师: {self.teacher}")
        print("详细学生信息:")
        for name, info in self.students_all.items():
            print(f"姓名: {name}, 年龄: {info['age']}, 年级: {info['grade']}")
        print("*****************************\n")
        
