# Да си декларираме променливи които ще пазят информация
# за горивото и кислорода. 168 / 90
OXIGEN_INDEX  = 168
FUEL_INDEX    = 90

IS_SYSTEM_ON  = False

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

    print(f"Системата мести на {x} и {y} координати")


# Задача 4 - да дефинираме една нова функция, която ще зарежда активната РЪКА - A / B / C. - след като заредим
# активната ръка - трябва функция move да променя координатите само на активната ръка.
# - трябвна да си дефинираме координатите за всички ръце
# - трябва да пазим активната ръка в момента 

def load(active_hand_id):

    global ACTIVE_HAND_ID
    ACTIVE_HAND_ID = active_hand_id


turnon()
load("A")
move(5,6)
load("B")
move(10, 10)