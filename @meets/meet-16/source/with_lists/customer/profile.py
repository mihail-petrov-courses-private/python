CUSTOMER_BIRTH_YEAR = -1
CUSTOMER_BMI = -1 

PREFERED_PRODUCT_CATEGORY = -1

# Вариант на същия код със списък
# Първо създаваме списък БЕЗ елементи
card_number_collection = []

def add_next_card_digit(value):
    card_number_collection.append(value)

def get_number_on_position(position):
    return card_number_collection[position - 1]


def sum_card_digits_so_far():

    sum = 0
    for card_digit_element in card_number_collection:
        sum += card_digit_element
    return sum
        


def set_customer_birth_date(year):
    global CUSTOMER_BIRTH_YEAR
    CUSTOMER_BIRTH_YEAR = year

def get_customer_age():
    return 2024 - CUSTOMER_BIRTH_YEAR

def is_adoult():
    return get_customer_age() >= 18

def is_minor():
    return not is_adoult()

def set_bmi(value):
    global CUSTOMER_BMI
    CUSTOMER_BMI = value

def get_bmi():
    return CUSTOMER_BMI

def is_customer_overweight():
    return get_bmi() >= 6 and get_bmi() <= 8


def set_prefered_product_category(value):
    global PREFERED_PRODUCT_CATEGORY
    PREFERED_PRODUCT_CATEGORY = value

def get_prefered_product_category():
    return PREFERED_PRODUCT_CATEGORY

def set_prefered_product_frequancy(value):
    global PREFERED_PRODUCT_FREQUANCY
    PREFERED_PRODUCT_FREQUANCY = value

def get_prefered_product_frequancy():
    return PREFERED_PRODUCT_FREQUANCY