# Вградени типове
file_count = 10

file_name = "string"

is_visible = True

file_collection = []


# Потребителски дефинирани типове
# ще си направим наш собствен тип данни
# с който ще моделираме информация за
# даден служител на нашата фирма
# -> име
# -> длъжност
# -> отдел
# -> в каква смяна работи

# -> като пакет - в който имаме
# данни и функции, които работят с тия данни
class Employ:
    first_name = ""
    last_name = ""
    occupation = ""
    department = ""

    work_schedule = []

    def full_name(self):
        return self.first_name + " " + self.last_name

# ПОТРЕБИТЕЛСКИ ДЕФИНИРАН ТИП
my_employ_tedy = Employ()
my_employ_tedy.first_name = "Теодора"
my_employ_tedy.last_name = "Копаранова"

# my_employ_galin = Employ()
# my_employ_galin.name = "Галин"
#

