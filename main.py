#Класс "Студенты", параметры: имя, фамилия, пол, пройденные курсы, курсы в изучении, оценка.
class Student:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()

#Реализуем возможность выставления оценки лектору студентом, если это лектор ведет лекции по данному курсу у этого студента
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f" Имя: {self.name}\n Фамилия: {self.surname}\n  Средняя оценка за домашние задания:{self.average_grades}\n  Курсы в процессе изучения:{courses_in_progress_string}\n  Завершенные курсы:{finished_courses_string}"
        return res

    def __lt__(self, other):
    # Реализует сравнение через операторы студентов между собой по средней оценке за домашние задания
        if not isinstance(other, Student):
            print('Такое сравнение неверное')
            return
        return self.average_grades < other.average_grades


#Класс "Преподаватели", параметры: имя, фамилия, курсы какие преподают.
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Класс "Лектор", параметры: имя, фамилия, Оценка студентов за начитанные лекции.
class Lecturer(Mentor):
    def __init__ (self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_grades = sum(map(sum, self.grades.values())) / grades_count
        res = f" Имя: {self.name}\n Фамилия: {self.surname}\n  Средняя оценка за лекции:{self.average_grades}"
        return res

    def __lt__(self, other):
    # Реализует сравнение через операторы лекторов между собой по средней оценке за домашние задания
        if not isinstance(other, Lecturer):
            print('Такое сравнение неверное')
            return
        return self.average_grades < other.average_grades

#Класс "Эксперты, проверяющие домашние задания", параметры:
class Reviewer(Mentor):
    def __init__ (self, name,surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f" Имя: {self.name}\n Фамилия: {self.surname}"
        return res

# Создаем лекторов и закрепляем их за каждым курсом
lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Sergey', 'Sergeev')
lecturer_3.courses_attached += ['Python']

# Создаем Reviewer и закрепляем их за курсом
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Ruoy', 'Eman')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Denis', 'Ivanov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Petrov')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Maxim', 'Maximov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам за проведенные лекции
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)

student_1.rate_lecturer(lecturer_2, 'Python', 6)
student_1.rate_lecturer(lecturer_2, 'Python', 5)
student_1.rate_lecturer(lecturer_2, 'Python', 8)

student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 9)

student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 9)

student_3.rate_lecturer(lecturer_3, 'Python', 6)
student_3.rate_lecturer(lecturer_3, 'Python', 7)
student_3.rate_lecturer(lecturer_3, 'Python', 8)

# Выставляем оценки студентам за ДЗ
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)

reviewer_2.rate_hw(student_3, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 6)
reviewer_2.rate_hw(student_3, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 8)
reviewer_2.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_3, 'Python', 9)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()

# Создаем список студентов
student_list = [student_1, student_2, student_3]

# Создаем список лекторов
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

# Создаем функцию для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса  в качестве аргументов принимает список студентов и название курса

def student_rating(student_list, course_name):
# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса в качестве аргументов принимает список студентов и название курса"""

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_grades
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Создаем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса в качестве аргумента принимает список лекторов и название курса

def lecturer_rating(lecturer_list, course_name):
# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса в качестве аргумента принимает список лекторов и название курса

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_grades
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
