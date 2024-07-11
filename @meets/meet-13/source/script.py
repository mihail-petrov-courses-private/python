# Да си декларираме променливи които ще пазят информация
# за горивото и кислорода. 168 / 90
OXIGEN_INDEX  = 168
FUEL_INDEX    = 90

IS_SYSTEM_ON  = False
IS_MISSION_ON = True

# Текущата ръка която местим
ACTIVE_HAND_ID = 'A'

# Координатите на всяка една от ръцете
aX = 1
aY = 1

bX = 1
bY = 1

cX = 1
cY = 1

dX = 1
dY = 1

# Задача 1. Да направим функция, извикването на която - ще ни създаде
# условия да работи с програмата от тук на сетне.
def turnon():

    global IS_SYSTEM_ON
    IS_SYSTEM_ON = True
    print("Системата е стартирана")

# Задача 2. Ако системата не е включена - тогава изведи съобщение за грешка
# Задача 3. Да си създадем място където да пазим коориданите за X и Y на роботска ръка A
# при извикване на функцията move трябва да променяме координатите със стойностите 
# x и y на функцията move
def move(x, y):

    global aX
    global aY
    global bX
    global bY
    global cX
    global cY

    # if IS_SYSTEM_ON == False:
    if not IS_SYSTEM_ON:
        return print("Системата не е включена")
    
    if ACTIVE_HAND_ID == 'A':
        aX = x
        aY = y
    
    if ACTIVE_HAND_ID == 'B':
        bX = x
        bY = y

    if ACTIVE_HAND_ID == 'C':
        cX = x
        cY = y

    spend_resource("OXIGEN", 5)
    print(f"Системата мести на {x} и {y} координати")


# Задача 4 - да дефинираме една нова функция, която ще зарежда активната РЪКА - A / B / C. - след като заредим
# активната ръка - трябва функция move да променя координатите само на активната ръка.
# - трябвна да си дефинираме координатите за всички ръце
# - трябва да пазим активната ръка в момента 

def load(active_hand_id):

    if not IS_SYSTEM_ON:
        return print("Системата не е включена")

    global ACTIVE_HAND_ID
    ACTIVE_HAND_ID = active_hand_id
    spend_resource(resource_id = "FUEL", step = 5)
    # spend_resource("FUEL", 5)
    # spend_resource("FUEL")
    print(f"Ръка {active_hand_id} е активирана успешно")

# Задача 5 - да се дефинира функция която да проверява дали има достатъчно РЕСУРСИ за да работи роботската ръка
def is_program_runing():
    return (OXIGEN_INDEX > 0 and FUEL_INDEX > 0) or IS_MISSION_ON


# Задача 6 - да се създаде / дефинира функция spend_resource която да изхарчва, предварително дефинирана стойност
# за ГОРИВО и КИСЛОРОД - условно казано 5 единици, в зависимост от аргумента, който и подадем
# spend_resource("OXIGEN")
# spend_resource("FUEL")

# Задача 6.1
# Да направим втори аргумент step с които да намаляваме количеството на ресурса, 
# с някаква определена от нас стъпка

def spend_resource(resource_id, step = 5):

    global FUEL_INDEX
    global OXIGEN_INDEX

    if resource_id == "OXIGEN":        
        OXIGEN_INDEX -= step

    if resource_id == "FUEL":
        FUEL_INDEX -= step


# Задача 7. Напишете функция, която ПРИНТИРА наличните ресурси
# print_resource_status()

def print_resource_status():
    print(f"КИСЛОРОД -> {OXIGEN_INDEX}")
    print(f"ГОРИВО   -> {FUEL_INDEX}")


# Задача 8. Да се направи основен цикъл, който да е активен докато системата има ресурси. Системата подканя потребителя да въведе команда - която трябвна да се изпълни. Командата се въвежда като ТЕКСТ, въведената команда се изпълнява веднага след нейното въвеждане. 
# Внимание. Някой команди имат нужда от аргументи. 

# Да се дефинират две нови функции:
# -> turnoff -> изключва озонобъркачката, но ЦИКЪЛА продължава да работи
def turnoff():
    global IS_SYSTEM_ON
    IS_SYSTEM_ON = False
    print("Системата е изключена")

# -> landoff -> спира изпълнението на цялата програма
def landoff():
    global IS_MISSION_ON
    IS_MISSION_ON = False

while is_program_runing():
    process_command = input("Въведи команда:")

    if process_command == "turnon":
        turnon()

    if process_command == "turnoff":
        turnoff()        

    if process_command == "landoff":
        landoff()
    
    if process_command == "load":

        hand_id = input("Въведи id на активната ръка")
        load(hand_id)
    
    if process_command == "move":

        position_x = int(input("Въведи позиция X"))
        position_y = int(input("Въведи позиция Y"))
        move(position_x, position_y)

    if process_command == "status":
        print_resource_status()


print("Мисията свърши")
