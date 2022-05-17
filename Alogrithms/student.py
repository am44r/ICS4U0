class Student:
    def __init__(self, fight_rank, grade):
        self.fight_rank = fight_rank
        self.grade = grade

    def buyRank(self):
        self.fight_rank += 1
        return self.fight_rank

    def increaseGrade(self):
        self.grade += 1
        return self.grade
