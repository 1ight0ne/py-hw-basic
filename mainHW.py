class Student:
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
            return 'Ошибка, оценка не доступна'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка, оценка не доступна'

def main():
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
 
    some_reviewer = Reviewer('Some', 'Buddy')
    some_reviewer.courses_attached += ['Python']
    
    some_lecturer = Lecturer('John', 'Smith')
    some_lecturer.courses_attached += ['Python']

    best_student.rate_lecture(some_lecturer, 'Python', 10) 
    best_student.rate_lecture(some_lecturer, 'Python', 9)

    some_reviewer.rate_hw(best_student, 'Python', 10)
    some_reviewer.rate_hw(best_student, 'Python', 10)
    some_reviewer.rate_hw(best_student, 'Python', 10)

    print(f'Оценки студента {best_student.name} {best_student.surname} за курс Python {best_student.grades["Python"]}')
    print(f'Оценки лектора {some_lecturer.name} {some_lecturer.surname} за курс Python {some_lecturer.grades["Python"]}')

if __name__ == "__main__":
  main()