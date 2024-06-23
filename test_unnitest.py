import unittest
from model import Student, Teacher, Course, EnrollmentStats
from unittest.mock import patch

class TestStudentCourseSystem(unittest.TestCase):
    def setUp(self):
        self.student1 = Student(1, "罗嘉烨", 20, "男", "龙岩市", "12345678901")
        self.student2 = Student(2, "乌有先生", 22, "男", "上海市", "19876543210")
        self.teacher1 = Teacher(1, "Professor ")
        self.course1 = Course(1, "软件工程", 2)
        self.course2 = Course(2, "嵌入式工程", 1)
        self.course3 = Course(3, "图像处理与模式识别", 2)
        self.stats = EnrollmentStats()

    def test_teacher_assign_course(self):
        result = self.teacher1.assign_course(self.course1)
        self.assertEqual(result, "✅ Professor  被分配教授课程：软件工程")
        result = self.teacher1.assign_course(self.course1)
        self.assertEqual(result, "⚠️ Professor  已经在教授 软件工程")

    def test_student_enroll_course(self):
        result = self.student1.enroll(self.course1)
        self.assertEqual(result, "✅ 罗嘉烨 成功选课：软件工程")
        result = self.student1.enroll(self.course1)
        self.assertEqual(result, "⚠️ 罗嘉烨 已经选了 软件工程")

        result = self.student2.enroll(self.course1)
        self.assertEqual(result, "✅ 乌有先生 成功选课：软件工程")

        result = self.student1.enroll(self.course2)
        self.assertEqual(result, "✅ 罗嘉烨 成功选课：嵌入式工程")
        
        result = self.student2.enroll(self.course2)
        self.assertEqual(result, "❌ 乌有先生 选课失败：嵌入式工程 已满员！")

    def test_course_is_full(self):
        self.student1.enroll(self.course2)
        self.assertTrue(self.course2.is_full())
        self.student2.enroll(self.course2)
        self.assertTrue(self.course2.is_full())

    @patch('builtins.print')
    def test_enrollment_stats(self, mock_print):
        self.student1.enroll(self.course1)
        self.student1.enroll(self.course2)
        self.student2.enroll(self.course1)
        self.stats.add_enrollment(self.student1, self.course1)
        self.stats.add_enrollment(self.student1, self.course2)
        self.stats.add_enrollment(self.student2, self.course1)
        
        self.stats.print_stats()

        mock_print.assert_any_call("📊 选课统计：")
        mock_print.assert_any_call("课程: 软件工程, 已选学生数: 2")
        mock_print.assert_any_call("课程: 嵌入式工程, 已选学生数: 1")

if __name__ == "__main__":
    unittest.main()
