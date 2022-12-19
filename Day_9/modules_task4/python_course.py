from course import Course


class PythonCourse(Course):
    def __init__(self, name, lector, time):
        self.name = name
        self.lector = lector
        self.time = time


    def teach(self):
        print("Vyksta programavimas!")