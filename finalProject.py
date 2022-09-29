import random

class Course:


    def __init__(self,course_name,course_class, course_number = None):
        if course_number is not None:
            self.course_number = course_number
        else:
            self.course_number = random.randrange(100,999)
        self.course_name = course_name
        self.course_class = course_class

class Student:

    def __init__(self, student_name, student_class, student_number=None):
        if student_number is not None:
            self.student_number = student_number
        else:
            self.student_number = random.randrange(1000, 9999)
        self.student_name = student_name
        self.student_class = student_class
