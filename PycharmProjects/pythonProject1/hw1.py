class person:
    def __init__(self, fullname, age, is_married, introduce_myself):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.introduce_myself = introduce_myself

class student(person):
    def __init__(self, fullname, age, is_married, introduce_myself, marks):
        super().__init__(fullname, age, is_married, introduce_myself)
        self.marks = marks

    def calculate_average_grade(self):
        if not self.marks:
            return 0
        total_grades = sum(self.marks.values())
        number_of_subjects = len(self.marks)
        return total_grades / number_of_subjects

islam_meshanlo = student(fullname= "islam_meshanlo", age= 17, is_married= 'not',
                         introduce_myself='love pubg', marks= 5)
print(f"fullname: {islam_meshanlo.fullname}, age: {islam_meshanlo.age}, is_married: {islam_meshanlo.is_married},"
      f"introduce_myself: {islam_meshanlo.introduce_myself}, marks: {islam_meshanlo.marks}")

class Teacher(person):
    def init(self, fullname, age, is_married, experience):
        super().init(fullname, age, is_married)
        self.experience = experience

    def base_salare(self):
        base_salare = 35000
        bonus = 0
        percentage = self.experience / 3
        if self.experience >= 3:
            bonus = (0.05 * percentage) * base_salare
            return f'зарплата учителя {self.fullname} составляет', base_salare + bonus


teacher = Teacher("Виктор", 34, True, 12)
teacher.introduce_myself()
print(f'зарплата{teacher.base_salare()}')

def create_students():
    students = [
        student('Алим', 17, False, {"математика": 5, "История": 5, "физика": 4}),
        student("Ислам", 16, False, {"математика": 4, "История": 4, "физика": 4}),
        student("Селим", 16, False, {"математика": 5, "История": 3, "физика": 4})
    ]

    return students


students = create_students()
for student in students:
    student.introduce_myself()
    print(f"оценки:{student.marks}\n"
          f"Средняя оценка: {student.average_marks()}\n")


