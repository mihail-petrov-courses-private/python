class Student:
    name: str
    grade_collection: list[int]

    def __init__(self, student_name: str, grade_collection):
        self.name = student_name
        self.grade_collection = grade_collection

    def get_grade(self):

        grade_sum = 0
        for grade in self.grade_collection:
            grade_sum += int(grade)

        return grade_sum

    def get_avg(self):
        return self.get_grade() // len(self.grade_collection)