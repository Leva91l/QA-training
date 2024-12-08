import random

from models.human import Human


class Student(Human):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.grades = {}
        self.total_lessons = {}
        self.completed_courses = []

    def average_grade(self):
        avg = []
        for grade in self.grades.values():
            if isinstance(grade, int):
                avg.append(grade)
            elif isinstance(grade, list):
                avg += grade
        try:
            return round(sum(avg) / len(avg), 2)
        except ZeroDivisionError:
            return None

    def student_visit_a_lesson(self, lesson):
        if lesson in self.total_lessons:
            self.total_lessons[lesson] += 1
        else:
            self.total_lessons[lesson] = 1

        total = self.total_lessons.get(lesson)
        if total >= lesson.total_hours:
            self.completed_courses.append(lesson)

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Only students can be compared')
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Only students can be compared')
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Only students can be compared')
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Only students can be compared')
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Only students can be compared')
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Only students can be compared')
        return self.average_grade() >= other.average_grade()

    def __hash__(self):
        index = random.randint
        return hash(index)
