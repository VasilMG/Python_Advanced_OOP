import unittest
from unittest import TestCase

from project.student import Student

class StudentTests(TestCase):
    NAME = 'Pesho'

    def setUp(self) -> None:
        self.the_student = Student(self.NAME)

    def test_init_without_courses(self):
        self.assertEqual(self.NAME, self.the_student.name)
        self.assertEqual({}, self.the_student.courses)

    def test_init_with_courses(self):
        current_student = Student(self.NAME, {'mathematics': ['difficult', 'note2']})
        self.assertEqual(self.NAME, current_student.name)
        self.assertEqual({'mathematics': ['difficult', 'note2']}, current_student.courses)

    def test_enroll_when_course_in_courses_expect_update(self):
        current_student = Student(self.NAME, {'mathematics': ['difficult', 'note2']})
        self.assertEqual("Course already added. Notes have been updated.", current_student.enroll('mathematics', ['note3', 'note4']))
        self.assertEqual({'mathematics': ['difficult', 'note2', 'note3', 'note4']}, current_student.courses)

    def test_enroll_when_course_not_in_courses_and_add_notes_not_passed(self):
        course = 'python'
        notes = ['note1', 'note2']
        current_student = Student(self.NAME)
        result = current_student.enroll(course, notes)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in current_student.courses)
        self.assertEqual({'python':['note1', 'note2']}, current_student.courses)

    def test_enroll_when_course_not_in_courses_and_add_notes_y(self):
        course = 'python'
        notes = ['note1', 'note2']
        current_student = Student(self.NAME)
        result = current_student.enroll(course, notes, 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in current_student.courses)
        self.assertEqual(notes, current_student.courses[course])

    def test_just_enroll_course_when_add_notes_not_blank_or_Y(self):
        course = 'python'
        notes = ['note1', 'note2']
        current_student = Student(self.NAME)
        result = current_student.enroll(course, notes, 'N')
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course in current_student.courses)
        self.assertEqual([], current_student.courses[course])

    def test_add_notes_raises_error_when_course_not_in_courses(self):
        with self.assertRaises(Exception) as exc:
            self.the_student.add_notes('History', 'jajdhjwj')
        self.assertEqual("Cannot add notes. Course not found.", str(exc.exception))

    def test_add_notes_when_course_exists(self):
        current_student = Student(self.NAME, {'mathematics': ['note2']})
        result = current_student.add_notes('mathematics', 'note3')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note2','note3'], current_student.courses['mathematics'])

    def test_leave_course_raises_error_when_course_not_in_courses(self):
        with self.assertRaises(Exception) as exc:
            self.the_student.leave_course('History')
        self.assertEqual("Cannot remove course. Course not found.", str(exc.exception))

    def test_leave_course_when_course_in_courses(self):
        current_student = Student(self.NAME, {'mathematics': ['note2']})
        result = current_student.leave_course('mathematics')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, current_student.courses)

if __name__ == '__main__':
    unittest.main()