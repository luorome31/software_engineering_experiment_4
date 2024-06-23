from model import Student, Teacher, Course, EnrollmentStats

def main():
    # 创建学生
    student1 = Student(1, "罗嘉烨", 20, "男", "龙岩市", "12345678910")
    student2 = Student(2, "乌有先生", 22, "男", "京海市", "8888888888")
    
    # 创建老师
    teacher1 = Teacher(1, "Professor Ren")
    
    # 创建课程
    course1 = Course(1, "软件工程", 2)
    course2 = Course(2, " 嵌入式系统", 1)
    course3 = Course(3, "图像处理与模式识别", 2)
    
    # 创建选课统计对象
    stats = EnrollmentStats()

    # 分配课程给老师
    print(teacher1.assign_course(course1))
    
    # 学生选课
    print(student1.enroll(course1))
    print(student1.enroll(course1))  # 重复选课
    print(student2.enroll(course1))
    
    # 课程已满员
    print(student2.enroll(course2))
    print(student1.enroll(course2))
    print(student2.enroll(course2))
    
    # 记录选课
    stats.add_enrollment(student1, course1)
    stats.add_enrollment(student1, course2)
    stats.add_enrollment(student2, course1)
    
    # 打印选课统计
    stats.print_stats()

    # 打印学生信息
    print(student1)
    print(student2)

    # 打印课程信息
    print(course1)
    print(course2)
    print(course3)

if __name__ == "__main__":
    main()
