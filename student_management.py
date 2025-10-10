class Person:
    name = ""
    id = 0

    def __init__(self, name , id):
        self._name = name
        self.id = id

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

class Student(Person):
    def __init__(self , id: int, name:str , age):
        super().__init__(id , name)
        self.age = age
        self.enrolled_courses = set()
        self.grades = {}



class Courses:
    def __init__(self ,id , name):
        self.id = id
        self.name = name
        self.enrolled_students = set()

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_students(self , student: Student):
        self.students[student.id] = student

    def remove_student(self , student: Student):
        self.students.pop(student.id, None)

    def add_courses(self , course: Courses):
        self.courses[course.id] = course

    def remove_courses(self , course: Courses):
        self.courses.pop(course.id, None)