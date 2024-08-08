def generate_digit_second():
    
    customer_gender = input("Въведи си пола ?")

    # ако той е мъжки - цифрата е 1
    if customer_gender == 'M':
        return 1

    # ако той е женски - цифрата е 3
    if customer_gender == 'F':
        return 3

    # ако потребителят не желае да посочи пол, то тогава ПОТРЕБИТЕЛЯ ВЪВЕДЖДА число в интервала от 1 до 9 включително, като съобразите факта, че числото не може да е, нито 1, нито 3.
    if customer_gender == 'N':

        while True:
            custom_number = int(input('Въведи число в интервал 1 - 9 без 1 и без 3'))

            if custom_number < 1 or custom_number > 9:
                print("Некоректен вход")
                continue

            if custom_number == 1:
                print("Некоректен вход")
                continue

            if custom_number == 3:
                print("Некоректен вход")
                continue

            return custom_number