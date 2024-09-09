class Student:
    name: str
    grade_collection: list[int]

    def __init__(self, student_name, grade_collection):
        self.name = student_name
        self.grade_collection = grade_collection

    def get_avg(self):

        grade_sum = 0
        for grade in self.grade_collection:
            grade_sum += int(grade)

        return grade_sum // len(self.grade_collection)