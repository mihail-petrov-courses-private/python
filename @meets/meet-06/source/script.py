# Входните данни от системата
env_input = input("Въведи какво виждаш")

# Валидация на входните данни
# Дали обекта който виждам е правилния
# В момента разпознавам само три неща. 

# Ако входните данни не са ми коректни - изведи съобщение ГРЕШКА
is_input_valid = (
                    (env_input == "стена")  or 
                    (env_input == "стол")   or 
                    (env_input == "нищо")
                )

# Вариант на проверка 
# ИЗПОЛЗВАЩА ВЛОЖЕН IF / ELSE
# При този вариант - всеки IF се проверява индивидуално.
if is_input_valid:

    if env_input == "стена":
        print("Go sideway")

    if env_input == "стол":
        print("Jump")

    if env_input == "нищо":
        print("Forward")

else:
    print("ГРЕШКА")


# Как тези три IF -а да се държат като една последователност.
if env_input == "стена":
    print("Go sideway")

elif env_input == "стол":
    print("Jump")

elif env_input == "нищо":
    print("Forward")

else:
    print("Грешка")


# Пази броя на ударите които можем да направим 
max_number_of_hits = 4

while max_number_of_hits > 0:

    # 1. Въведете число от конзолата, 
    pixel_count         = input("Въведете брой на пикселите от околната среда")
    # 2.  конвертирайте го към цяло число, 
    pixel_number        = int(pixel_count)
    # 3.  разделете го модулно на 2 и провдерете дали остатъка е 0
    is_mouse_detected   = (pixel_number % 2) == 0

    # Същото с по-малко код
    # pixel_number        = int(input("Въведи число"))
    # is_mouse_detected   = pixel_number % 2 == 0

    # Същото с най-малко код
    # is_mouse_detected   = int(input()) % 2 == 0

    # Трябва ни променлива която да проверява дали батерията е заредена.
    # Батерията е заредена коягот броя на ударите е по голям от 0
    is_battery_full = max_number_of_hits > 0

    if is_mouse_detected and is_battery_full:
        print("Успешен удар")
        max_number_of_hits = max_number_of_hits - 1

