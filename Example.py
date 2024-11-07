# 从 Definition.py 导入所有类
from Definition import *

# 测试代码
Teacher1 = Teacher("田eason", 19, "拉丁")
Teacher2 = Teacher("Mr.Zhang", 30, "高数")

Student1 = Student("小明", 18, "大二")
Student2 = Student("小志", 18, "大二")
Student3 = Student("阿伟", 18, "大二")

Latin = Course("拉丁", Teacher1)
Math = Course("高数", Teacher2)

Math.add_student(Student1)
Math.add_student(Student2)
Latin.add_student(Student3)

Math.show_course_info()
Latin.show_course_info()

Math.remove_student(Student1)
Math.show_course_info()