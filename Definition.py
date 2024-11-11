# -*- coding: utf-8 -*-
##
# @file    course_management.py
# @brief   课程管理系统，用于管理人员、教师、学生和课程。
# @details 定义了一组类来表示和管理教师、学生和课程的信息。允许添加和移除学生到课程中，并显示详细信息。
# @author  [您的名字]
# @version 1.0
# @date    [最后修改日期]
#

class Person:
    """
    @brief 人员基类
    @details 用于存储人员的基本属性，包括姓名和年龄。
    """

    def __init__(self, name, age):
        """
        @brief Person类的构造函数。
        @param name 人员的姓名。
        @param age 人员的年龄。
        """
        self.name = name  # 人员的姓名
        self.age = age    # 人员的年龄

    def introduce(self):
        """
        @brief 打印人员的基本信息。
        @details 显示人员的姓名和年龄。
        """
        print(f"姓名: {self.name}, 年龄: {self.age}")


class Teacher(Person):
    """
    @brief 教师类
    @details 扩展Person类，增加教师教授的科目。
    """

    def __init__(self, name, age, subject):
        """
        @brief Teacher类的构造函数。
        @param name 教师的姓名。
        @param age 教师的年龄。
        @param subject 教师教授的科目。
        """
        super().__init__(name, age)
        self.subject = subject  # 教师教授的科目

    def include(self):
        """
        @brief 打印教师的详细信息。
        @details 显示教师的姓名、年龄和教授科目。
        """
        print(f"姓名: {self.name}, 年龄: {self.age}, 教授科目: {self.subject}")


class Student(Person):
    """
    @brief 学生类
    @details 扩展Person类，增加学生所在的年级。
    """

    def __init__(self, name, age, grade):
        """
        @brief Student类的构造函数。
        @param name 学生的姓名。
        @param age 学生的年龄。
        @param grade 学生所在的年级。
        """
        super().__init__(name, age)
        self.grade = grade  # 学生所在的年级

    def include(self):
        """
        @brief 打印学生的详细信息。
        @details 显示学生的姓名、年龄和年级。
        """
        print(f"姓名: {self.name}, 年龄: {self.age}, 年级: {self.grade}")


class Course:
    """
    @brief 课程类
    @details 用于存储课程的名称、授课教师和学生名单，允许添加或删除学生，并显示课程信息。
    """

    def __init__(self, course_name, teacher):
        """
        @brief Course类的构造函数。
        @param course_name 课程的名称。
        @param teacher 授课教师（Teacher类实例）。
        """
        self.name = course_name            # 课程名称
        self.teacher = teacher.name        # 授课教师的姓名
        self.students = []                 # 学生名单，存储学生姓名
        self.students_all = {}             # 存储每位学生的详细信息（年龄和年级）

    def add_student(self, student):
        """
        @brief 向课程中添加学生。
        @param student 要添加的学生（Student类实例）。
        """
        self.students.append(student.name)  # 将学生的姓名添加到学生名单中
        self.students_all[student.name] = {
            "age": student.age,             # 学生的年龄
            "grade": student.grade          # 学生的年级
        }

    def remove_student(self, student):
        """
        @brief 从课程中移除学生。
        @param student 要移除的学生（Student类实例）。
        """
        if student.name in self.students:
            self.students.remove(student.name)  # 从学生名单中移除学生姓名
            del self.students_all[student.name] # 从详细信息中删除该学生的记录

    def show_course_info(self):
        """
        @brief 显示课程的详细信息。
        @details 包括课程名称、授课教师和所有学生的详细信息。
        """
        print(
            f"\n*****************************\n课程名称: {self.name}\n授课教师: {self.teacher}")
        print("详细学生信息:")
        for name, info in self.students_all.items():
            print(f"姓名: {name}, 年龄: {info['age']}, 年级: {info['grade']}")
        print("*****************************\n")

