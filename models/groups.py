class Group:
    def __init__(self, number, *args):
        self.number = number
        self.students = list(args)

    def add(self, *args):
        for student in args:
            self.students.append(student)

    def average_grade_by_group(self):
        average = 0
        for student in self.students:
            try:
                average += student.average_grade()
            except TypeError:
                return None
        return average

    def remove(self, *args):
        self.students.remove(*args)

    def __iter__(self):
        return iter(self.students)

    def __getitem__(self, i):
        return self.students[i]

    def __setitem__(self, i, v):
        self.students[i] = v

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

    def __len__(self):
        return len(self.students)

    def __contains__(self, item):
        return item in self.students
