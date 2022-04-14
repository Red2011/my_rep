"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    def __init__(self, text):
        self.text = text


class Homework:
    def __init__(self, text, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    # return true if our date is earlier than the job creation date + the number of days to complete
    def is_active(self) -> bool:
        return datetime.datetime.now() < self.created + self.deadline


class Naming:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Naming):

    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError('You are late')


class HomeworkResult:
    def __init__(self, author: Student, homework, solution: str):
        if not isinstance(homework, Homework):
            # returned error of Type: need object of class
            raise TypeError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Teacher(Naming):
    homework_done = defaultdict(lambda: [])

    @staticmethod
    def create_homework(text, deadline) -> Homework:
        return Homework(text, datetime.timedelta(deadline))

    @staticmethod
    def check_homework(result: HomeworkResult):
        if len(result.solution) < 5:
            return False
        else:
            # result.homework: this is key, which contains the task
            # result.solution: result - value equal to the HomeworkResult text
            Teacher.homework_done[result.homework] = result.solution
            return True

    @staticmethod
    def reset_results(something: Homework = None):
        if something is not None:
            Teacher.homework_done[something.text].clear()
        else:
            Teacher.homework_done.clear()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    print(Teacher.homework_done[docs_hw])
    Teacher.reset_results()
    print(Teacher.homework_done[oop_hw])
