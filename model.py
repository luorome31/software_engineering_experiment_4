class Student:
    def __init__(self, student_id, name, age, gender, address, phone):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
        self.courses = []

    def enroll(self, course):
        if course.is_full():
            return f"❌ {self.name} 选课失败：{course.course_name} 已满员！"
        else:
            if course not in self.courses:
                self.courses.append(course)
                course.add_student(self)
                return f"✅ {self.name} 成功选课：{course.course_name}"
            else:
                return f"⚠️ {self.name} 已经选了 {course.course_name}"

    def __str__(self):
        return (f"学生号: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, "
                f"通讯地址: {self.address}, 联系电话: {self.phone}, 已选课程: {[course.course_name for course in self.courses]}")


class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.set_teacher(self)
            return f"✅ {self.name} 被分配教授课程：{course.course_name}"
        else:
            return f"⚠️ {self.name} 已经在教授 {course.course_name}"

    def __str__(self):
        return f"教师号: {self.teacher_id}, 姓名: {self.name}, 教授课程: {[course.course_name for course in self.courses]}"


class Course:
    def __init__(self, course_id, course_name, max_students):
        self.course_id = course_id
        self.course_name = course_name
        self.max_students = max_students
        self.students = []
        self.teacher = None

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            return f"❌ 无法添加 {student.name} 到 {self.course_name}：课程已满员！"

    def set_teacher(self, teacher):
        self.teacher = teacher

    def is_full(self):
        return len(self.students) >= self.max_students

    def __str__(self):
        return (f"课程号: {self.course_id}, 课程名: {self.course_name}, 教师: {self.teacher.name if self.teacher else '未分配'}, "
                f"已选学生: {[student.name for student in self.students]}, 最大容量: {self.max_students}")


class EnrollmentStats:
    def __init__(self):
        self.enrollments = []

    def add_enrollment(self, student, course):
        if (student, course) not in self.enrollments:
            self.enrollments.append((student, course))

    def print_stats(self):
        stats = {}
        for student, course in self.enrollments:
            if course.course_name not in stats:
                stats[course.course_name] = 0
            stats[course.course_name] += 1

        print("📊 选课统计：")
        for course_name, count in stats.items():
            print(f"课程: {course_name}, 已选学生数: {count}")
    