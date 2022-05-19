class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def displayName(self):
        return self.name

    def increaseGrade(self):
        self.grade += 1
        return self.grade
