# Задача 1
# Напишете функция която изписва съобщение завивам наляво
def turn_left():
    print("завиввам на ляво")

# Задача 2
# Напишете функция която изписва съобщение завивам надясно
def turn_right():
    print("завивам на дясно")

# Напишете функция, която получава като АРГУМЕНТ 1 или 2
#  -> ако е 1 извиква функцията turn_left
#  -> ако е 2 извиква функция turn_right
#  -> във всички останали случай - извежда съобщение - грешна команда
def turn(direction):
    
    if direction == 1:
        turn_left()
    elif direction == 2:
        turn_right()    
    else:
        print("Грешна команда")

# Напишете функция, която получава един аргумент число и ВРЪЩА неговата стойност 
# в текстов вид на англиски език - ПРИМЕР translate(1) -> "one" - до 10 
# Всички стойности точно или над 10 да връща стойност "NA"

def translate(numberId):

    # с помоща на return - ключовата дума - ние спираме 
    # изпълнението на функцията - и връщаме на МЯСТОТО в което сме извикали ФУНКЦИЯТА
    # стойността след RETURN.

    # Функции които връщат стойноист, се ползват само в контекста на 
    # ооператор за присвояване

    # RETURN е като BREAK но за функции

    if numberId == 1:
        return "one"
    
    if numberId == 2:
        return "two"
    
    return "NA"
    
# Така извикана функцията е БЕЗ СМИСЪЛ
translate(1)

# Логично е да я викмен по този начин
id = translate(1)

# Задача 3.
# Напишете функция, която изписва съобщение включвам на {N} та скорост, като максималното количество скоростти е 5. 
# Ако се опитаме да включим на по висока скорост ще получим съобщение за грешка

def shit_gear(gear_number):
    
    if gear_number>= 1 and gear_number <= 5:
        print(f"включвам на {gear_number} та скорост")
    else:
        print("Невалидна скорост")


def shit_gear(gear_number):
    
    if gear_number>= 1 and gear_number <= 5:
        return f"включвам на {gear_number} та скорост"

    return "Невалидна скорост"


# Задача 4.
# Напишете функция, която проверява дали двигателя може да запали. 
# За целтя е необходимо да му се подаде сигнал които е четно число. 
# Сигнала се подава като променлива или като литерал. Функцията връща True или False

def start_engine(signal_id):

    # Вариант 1
    # is_even = signal_id % 2 == 0
    # return is_even

    # Варниат 2
    # if signal_id % 2 == 0:
    #     return True
    
    # return False

    # Варниат 3
    return signal_id % 2 == 0


# print(start_engine(1))
# print(start_engine(2))

signal_id = input('Въведете сигнал')
if start_engine(int(signal_id)):
    print("Колата пали")

# Напишете функция която прима като АРГУМЕНТИ три числа
# - Първото число винаги е 1 или 0
# Функцията трябва да върне конкатенирата стойност на двете числа разделени с:
# __ - ако първото число е 1
# @@ - ако първото число е 0
def cypher(mask_id, first_number, second_number):
    
    if mask_id == 1:
        return f"{first_number}__{second_number}"
    elif mask_id == 0:
        return f"{first_number}@@{second_number}"
    
    return ""


# Задача 5.
# Напишете функция, която проверява дали системата за запалване е изправна. Функцията приема две числа. Ако сбора на тези числа е по голям от 15, колата пали в противен случай не може.
def is_electric_system_working(a, b):
    return a + b > 15

is_electric_system_working(10, 25)


# Задача 6
# Напишете функция която изпраща стойност, която показва състоянието за изправността на спирачките. 
# 
# Системата приема две числа и специален текст. Текста може да бъде една от две стойности:

# BRAKE_SOFT
# BRAKE_HARD
# АКо системата получи аргумент BRAKE_SOFT винаги се връща стойност -1. Ако системата получи BRAKE_HARD се връща едно от следните числа:

# Ако произведението на числата е положително число връщаме 1
# Ако произведението на числата е отрицателно число връщаме 0
# Ако се подаде текст с различна стойност от посочениет, върнете текст "NoN"

def is_break_system_working(first_input, second_input, text_id):

    if text_id == "BRAKE_SOFT":
        return -1
    
    # if text_id == "BRAKE_HARD":
    #     if first_input * second_input > 0:
    #         return 1
    #     if first_input * second_input < 0:
    #         return 0
    
    if text_id == "BREAK_HARD" and (first_input * second_input > 0):
        return 1
    
    if text_id == "BREAK_HARD" and (first_input * second_input < 1):
        return 0

    return "NoN"
        

print(is_break_system_working(1,1,"BRAKE_SOFT"))
print(is_break_system_working(1,1,"BREAK_HARD"))
print(is_break_system_working(1,-1,"BREAK_HARD"))
print(is_break_system_working(1,-1,"JUST_BREAK"))