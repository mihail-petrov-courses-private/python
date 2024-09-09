from student import Student


class Classroom:
    student_collection: list[Student]

    def __init__(self):
        self.student_collection = []

    def read_student_grade(self, file_id):

        file_reference = open(file_id, "r")
        file_content = file_reference.read()
        line_collection = file_content.split("\n")

        # пускам цикъл по всеки един ред от този списък
        for line in line_collection:
            student_data_collection = line.split(",")
            student_name = student_data_collection.pop(0)
            self.student_collection.append(
                Student(student_name, student_data_collection)
            )

    def list_all_students(self):
        for student in self.student_collection:
            print(f"{student.name} - {student.get_avg()}")