from student import Student


class Classroom:

    # полета с ЧАСТНА видимост
    _classroom_name: int

    def set_classroom_name(self, name: int):
        self._classroom_name = name

    # public - публични полета
    __student_collection: list[Student]

    def __init__(self):
        self.__student_collection = []

    def read_student_grade(self, file_id):

        file_reference = open(file_id, "r")
        file_content = file_reference.read()
        line_collection = file_content.split("\n")

        # пускам цикъл по всеки един ред от този списък
        for line in line_collection:
            student_data_collection = line.split(",")
            student_name = student_data_collection.pop(0)
            self._add_student(Student(student_name, student_data_collection))
            # self.add_student(student_name, student_data_collection)

    def list_all_students(self):
        for student in self.__student_collection:
            print(f"{student.name} - {student.get_avg()}")

    def _add_student(self, student_obj: Student):
        self.__student_collection.append(student_obj)

    def add_student_by_name_and_grade(self, student_name: str, grade_collection):
        self._add_student(Student(student_name, grade_collection))

    def add_student_by_name(self, student_name: str):
        self._add_student(Student(student_name, []))

    def get_top_student(self) -> Student:

        top_student = self.__student_collection[0]

        for student in self.__student_collection:
            if student.get_grade() > top_student.get_grade():
                top_student = student

        return top_student

    def get_class_avg(self) -> int:

        class_avg_score = 0
        for student in self.__student_collection:
            class_avg_score += student.get_avg()

        return class_avg_score // len(self.__student_collection)

