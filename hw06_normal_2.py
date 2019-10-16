__author__ = "Гончаров Всеволод Сергеевич"

import os


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def short_name(self):
        return "{} {}.{}.".format(self.surname, self.name[:1], self.patronymic[:1])


class Student(Human):
    def __init__(self, surname, name, patronymic, father, mother):
        Human.__init__(self, surname, name, patronymic)
        self.father = father
        self.mother = mother

    def __str__(self):
        return self.short_name()


class Parent(Human):

    def __init__(self, surname, name, patronymic):
        Human.__init__(self, surname, name, patronymic)
        self.children = []

    def __str__(self):
        return self.short_name()


class Teacher(Human):
    def __init__(self, surname, name, patronymic):
        Human.__init__(self, surname, name, patronymic)

    def __str__(self):
        return self.short_name()


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __str__(self):
        return self.name


class Room:
    def __init__(self, grade, idx, Students, Lessons):
        self.grade = grade
        self.idx = idx
        self.students = Students
        self.lessons = Lessons

    def __str__(self):
        return self.grade + self.idx


def create_parents_data():
    parent = Parent("Злоустов", "Алексей", "Иванович")
    parents.append(parent)
    parent = Parent("Злоустова", "Лили", "Петровна")
    parents.append(parent)
    parent = Parent("Петросян", "Артур", "Семёнович")
    parents.append(parent)
    parent = Parent("Петросян", "Молли", "Альфредовна")
    parents.append(parent)
    parent = Parent("Паркинсон", "Фёдор", "Иванович")
    parents.append(parent)
    parent = Parent("Паркинсон", "Алла", "Петровна")
    parents.append(parent)
    parent = Parent("Свистополов", "Алексей", "Степанович")
    parents.append(parent)
    parent = Parent("Свистополова", "Марфа", "Петровна")
    parents.append(parent)
    parent = Parent("Градусников", "Август", "Злодеевич")
    parents.append(parent)
    parent = Parent("Градусникова", "Агнесса", "Невкупаевна")
    parents.append(parent)
    parent = Parent("Чикистов", "Василий", "Галопередолович")
    parents.append(parent)
    parent = Parent("Чикистова", "Анжелика", "Анжеловна")
    parents.append(parent)
    parent = Parent("Котик", "Василий", "Васильевич")
    parents.append(parent)
    parent = Parent("Котик", "Алиса", "Олеговна")
    parents.append(parent)


def create_rooms_data():
    room = Room("5", "А", [students[0], students[1], students[2], students[9]], [subjects[0], subjects[1], subjects[3]])
    rooms.append(room)
    room = Room("5", "Б", [students[5], students[6], students[7]], [subjects[0], subjects[1], subjects[4]])
    rooms.append(room)
    room = Room("6", "Ё", [students[3], students[4], students[8]], [subjects[0], subjects[1], subjects[2], subjects[3],
                                                                    subjects[4]])
    rooms.append(room)


def create_students_data():
    student = Student("Злоустов", "Благодей", "Алексеевич", parents[0], parents[1])
    students.append(student)
    parents[0].children.append(student)
    parents[1].children.append(student)
    student = Student("Петросян", "Олег", "Артурович", parents[2], parents[3])
    students.append(student)
    parents[2].children.append(student)
    parents[3].children.append(student)
    student = Student("Петросян", "Пробег", "Артурович", parents[2], parents[3])
    students.append(student)
    parents[2].children.append(student)
    parents[3].children.append(student)
    student = Student("Петросян", "Глаша", "Артуровна", parents[2], parents[3])
    students.append(student)
    parents[2].children.append(student)
    parents[3].children.append(student)
    student = Student("Паркинсон", "Мария", "Алловна", parents[4], parents[5])
    students.append(student)
    parents[4].children.append(student)
    parents[5].children.append(student)
    student = Student("Свистополова", "Оксана", "Алексеевна", parents[6], parents[7])
    students.append(student)
    parents[6].children.append(student)
    parents[7].children.append(student)
    student = Student("Градусников", "Максим", "Августович", parents[8], parents[9])
    students.append(student)
    parents[8].children.append(student)
    parents[9].children.append(student)
    student = Student("Чикистов", "Пётр", "Васильевич", parents[10], parents[11])
    students.append(student)
    parents[10].children.append(student)
    parents[11].children.append(student)
    student = Student("Чикистова", "Пега", "Васильевна", parents[10], parents[11])
    students.append(student)
    parents[10].children.append(student)
    parents[11].children.append(student)
    student = Student("Котик", "Барсик", "Васильевич", parents[12], parents[13])
    students.append(student)
    parents[12].children.append(student)
    parents[13].children.append(student)


def create_subjects_data():
    subject = Subject("Математика", teachers[0])
    subjects.append(subject)
    subject = Subject("Русский язык", teachers[1])
    subjects.append(subject)
    subject = Subject("Зельеварение", teachers[2])
    subjects.append(subject)
    subject = Subject("Физкультура", teachers[3])
    subjects.append(subject)
    subject = Subject("Труды", teachers[4])
    subjects.append(subject)


def create_teachers_data():
    teacher = Teacher("Говов", "Иван", "Иванович")
    teachers.append(teacher)
    teacher = Teacher("Меняйло", "Арсений", "Арсеньевич")
    teachers.append(teacher)
    teacher = Teacher("Рофловна", "Мария", "Степановна")
    teachers.append(teacher)
    teacher = Teacher("Физкультурников", "Физрук", "Петрович")
    teachers.append(teacher)
    teacher = Teacher("Бухлов", "Андрей", "Андреевич")
    teachers.append(teacher)


parents = []
students = []
teachers = []
subjects = []
rooms = []


def main():
    create_parents_data()
    create_teachers_data()
    create_subjects_data()
    create_students_data()
    create_rooms_data()
    while True:

        print("1.Вывести список всех классов школы\n2.Получить список всех учеников в классе\n"
              "3.Получить список всех предметов указанного ученика\n4.Узнать ФИО родителей указанного ученика\n"
              "5.Получить список всех Учителей, преподающих в указанном классе\n0.Выход")
        key = int(input())

        if key == 1:  # Вывести список всех классов школы

            for item in rooms:
                print(item)

        elif key == 2:  # Получить список всех учеников в классе

            for idx, item in enumerate(rooms, start=1):
                print("{}.{}".format(idx, item))
            print("Выбери порядковый номер класса")
            try:
                for item in rooms[int(input()) - 1].students:
                    print(item)
            except IndexError:
                print("Некорректный ввод")

        elif key == 3:  # Получить список всех предметов указанного ученика

            for idx, item in enumerate(students, start=1):
                print("{}.{}".format(idx, item))
            print("Выбери порядковый номер ученика")
            try:
                student_idx = int(input()) - 1
                student_room = None
                for room in rooms:
                    if students[student_idx] in room.students:
                        student_room = room
                        break
                for lesson in student_room.lessons:
                    print(lesson)
            except IndexError:
                print("Некорректный ввод")

        elif key == 4:  # Узнать ФИО родителей указанного ученика

            for idx, item in enumerate(students, start=1):
                print("{}.{}".format(idx, item))
            print("Выбери порядковый номер ученика")
            try:
                student_idx = int(input()) - 1
                print("Отец: {}\nМать: {}".format(students[student_idx].father, students[student_idx].mother))
            except IndexError:
                print("Некорректный ввод")

        elif key == 5:  # Получить список всех Учителей, преподающих в указанном классе

            for idx, item in enumerate(rooms, start=1):
                print("{}.{}".format(idx, item))
            print("Выбери порядковый номер класса")
            try:
                for lesson in rooms[int(input()) - 1].lessons:
                    print(lesson.teacher)
            except IndexError:
                print("Некорректный ввод")

        elif key == 0:  # Выход
            pass
        else:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()
