import csv
import datetime

from models.groups import Group
from models.subjects import Subject
from models.teachers import Teacher
from models.tickets import Tickets


class Exam:
    EXAM_DATE = datetime.date.today().strftime("%d %m, %Y")
    EXAM_FILES = 'exam_results/'
    FIELDNAMES = ['Студент', '№ билета', 'Преподаватель', 'Группа']

    def __init__(self, subject: Subject, teacher: Teacher, group: Group):
        self.subject = subject
        self.teacher = teacher
        self.group = group

        if self.subject.title not in teacher.subjects:
            raise ValueError("Subject not found in teacher's subjects")

    def spend_exam(self):
        student_ticket_dict = {}
        ticket = Tickets(self.subject)

        for student in self.group:
            student_ticket_dict[student] = next(next(ticket))

        with open(f'{self.EXAM_FILES}Экзамен по {self.subject}, {self.EXAM_DATE}, {self.group}.csv', 'w',
                  newline='\n') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            for student, ticket in student_ticket_dict.items():
                writer.writerow({'Студент': student, '№ билета': ticket})
            writer.writerow({'Преподаватель': self.teacher, 'Группа': self.group})
