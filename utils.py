def students_rating(students: list):
    rating = sorted(students, reverse=True)
    for student in rating:
        return student.first_name, student.average_grade()
