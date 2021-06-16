
#Задание № 1. Наследование.
# Класс Mentor должен стать родительским классом 
# Реализовать наследование классов Lecturer и Reviewer 
# Имя, фамилия и список закрепленных курсов реализовать на уровне родительского класса Mentor

#Задание № 2. Атрибуты и взаимодействие классов.
# A. Класс Reviewer должен иметь метод который сможет выставлять оценки за домашние задание 
  # (создать\унаследовать метод который будет лезть в класс\обект класса  Student и записывать что-то в словарь student.grades =D )
# B. Класс Student должен иметь метод который сможет выставлять оценки за лекции
#(создать метод который будет лезть в класс\объект Lecturer и записывать от 1 до 10 числа в список 
#при условии что, объект Lecturer должен быть закреплен за тем курсом что и студент)

#Задание № 3. Полиморфизм и магические методы
# A. Перегрузите магический метод __str__ у всех классов.
# B. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

# Задание № 4. Полевые испытания
# A. Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, 
# B. А также реализуйте две функции:
#   B1. для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
#   B2. для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса (в качестве аргументов принимаем список лекторов и название курса).


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def rate_hw_for_lecturer(self, student, lector, lectors_course, lectors_grade):
        if isinstance(lector, Mentor) and lectors_course in lector.courses_attached and lectors_course in student.courses_in_progress:
            if lectors_course in lector.grades:
                lector.grades[lectors_course] += [lectors_grade]
            else:
                lector.grades[lectors_course] = [lectors_grade]
        else:
            return 'Ошибка'        

    def comparison2(self):
        sum_grades = 0
        for key, val in self.grades.items():
            for x3 in range(len(val)):
                for_division_x = len(val)
                sum_grades += self.grades[key][x3]
        average_grades = round((sum_grades / for_division_x), 2)

        sum_courses_progress = ''
        for list in self.courses_in_progress:
            sum_courses_progress += (list + ', ')   

        sum_finished_courses = ''
        for list in self.finished_courses:
            sum_finished_courses += (list + ', ')        
        return average_grades, sum_courses_progress.rstrip(" ,"), sum_finished_courses.rstrip(" ,")

    def __str__(self):
        average_grades, sum_courses_progress, sum_finished_courses = self.comparison2()
        
        return f'Student \nИмя: {self.name} \nФамилия: {self.surname} \
\nСредняя оценка за домашние задания: {average_grades} \
\nКурсы в процессе изучения: {sum_courses_progress} \
\nЗавершенные курсы: {sum_finished_courses}'
        

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Не тот класс для сравнения'
        return self.comparison2() < other.comparison2()  



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def comparison1(self):
        sum_grades = 0
        for key, val in self.grades.items():
            for x3 in range(len(val)):
                for_division_x = len(val)
                sum_grades += self.grades[key][x3]
        average_grades = round((sum_grades / for_division_x), 2)
        return average_grades
    
    def __str__(self):
        return f'Lecturer \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {self.comparison1()}' 

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не тот класс для сравнения'
        return self.comparison1() < other.comparison1()   


class Reviewer(Mentor): 
    def rate_hw_2(self, student, course, grade):
        self.rate_hw(student, course, grade)

    def __str__(self):
        return f'Reviewer \nИмя: {self.name} \nФамилия: {self.surname}'




#Задание 4 Функция подсчет среднего значения студентов 
def sum_students_grades(students_list, students_courses):

    for_division_list = 0
    sum_each_grades = 0

    for objeck in students_list:
        for key, val in objeck.grades.items():
            for_division_list += len(val)
            if key == students_courses:
                for list_val in range(len(val)):
                    sum_each_grades += objeck.grades[key][list_val]
            else:
                print(f'Ошибка у Cтудента {objeck.name} \
нет курса по {students_courses} есть только {objeck.courses_in_progress}')   

    average_grades = round((sum_each_grades / for_division_list), 2)                

    print(f'Сердняя оценка по всем студентам {average_grades} по курсу {students_courses}')



#Задание 4 Функция подсчет среднего значения лекторов
def sum_lecturer_grades(lecturer_list, lecturer_courses):

    for_division_list = 0
    sum_each_grades = 0

    for objeck in lecturer_list:
        for key, val in objeck.grades.items():
            for_division_list += len(val)
            if key == lecturer_courses:
                for list_val in range(len(val)):
                    sum_each_grades += objeck.grades[key][list_val]
            else:
                print(f'Ошибка у Лектора {objeck.name} \
нет курса по {lecturer_courses} есть только {objeck.courses_attached}')   

    average_grades = round((sum_each_grades / for_division_list), 2)                

    print(f'Сердняя оценка по всем Лекторам {average_grades} по курсу {lecturer_courses}')





#Создает объект студента
best_student3 = Student('Гиви', 'Минашвили', 'your_gender')
best_student3.courses_in_progress += ['GO', 'Git']
best_student3.finished_courses += ['Введение в программирование']

#Создает объект студента
best_student = Student('Денис', 'Красносваров', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

#Создает объект студента
best_student2 = Student('Георгий', 'Минашвили', 'your_gender')
best_student2.courses_in_progress += ['Python', 'Git']
best_student2.finished_courses += ['Введение в программирование']

#Создает объект Ментор и выставляет оценку студенту "best_student"
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

#Создает объект Ревьюрер(наследует Ментор) и выставяет оценку студенту "best_student" и студенту "best_student2" 
super_cool_reviewer = Reviewer('Мун', 'Андрей' )
super_cool_reviewer.courses_attached += ['Python', 'GO']                     
super_cool_reviewer.rate_hw_2(best_student, 'Python', 7)
super_cool_reviewer.rate_hw_2(best_student2, 'Python', 7)
super_cool_reviewer.rate_hw_2(best_student3, 'GO', 100)

#Создает объект Лектор(наследует Ментор) и получает оценки от студента "best_student" 
best_lector = Lecturer('Oleg', 'Buligin')
best_lector.courses_attached += ['Python']
best_student.rate_hw_for_lecturer(best_student, best_lector, 'Python', 5)
best_student.rate_hw_for_lecturer(best_student, best_lector, 'Python', 7)
best_student.rate_hw_for_lecturer(best_student, best_lector, 'Python', 10)

#Создает еще объект Лектор2(наследует Ментор) и получает оценки от студента "best_student" 
best_lector2 = Lecturer('Яна', 'Воля')
best_lector2.courses_attached += ['Python']
best_student.rate_hw_for_lecturer(best_student, best_lector2, 'Python', 10)
best_student.rate_hw_for_lecturer(best_student, best_lector2, 'Python', 10)
best_student.rate_hw_for_lecturer(best_student, best_lector2, 'Python', 10)


#Вывод решений по заданиям №1 №2 №3 
print()
print(super_cool_reviewer)
print()
print(best_lector)
print()
print(best_lector2)
print()
print(best_student) 
print()
print(best_student2)
print()
print(best_student3)
print()
print(f'Сравнивает среднюю оценку лектора- {best_lector2.name} и лектора- {best_lector.name}, \
получает true если {best_lector2.name} имеет оценку лучше: {best_lector2 > best_lector}')
print()
print(f'Сравнивает среднюю оценку студента- {best_student.name} и студента- {best_student2.name}, \
получает true если {best_student.name} имеет оценку лучше: {best_student > best_student2}')
print()
sum_students_grades([best_student, best_student2], 'Python')
sum_lecturer_grades([best_lector, best_lector2], 'Python')





