class Grades_cmp:
    def __eq__(self, other):
        return avr_grade(self) == avr_grade(other)

    def __ne__(self, other):
        return avr_grade(self) != avr_grade(other)

    def __lt__(self, other):
        return avr_grade(self) < avr_grade(other)

    def __le__(self, other):
        return avr_grade(self) <= avr_grade(other)

    def __gt__(self, other):
        return avr_grade(self) > avr_grade(other)

    def __ge__(self, other):
        return avr_grade(self) >= avr_grade(other)

class Student(Grades_cmp):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка! Оценка не доступна'
    
    def __str__(self):
        rtn = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {round(avr_grade(self),2)}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {",".join(self.finished_courses)}\n')
        return rtn

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        rtn = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return rtn

class Lecturer(Mentor, Grades_cmp):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        rtn = super().__str__()
        rtn += f'Средняя оценка за лекции: {round(avr_grade(self),2)}\n'
        return rtn

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка! Оценка не доступна'

def avr_grade(cls_with_grade):
    if isinstance(cls_with_grade, Student) or isinstance(cls_with_grade, Lecturer):
        list_avg_grade = list(map(lambda el: sum(el)/len(el), cls_with_grade.grades.values()))
        return sum(list_avg_grade)/len(list_avg_grade)
    else:
        return f'Ошибка! Расчет не доступен'

def main():
    best_student = Student('Ruoy', 'Eman', 'male')
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['Git']
    poor_student = Student('Albert', 'Epstein', 'male')
    poor_student.courses_in_progress += ['Python']
    poor_student.courses_in_progress += ['Git']
    poor_student.finished_courses += ['Git']

    some_reviewer = Reviewer('Some', 'Buddy')
    some_reviewer.courses_attached += ['Python']
    
    some_lecturer = Lecturer('John', 'Smith')
    some_lecturer.courses_attached += ['Python']

    best_student.rate_lecture(some_lecturer, 'Python', 10) 
    best_student.rate_lecture(some_lecturer, 'Python', 9)
    poor_student.rate_lecture(some_lecturer, 'Git', 9)

    some_reviewer.rate_hw(best_student, 'Python', 10)
    some_reviewer.rate_hw(best_student, 'Python', 10)
    some_reviewer.rate_hw(best_student, 'Python', 9)

    some_reviewer.rate_hw(best_student, 'Git', 7)
    some_reviewer.rate_hw(best_student, 'Git', 9)
    some_reviewer.rate_hw(best_student, 'Git', 10)

    some_reviewer.rate_hw(poor_student, 'Python', 9)
    some_reviewer.rate_hw(poor_student, 'Python', 7)
    some_reviewer.rate_hw(poor_student, 'Python', 9)

    some_reviewer.rate_hw(poor_student, 'Git', 7)
    some_reviewer.rate_hw(poor_student, 'Git', 6)
    some_reviewer.rate_hw(poor_student, 'Git', 10)

    print(f'Оценки студента {best_student.name} {best_student.surname} за курс Python {best_student.grades["Python"]}')
    print(f'Оценки лектора {some_lecturer.name} {some_lecturer.surname} за курс Python {some_lecturer.grades["Python"]}')
    print(some_lecturer)
    print(some_reviewer)
    print(best_student)
    print(poor_student)
    print(best_student < poor_student)

if __name__ == "__main__":
  main()