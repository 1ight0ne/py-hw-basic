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

def avr_grade(person, course='all'):
    if isinstance(person, Student) or isinstance(person, Lecturer):
        if course == 'all':
            list_avg_grade = list(map(lambda el: sum(el)/len(el), person.grades.values()))
            return sum(list_avg_grade)/len(list_avg_grade)
        elif course in person.grades:
            return sum(person.grades[course])/len(person.grades[course])
        else:
            return 0
    return 'Ошибка! Расчет не доступен'

def multi_avr_grade(course, *persons):
    sum = 0
    count = len(persons)
    for person in persons:
        sum += avr_grade(person, course)
        if avr_grade(person, course) == 0:
            count -= 1
    return sum/count

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
    some_reviewer.courses_attached += ['Git']

    some_lecturer = Lecturer('John', 'Smith')
    some_lecturer.courses_attached += ['Python']
    new_lecturer = Lecturer('Nick', 'Jenkins')
    new_lecturer.courses_attached += ['Git']

    print(best_student.rate_lecture(some_lecturer, 'Python', 10))
    print(best_student.rate_lecture(some_lecturer, 'Python', 9))
    print(poor_student.rate_lecture(some_lecturer, 'Git', 9))
    print(poor_student.rate_lecture(new_lecturer, 'Git', 9))
    print(best_student.rate_lecture(new_lecturer, 'Git', 10))
    print(poor_student.rate_lecture(some_lecturer, 'Python', 5))

    print(some_reviewer.rate_hw(best_student, 'Python', 10))
    print(some_reviewer.rate_hw(best_student, 'Python', 10))
    print(some_reviewer.rate_hw(best_student, 'Python', 9))
    print(some_reviewer.rate_hw(best_student, 'Git', 7))
    print(some_reviewer.rate_hw(best_student, 'Git', 9))
    print(some_reviewer.rate_hw(best_student, 'Git', 10))
    print(some_reviewer.rate_hw(poor_student, 'Python', 9))
    print(some_reviewer.rate_hw(poor_student, 'Python', 7))
    print(some_reviewer.rate_hw(poor_student, 'Python', 9))
    print(some_reviewer.rate_hw(poor_student, 'Git', 7))
    print(some_reviewer.rate_hw(poor_student, 'Git', 6))
    print(some_reviewer.rate_hw(poor_student, 'Git', 10))

    print(f'Оценки студента {best_student.name} {best_student.surname} за курс Python {best_student.grades["Python"]}\n')
    print(f'Оценки лектора {some_lecturer.name} {some_lecturer.surname} за курс Python {some_lecturer.grades["Python"]}\n')
    print(some_lecturer)
    print(new_lecturer)
    print(some_reviewer)
    print(best_student)
    print(poor_student)
    print(best_student < poor_student)
    print(avr_grade(best_student, course='Python'))
    print(avr_grade(poor_student, course='Python'))
    print(multi_avr_grade('Python', best_student, poor_student))
    print(multi_avr_grade('Python', some_lecturer, new_lecturer))

if __name__ == "__main__":
  main()