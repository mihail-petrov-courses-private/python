from classroom import Classroom
from student import Student

mainClassroom = Classroom("A1")
mainClassroom.read_student_grade("a1_student_grade.csv")

mainClassroom.add_student_by_name_and_grade("Maria", [1, 2, 3, 4, 5])

mainClassroom.list_all_students()

# Да си припомните обяснението за връщаните обекти.
print(mainClassroom.get_top_student().name)
print(mainClassroom.get_class_avg())


# Направете нов клас School
# - полетата му са : ИМЕ + СПИСЪК ОТ КЛАСНИ СТАИ
# - един метод, който листва всички класни стаии - техните имена.

# Направете модификация на класа Classroom така че да изисква задължително име на
# класна стая, при създаването й.