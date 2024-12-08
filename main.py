from models.exam import Exam
from models.groups import Group
from models.students import Student
from models.subjects import Subject
from models.teachers import Teacher
from utils import students_rating

# 6 студентов:
john = Student('John', 'Sinna', 20)
peter = Student('Peter', 'Parker', 25)
sandra = Student('Sandra', 'Bullock', 23)
james = Student('James', 'Smith', 25)
liza = Student('Liza', 'Wallace', 24)
nick = Student('Nick', 'Jack', 26)

# 3 предмета:
math = Subject('math', 5000, 5)
biology = Subject('biology', 4000, 4)
russian = Subject('russian', 3000, 3)

# 3 учителя:
jack = Teacher('Jack', 'Vorobei', '40', 'math')
katya = Teacher('Katya', 'Smith', '25', 'russian')
dasha = Teacher('Dasha', 'James', '25', 'biology')

# 2 группы, куда добавляем студентов:
group_1 = Group('Группа №1', john, peter, sandra)
group_2 = Group('Группа №2', james, liza, nick)

# 3 экзамена
biology_exam = Exam(biology, dasha, group_1)
math_exam = Exam(math, jack, group_2)
russian_exam = Exam(russian, katya, group_1)

# проставляем оценки студентам:
jack.set_grade(john, 'math', 5)
katya.set_grade(john, 'russian', 5)
dasha.set_grade(john, 'biology', 5)

jack.set_grade(sandra, 'math', 4)
katya.set_grade(sandra, 'russian', 2)
dasha.set_grade(sandra, 'biology', 1)

jack.set_grade(peter, 'math', 4)
katya.set_grade(peter, 'russian', 4)
dasha.set_grade(peter, 'biology', 4)

jack.set_grade(james, 'math', 4)
katya.set_grade(james, 'russian', 4)
dasha.set_grade(james, 'biology', 4)

jack.set_grade(liza, 'math', 3)
katya.set_grade(liza, 'russian', 4)
dasha.set_grade(liza, 'biology', 4)

jack.set_grade(nick, 'math', 4)
katya.set_grade(nick, 'russian', 4)
dasha.set_grade(nick, 'biology', 4)

# выводим рейтинг студентов лучшего студента:
print(students_rating([john, sandra, peter]))

# проверяем что у студента появится запись в атрибуте completed_courses при прохождении курса полностью
john.student_visit_a_lesson(math)
john.student_visit_a_lesson(math)
john.student_visit_a_lesson(math)
john.student_visit_a_lesson(math)
john.student_visit_a_lesson(math)
print(john.completed_courses)

# проверяем что учитель может провести урок и получить за это зарплату
# а студенты получат 1 час курса в словарь пройденных курсов
print(jack.salary)
print(john.total_lessons)
print(sandra.total_lessons)
jack.spend_a_lesson(math, group_1)
print(jack.salary)
print(john.total_lessons)
print(sandra.total_lessons)

# проверяем средний балл по группам и сравниваем:
print(group_1.average_grade_by_group())
print(group_2.average_grade_by_group())
print(group_1.average_grade_by_group() > group_2.average_grade_by_group())

# сравниваем студентов по оценкам:
print(john > peter)

# проводим экзамены:
print(biology_exam.spend_exam())
print(math_exam.spend_exam())
print(russian_exam.spend_exam())

print(john.average_grade())
