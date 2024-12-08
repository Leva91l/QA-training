from models.groups import Group
from models.human import Human
from models.students import Student
from models.subjects import Subject


class Teacher(Human):

    def __init__(self, first_name, last_name, age, subjects):
        super().__init__(first_name, last_name, age)
        self.subjects: list = [subjects]
        self.salary = 0

    def set_grade(self, student: Student, course, grade):
        if course in self.subjects:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise ValueError('This teacher cannot teach this subject!')

    def spend_a_lesson(self, subject: Subject, group: Group):
        if subject.title in self.subjects:
            self.salary += subject.payment_per_hour
            for students in group:
                students.student_visit_a_lesson(subject)
        else:
            raise ValueError('This teacher cannot teach this subject!')
