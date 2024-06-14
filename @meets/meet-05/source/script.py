customer_account_balance = 0

# Задача 1
# Когато влезете в системата ще трябва да въведете:

# слоя клиентски номер - число в интервала от 50 до 300
# абонаментния пакет които сте избрали (показан в таблица абонаментни пакети)
# вашата възраст

customer_number = int(input("Въведете вашия клиентски номер"))

# ДОПЪЛНИТЕЛНА ПРОВЕРКА
is_customer_number_valid = (customer_number >= 50 and customer_number <= 300)
if not is_customer_number_valid:
    print("Клиентския номер е не валиден")
    exit()

if customer_number < 50 or customer_number > 300:
    print("Клиентския номер е не валиден")

if not (customer_number >= 50 and customer_number <= 300):
    print("Клиентския номер е не валиден")



customer_plan   = input("Въведете вашия предпочитан план")

# ДОПЪЛНИТЕЛНА ПРОВЕРКА
is_customer_plan_valid = (
                            (customer_plan == 'ENTRY'   )   or 
                            (customer_plan == 'PREMIUM' )   or 
                            (customer_plan == 'ULTRA'   )   or 
                            (customer_plan == 'NO'      )
                          )

if not is_customer_plan_valid:
    print("Абонаментния план НЕ Е валиден")
    exit()

customer_age    = int(input("Въведете вашата възраст"))

# ДОПЪЛНИТЕЛНА ПРОВЕРКА

if customer_age > 100:
    print("Невалидна възраст")
    exit()


# Задача 2

# За да ползвате услугата Телетекст е необходимо:

# да сте потребител с клиентски номер завършващ на четно число
# да сте си купили абонаментен план ENTRY
# да сте на 65 или повече години
is_teleteks_available = (
                            (customer_number % 2 == 0   ) and 
                            (customer_plan == 'ENTRY'   ) and
                            (customer_age >= 65         )
                        )

# За да ползвате услугата Канали за възрастни е необходимо:

# да сте във възрастовия интервал 18 - 55
# да сте си купили обонаментен план PREMIUM или ULTRA

is_adoult_chanel_available =    (
                                    (
                                        customer_age >= 18 and 
                                        customer_age <= 55
                                    )  and 
                                    (
                                        customer_plan == 'PREMIUM' or 
                                        customer_plan == 'ULTRA'
                                    )
                                )

# За да ползвате услугата Футболни мачове е необходимо:

# да нямате закупен абонаментен план
# да сте точно на 36 години
# номера ви да е 100 или 200 или 300

is_footbal_available =  (
                            (customer_plan == 'NO'  ) and
                            (customer_age == 36     ) and 
                            ( 
                                customer_number == 100  or 
                                customer_number == 200  or 
                                customer_number == 300
                            )
                        )

# За да ползвате услугата Анимационни канали е необходимо:

# да сте под или точно на 18 години
# номера ви да е под 100
# да имате закупен пакет ULTRA
is_animation_chanel_available = (
                                    (customer_age <= 18         ) and
                                    (customer_number < 100      ) and
                                    (customer_plan == 'ULTRA'   )
                                )

# Задача 3.1
# Искаме да се извеждат Ващите услуги са: само ако има минимум една услуга

has_service =   (
                    is_teleteks_available           or 
                    is_adoult_chanel_available      or 
                    is_footbal_available            or 
                    is_animation_chanel_available
                )

if has_service:
    print("Ващите услуги са:")
    if is_teleteks_available:
        if customer_age == 70:
            print("ПРЕМИУМ телетекст")
        else:
            print("- телетекст")

    if is_adoult_chanel_available:
        if customer_plan == 'ULTRA':
            print('УЛТРА канали за възрастни')
        else:
            print("- канали за възрастни")

    if is_footbal_available:
        if customer_number == 200 or customer_number == 30:
            print("МЕГА футбол")
        else:
            print("- футболни канали")

    if is_animation_chanel_available:
        if customer_age == 18:
            print("ти не си ли много голям бе")
        else:
            print("- анимационни канали")
else:
    print("Няма услуги")


