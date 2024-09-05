# импортиране на целия пакет
# import object_overview

# импортиране на целия пакет и преиментуването му (АЛИАС)
# import object_overview as oo

# импортиране на ЕДИН единствен обект
from object_overview import Employ


file = open("./test.csv", "r")
content = file.read()

line_collection = content.split("\n")

# Премахва ХЕДЪРА НА ФАЙЛА
schedule_header = line_collection.pop(0)
schedule_map = {}

employ_collection = []

def transform_shift_data(shift_collection):

    shift_word_collection = []

    for element in shift_collection:
        if element == '1':
            shift_word_collection.append('първа')
            continue
        if element == '2':
            shift_word_collection.append('втора')
            continue

        shift_word_collection.append('грешка')

    return shift_word_collection

for line in line_collection:
    data_collection = line.split(",")

    # Мога да врътна масив и да взема първия елемент на всеки един от
    # съществуващите масиви
    map_key = data_collection.pop(0)
    schedule_map[map_key] = transform_shift_data(data_collection)

    # ще направя тип данни за всеки един служител, който имам
    employ = Employ()
    employ.first_name = map_key
    employ.work_schedule = transform_shift_data(data_collection)
    employ_collection.append(employ)

    # Искаме в писава да пише първа и втора

print(schedule_map)


# Задачка закачка:
# Да се направи РЕЧНИК - в който ключът да бъде
# името на служителя а стойността да бъде
# МАСИВ от сменитене, НО всяка смяна трябва да бъде
# записана със своето име вместо номер

# "Теодора" => ["първа", "първа", "втора"]
# "Галин"   => ["първа", "първа", "втора"]

# "Понеделник" => [{"първа"} => ["Галин", "Теодора"] ]
