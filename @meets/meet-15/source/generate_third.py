import profile

def generate():

    if profile.is_adoult():
        return 0
    
    # да решаваме задача
    mother_date = int(input("Кога е родена майка ти ?"))
    father_date = int(input("Кога е роден баща ти ?"))

    # Ако последната цифра на годината на майка му е равна на тази на баща му, то третата цифра от номера на клиентската карта е равна на предпоследната цифра от годината на майка му.
    mother_date_last_digit = (mother_date % 10)
    father_date_last_digit = (father_date % 10)

    if mother_date_last_digit == father_date_last_digit:
        # 1965 -> 65 -> 6.5
        return int((mother_date % 100) / 10)

    #  Ако двете цифри са различни, то третата цифра от номера на картата е равна на последната цифра от годината на баща му.
    return father_date_last_digit
