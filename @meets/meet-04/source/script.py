# ОПЕРАТОРИ ЗА СРАВНЕНИЕ
# РАВНО                 ==
# ПО ГОЛЯМО             >
# ПО МАЛКО              <
# ПО-ГОЛЯМО ИЛИ РАВНО   >=
# ПО-МАЛКО ИЛИ РАВНО    <=
# РАЗЛИЧНО              !=

customer_number = 55555

# 
is_customer_lagger = customer_number > 999999

# 
is_greather_or_equal_to_100000  = customer_number >= 100000 # True / False
is_lower_or_equal_to_999999     = customer_number <= 999999 # True / False
is_customer_normal              = (customer_number >= 100000) and (customer_number <= 999999)

# - да съм с число ПО-ГОЛЯМО от 99
# - да НЕ СЪМ от ТИП NORMAL
# - да НЕ СЪМ от ТИП LAGGER
# is_customer_early_adopter = (customer_number > 99) and (is_customer_normal == False) and (is_customer_lagger == False)
# early_adopter СЪМ КОГАТО (НОМЕРА МИ Е ПО ГОЛЯМ ОТ 99) и НЕ СЪМ (NORMAL) и НЕ СЪМ (LAGGER) 
is_customer_early_adopter = (customer_number > 99) and (not is_customer_normal) and (not is_customer_lagger)

# - ТИП SPECIAL
# + когато стойността на номера ти е 666
# + специалния потребител НЕ Е EARLY ADOPTER
is_customer_special      = (customer_number == 666) and (is_customer_early_adopter == False)
# is_customer_special      = (customer_number == 666) and (not is_customer_early_adopter)

# - ТИП SELECTED
# + той е EARLY ADOPTER
# + номера на картата му е в интервала 100 - 200
is_customer_selected    = is_customer_early_adopter and (customer_number >= 100 and customer_number <= 200)



# - ТИП NOT_SELECTED
# - тое е EARLY ADOPTER
# - И
# - номера на картата му не трябва да е 133 ИЛИ 233 ИЛИ 333
#  !=
is_customer_not_selected = is_customer_early_adopter and (customer_number != 133 or customer_number != 233 or customer_number != 333)

# - ТИП ULTIMATE
# - той е NORMAL
# - неговата карта е в интервала 555555 - 666666
# - неговата карта НЕ е с номер 555558 ИЛИ 555559
is_customer_ultimate = is_customer_normal and ( customer_number >= 555555 and customer_number <= 666666) and (customer_number != 555558 or customer_number != 555559)


print(is_customer_early_adopter)
print(is_customer_lagger)
print(is_customer_normal)

# ПОД ПРОГРАМА
if is_customer_early_adopter: # само ако е TRUE
    print("Потребителя е от тип EARLY_ADOPTER")

if is_customer_lagger: # само ако е TRUE
    print("Потребителя е от тип LAGGER")

if is_customer_normal: # само ако е TRUE
    print("Потребителя е от тип NORMAL")


# Задача 2 - проверка за VIP статус
is_customer_vip         = (customer_number % 2 == 0)
is_customer_super_vip   =  is_customer_early_adopter and is_customer_vip

# Ако потребителя е VIP
if is_customer_vip:
    print("Потребителя е VIP")

# Ако потребителя е EARLY ADOPTER 
# - да се изведе съобщение че си SUPER VIP
# if is_customer_super_vip:
#     print("Потребителя е SUPER VIP")


# Ако потребителя е EARLY ADOPTER 
    # И Е VIP - изведе съобщение SUPER VIP
    # в ПРОТИВЕН СЛУЧАЙ ИЗВЕДЕТЕ СЪОБЩЕНИЕ НЯМА СПЕЦИАЛНИ ПРАВА 

if is_customer_early_adopter and is_customer_vip:
    print("Потребителя е SUPER VIP")
else: # ИЗПЪЛНЯВА СЕ ВИНАГИ - Когато горната операция (в IF) не се изпълнява
    print("Няма специални права")


# Ако е NORMAL
# и НОМЕРА на картата му е 555555
#  --> изведете на екрана съобщение ти си специален ПОТРЕБИТЕЛ
# В противен случай 
# --> изведете на екрана съобщение - ГРЕШКА объркахме се
if is_customer_normal and customer_number == 555555:
    print("Ти си специален потребител")
else:
    print("Грешка")

if is_customer_normal:
    if customer_number == 555555:
        print("Ти си специален потребител")    
    else:
        print("Грешка")



# Ще модифицираме горните два варианта - така че да правим проверка само
# и единстнено когато потребителя ми е от определен тип.

# АКО СЪМ EARLY адоптър
# САМО ТОГАВА - прави проверка дали съм VIP и извеждаи подходящи съобщения
if is_customer_early_adopter:
    if is_customer_vip:
        print("Потребителя е SUPER VIP")
    else:
        print("Няма специални права")


print("Продължаваме работа си .....")
